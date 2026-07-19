from __future__ import annotations

import json
from typing import Any

import frappe
from frappe.utils.password import get_decrypted_password


def _settings():
	return frappe.get_single("N8N Bridge Settings")


def _headers_from_settings() -> dict[str, str]:
	s = _settings()
	auth_type = (s.auth_type or "").strip()
	headers: dict[str, str] = {"Content-Type": "application/json"}

	if auth_type == "API Key" and s.api_key:
		headers[s.api_key_header or "X-API-KEY"] = get_decrypted_password(
			"N8N Bridge Settings", "N8N Bridge Settings", "api_key"
		)
	elif auth_type == "Bearer Token" and s.bearer_token:
		token = get_decrypted_password("N8N Bridge Settings", "N8N Bridge Settings", "bearer_token")
		headers["Authorization"] = f"Bearer {token}"
	elif auth_type == "Basic Auth" and s.basic_username and s.basic_password:
		username = s.basic_username
		password = get_decrypted_password("N8N Bridge Settings", "N8N Bridge Settings", "basic_password")
		import base64

		basic = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
		headers["Authorization"] = f"Basic {basic}"

	return headers


def request(path: str, method: str = "GET", payload: dict[str, Any] | None = None) -> dict[str, Any]:
	s = _settings()
	base_url = (s.base_url or "").rstrip("/")
	if not base_url:
		frappe.throw("N8N base URL is required in N8N Bridge Settings.")

	timeout = int(s.timeout_seconds or 30)
	headers = _headers_from_settings()
	url = f"{base_url}/{path.lstrip('/')}"
	body = json.dumps(payload or {}).encode("utf-8") if payload is not None else None

	import urllib.request

	req = urllib.request.Request(url=url, data=body, headers=headers, method=method.upper())
	with urllib.request.urlopen(req, timeout=timeout) as resp:
		raw = resp.read().decode("utf-8") or "{}"
		return json.loads(raw)

