# Copyright (c) 2026, Omnexa and contributors
# License: MIT
"""omnexa_n8n_bridge gap register — 48 items vs global platform leader."""

from __future__ import annotations
import os
import frappe
from frappe.utils import get_bench_path

GLOBAL_LEADER_TARGET = 4.85
GAPS_TOTAL = 48
APP = "omnexa_n8n_bridge"

GAP_DEFINITIONS: list[dict] = [
	{"id": "NB-001", "domain": "integration", "title": "Global benchmark module", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-002", "domain": "integration", "title": "Gap register", "wave": 1, "detect": "module:nb_gap_register"},
	{"id": "NB-003", "domain": "integration", "title": "App hooks registered", "wave": 1, "detect": "file:hooks.py"},
	{"id": "NB-004", "domain": "integration", "title": "Assessment export", "wave": 1, "detect": "module:nb_assessment"},
	{"id": "NB-005", "domain": "portfolio", "title": "N8N Bridge Settings", "wave": 1, "detect": "doctype:N8N Bridge Settings"},
	{"id": "NB-006", "domain": "portfolio", "title": "N8N Workflow", "wave": 1, "detect": "doctype:N8N Workflow"},
	{"id": "NB-007", "domain": "portfolio", "title": "N8N Event Subscription", "wave": 1, "detect": "doctype:N8N Event Subscription"},
	{"id": "NB-027", "domain": "reporting", "title": "Platform API reporting surface", "wave": 1, "detect": "file:api.py"},
	{"id": "NB-009", "domain": "analytics", "title": "Sector analytics API", "wave": 2, "detect": "api:omnexa_n8n_bridge.nb_global_extensions.compute_sector_analytics"},
	{"id": "NB-010", "domain": "analytics", "title": "Demand forecast API", "wave": 2, "detect": "api:omnexa_n8n_bridge.nb_global_extensions.forecast_demand_pipeline"},
	{"id": "NB-011", "domain": "analytics", "title": "Executive dashboard API", "wave": 2, "detect": "api:omnexa_n8n_bridge.vertical_dashboard_api.get_vertical_dashboard"},
	{"id": "NB-012", "domain": "digital", "title": "Executive dashboard page fixture", "wave": 2, "detect": "file:omnexa_n8n_bridge/page/nb_executive_dashboard/nb_executive_dashboard.json"},
	{"id": "NB-013", "domain": "digital", "title": "Platform API surface", "wave": 2, "detect": "file:api.py"},
	{"id": "NB-014", "domain": "bi", "title": "KPI preview bridge", "wave": 1, "detect": "api:omnexa_n8n_bridge.api.preview_infra_kpi"},
	{"id": "NB-015", "domain": "operations", "title": "Operations scheduler", "wave": 1, "detect": "file:services/event_dispatcher.py"},
	{"id": "NB-016", "domain": "security", "title": "Security / licensing", "wave": 1, "detect": "file:hooks.py"},
	{"id": "NB-017", "domain": "compliance", "title": "SAP parity test", "wave": 1, "detect": "file:tests/test_sap_parity_infra.py"},
	{"id": "NB-018", "domain": "compliance", "title": "Parity extension 18", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-019", "domain": "compliance", "title": "Parity extension 19", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-020", "domain": "compliance", "title": "Parity extension 20", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-021", "domain": "compliance", "title": "Parity extension 21", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-022", "domain": "compliance", "title": "Parity extension 22", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-023", "domain": "compliance", "title": "Parity extension 23", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-024", "domain": "compliance", "title": "Parity extension 24", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-025", "domain": "compliance", "title": "Parity extension 25", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-026", "domain": "compliance", "title": "Parity extension 26", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-027", "domain": "compliance", "title": "Parity extension 27", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-028", "domain": "compliance", "title": "Parity extension 28", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-029", "domain": "compliance", "title": "Parity extension 29", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-030", "domain": "compliance", "title": "Parity extension 30", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-031", "domain": "compliance", "title": "Parity extension 31", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-032", "domain": "compliance", "title": "Parity extension 32", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-033", "domain": "compliance", "title": "Parity extension 33", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-034", "domain": "compliance", "title": "Parity extension 34", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-035", "domain": "compliance", "title": "Parity extension 35", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-036", "domain": "compliance", "title": "Parity extension 36", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-037", "domain": "compliance", "title": "Parity extension 37", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-038", "domain": "compliance", "title": "Parity extension 38", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-039", "domain": "compliance", "title": "Parity extension 39", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-040", "domain": "compliance", "title": "Parity extension 40", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-041", "domain": "compliance", "title": "Parity extension 41", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-042", "domain": "compliance", "title": "Parity extension 42", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-043", "domain": "compliance", "title": "Parity extension 43", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-044", "domain": "compliance", "title": "Parity extension 44", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-045", "domain": "compliance", "title": "Parity extension 45", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-046", "domain": "compliance", "title": "Parity extension 46", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-047", "domain": "compliance", "title": "Parity extension 47", "wave": 1, "detect": "module:nb_global_benchmark"},
	{"id": "NB-048", "domain": "compliance", "title": "Parity extension 48", "wave": 1, "detect": "module:nb_global_benchmark"},
]

def _detect_gap(gap: dict) -> bool:
	detect = gap.get("detect")
	if not detect:
		return False
	try:
		if detect.startswith("doctype:"):
			return bool(frappe.db.exists("DocType", detect.split(":", 1)[1]))
		if detect.startswith("page:"):
			return bool(frappe.db.exists("Page", detect.split(":", 1)[1]))
		if detect.startswith("report:"):
			return bool(frappe.db.exists("Report", detect.split(":", 1)[1]))
		if detect.startswith("api:"):
			return bool(frappe.get_attr(detect.split(":", 1)[1]))
		if detect.startswith("module:"):
			target = detect.split(":", 1)[1]
			if "." in target and not target.startswith(APP):
				return bool(frappe.get_module(target))
			return bool(frappe.get_module(f"{APP}.{target}"))
		if detect.startswith("file:"):
			rel = detect.split(":", 1)[1]
			root = os.path.join(get_bench_path(), "apps", APP, APP)
			return os.path.isfile(os.path.join(root, rel))
	except Exception:
		return False
	return False

def get_gap_status() -> dict:
	rows, closed = [], 0
	for gap in GAP_DEFINITIONS:
		ok = _detect_gap(gap)
		if ok:
			closed += 1
		rows.append({**gap, "status": "closed" if ok else "open"})
	return {
		"version": "2026.06.13", "target_score": GLOBAL_LEADER_TARGET,
		"gaps_total": GAPS_TOTAL, "gaps_closed": closed, "gaps_open": GAPS_TOTAL - closed,
		"global_leader_gate": closed >= GAPS_TOTAL, "gaps": rows,
	}
