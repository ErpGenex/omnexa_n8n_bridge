# Copyright (c) 2026, ErpGenEx
# Auto-generated Global Excellence report pack

import frappe
from frappe import _


def execute(filters=None):
	data = frappe.db.sql(
		"""
		SELECT `name`, `enabled`, `doctype_name`, `event_name`, `workflow`
		FROM `tabN8N Event Subscription`
		ORDER BY modified DESC
		LIMIT 500
		""",
		as_dict=True,
	)
	columns = [
		{"label": _("Name"), "fieldname": "name", "fieldtype": "Link", "width": 140},
		{"label": _("Enabled"), "fieldname": "enabled", "fieldtype": "Check", "width": 120},
		{"label": _("DocType Name"), "fieldname": "doctype_name", "fieldtype": "Data", "width": 120},
		{"label": _("Event"), "fieldname": "event_name", "fieldtype": "Select", "width": 120},
		{"label": _("N8N Workflow"), "fieldname": "workflow", "fieldtype": "Link", "width": 120}
	]
	return columns, data
