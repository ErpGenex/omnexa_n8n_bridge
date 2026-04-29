from __future__ import annotations

import frappe
from frappe import _
from frappe.utils.password import get_decrypted_password

from omnexa_n8n_bridge.services.n8n_client import request


@frappe.whitelist()
def test_connection():
	"""Basic connectivity test to n8n endpoint."""
	frappe.only_for(("System Manager",))
	try:
		resp = request("/healthz", method="GET")
		return {"ok": True, "response": resp}
	except Exception:
		return {"ok": False, "error": frappe.get_traceback()}


@frappe.whitelist()
def trigger_workflow(workflow: str, reference_doctype: str | None = None, reference_name: str | None = None):
	"""Trigger configured n8n workflow endpoint manually."""
	frappe.only_for(("System Manager",))
	wf = frappe.get_doc("N8N Workflow", workflow)
	payload = {
		"workflow": wf.name,
		"reference_doctype": reference_doctype,
		"reference_name": reference_name,
	}
	try:
		resp = request(wf.workflow_path or "/webhook/manual-trigger", method="POST", payload=payload)
		_create_manual_log(wf.name, payload, resp, status="Success")
		return {"ok": True, "response": resp}
	except Exception:
		_create_manual_log(wf.name, payload, None, status="Failed", error=frappe.get_traceback())
		return {"ok": False, "error": frappe.get_traceback()}


@frappe.whitelist(allow_guest=True)
def inbound_webhook():
	"""Public endpoint for n8n callbacks, protected by shared secret header."""
	secret = (frappe.request.headers.get("X-N8N-SECRET") or "").strip()
	expected = ""
	try:
		expected = get_decrypted_password("N8N Bridge Settings", "N8N Bridge Settings", "webhook_secret")
	except Exception:
		expected = ""

	if not expected or secret != expected:
		frappe.throw(_("Unauthorized webhook call"), frappe.PermissionError)

	payload = frappe.request.get_json(silent=True) or {}
	log = frappe.new_doc("N8N Sync Log")
	log.status = "Success"
	log.event_name = "inbound_webhook"
	log.reference_doctype = payload.get("reference_doctype") or "N/A"
	log.reference_name = payload.get("reference_name") or "N/A"
	log.response_payload = frappe.as_json(payload)
	log.insert(ignore_permissions=True)
	return {"ok": True}


def _create_manual_log(workflow: str, req: dict, resp: dict | None, status: str, error: str | None = None):
	log = frappe.new_doc("N8N Sync Log")
	log.status = status
	log.workflow = workflow
	log.event_name = "manual_trigger"
	log.reference_doctype = req.get("reference_doctype") or "N/A"
	log.reference_name = req.get("reference_name") or "N/A"
	log.request_payload = frappe.as_json(req)
	if resp is not None:
		log.response_payload = frappe.as_json(resp)
	if error:
		log.error_message = error
	log.insert(ignore_permissions=True)
