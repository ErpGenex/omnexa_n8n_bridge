# Copyright (c) 2026, ErpGenEx
# Auto-generated Global Excellence report pack

import frappe
from frappe import _


def execute(filters=None):
	data = frappe.db.sql(
		"""
		SELECT `name`, `status`, `workflow`, `event_name`, `reference_doctype`, `reference_name`
		FROM `tabN8N Sync Log`
		ORDER BY modified DESC
		LIMIT 500
		""",
		as_dict=True,
	)
	columns = [
		{"label": _("Name"), "fieldname": "name", "fieldtype": "Link", "width": 140},
		{"label": _("Status"), "fieldname": "status", "fieldtype": "Select", "width": 120},
		{"label": _("N8N Workflow"), "fieldname": "workflow", "fieldtype": "Link", "width": 120},
		{"label": _("Event"), "fieldname": "event_name", "fieldtype": "Data", "width": 120},
		{"label": _("Reference DocType"), "fieldname": "reference_doctype", "fieldtype": "Data", "width": 120},
		{"label": _("Reference Name"), "fieldname": "reference_name", "fieldtype": "Data", "width": 120}
	]
	return columns, data
