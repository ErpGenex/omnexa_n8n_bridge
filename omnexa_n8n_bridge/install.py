import frappe


def after_install():
	"""Bootstrap defaults for first-time installation."""
	try:
		if not frappe.db.exists("N8N Bridge Settings", "N8N Bridge Settings"):
			doc = frappe.new_doc("N8N Bridge Settings")
			doc.enabled = 1
			doc.connection_mode = "Cloud"
			doc.auth_type = "Bearer Token"
			doc.timeout_seconds = 30
			doc.max_retries = 2
			doc.log_payloads = 0
			doc.save(ignore_permissions=True)
	except Exception:
		frappe.log_error(frappe.get_traceback(), "N8N Bridge: after_install bootstrap")
