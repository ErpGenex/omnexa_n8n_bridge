from __future__ import annotations

from typing import Any

import frappe

from omnexa_n8n_bridge.services.n8n_client import request


def _safe_payload(doc, event_name: str) -> dict[str, Any]:
	return {
		"doctype": doc.doctype,
		"name": doc.name,
		"event": event_name,
		"data": doc.as_dict(no_default_fields=False),
	}


def _create_log(
	status: str,
	workflow: str | None,
	event_name: str,
	ref_doctype: str,
	ref_name: str,
	request_payload: dict[str, Any] | None = None,
	response_payload: dict[str, Any] | None = None,
	error_message: str | None = None,
):
	log = frappe.new_doc("N8N Sync Log")
	log.status = status
	log.workflow = workflow
	log.event_name = event_name
	log.reference_doctype = ref_doctype
	log.reference_name = ref_name
	if request_payload:
		log.request_payload = frappe.as_json(request_payload)
	if response_payload:
		log.response_payload = frappe.as_json(response_payload)
	if error_message:
		log.error_message = error_message
	log.insert(ignore_permissions=True)


def dispatch_doc_event(doc, method: str | None = None):
	"""Global hook that dispatches only configured subscriptions."""
	# Never run integration dispatch during install/migrate/patch operations.
	# During schema sync, the subscription DocType tables may not exist yet.
	if (
		getattr(frappe.flags, "in_install", False)
		or getattr(frappe.flags, "in_migrate", False)
		or getattr(frappe.flags, "in_patch", False)
		or getattr(frappe.flags, "in_import", False)
	):
		return

	try:
		settings = frappe.get_single("N8N Bridge Settings")
	except Exception:
		return

	if not settings.enabled:
		return

	event_name = (method or "").strip() or "on_update"
	# If the subscription DocType/table isn't installed yet, silently skip.
	try:
		if not frappe.db.exists("DocType", "N8N Event Subscription"):
			return
		if not frappe.db.table_exists("tabN8N Event Subscription"):
			return
	except Exception:
		return

	try:
		subscriptions = frappe.get_all(
			"N8N Event Subscription",
			filters={"enabled": 1, "doctype_name": doc.doctype, "event_name": event_name},
			fields=["name", "workflow", "workflow_path", "send_full_doc"],
			limit_page_length=200,
		)
	except Exception:
		# Avoid breaking normal saves if schema isn't ready / table missing.
		return
	if not subscriptions:
		return

	for sub in subscriptions:
		try:
			payload = _safe_payload(doc, event_name)
			if not sub.send_full_doc:
				payload = {
					"doctype": doc.doctype,
					"name": doc.name,
					"event": event_name,
				}

			response = request(sub.workflow_path or "/webhook/erp-event", method="POST", payload=payload)
			_create_log(
				status="Success",
				workflow=sub.workflow,
				event_name=event_name,
				ref_doctype=doc.doctype,
				ref_name=doc.name,
				request_payload=payload,
				response_payload=response,
			)
		except Exception:
			_create_log(
				status="Failed",
				workflow=sub.workflow,
				event_name=event_name,
				ref_doctype=doc.doctype,
				ref_name=doc.name,
				error_message=frappe.get_traceback(),
			)
