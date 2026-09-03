# Copyright (c) 2026, ErpGenEx
# Auto-generated Global Excellence report pack

import frappe
from frappe import _


def execute(filters=None):
	data = frappe.db.sql(
		"""
		SELECT `name`, `workflow_name`, `workflow_path`, `is_active`
		FROM `tabN8N Workflow`
		ORDER BY modified DESC
		LIMIT 500
		""",
		as_dict=True,
	)
	columns = [
		{"label": _("Name"), "fieldname": "name", "fieldtype": "Link", "width": 140},
		{"label": _("Workflow Name"), "fieldname": "workflow_name", "fieldtype": "Data", "width": 120},
		{"label": _("Workflow Endpoint Path"), "fieldname": "workflow_path", "fieldtype": "Data", "width": 120},
		{"label": _("Is Active"), "fieldname": "is_active", "fieldtype": "Check", "width": 120}
	]
	return columns, data
