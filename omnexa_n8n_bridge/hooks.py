app_name = "omnexa_n8n_bridge"
app_title = "Omnexa n8n Bridge"
app_publisher = "ErpGenEx"
app_description = "Unified integration app for n8n cloud and local"
app_email = "dev@erpgenex.com"
app_license = "mit"

# Apps
# ------------------

required_apps = ["omnexa_core"]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "omnexa_n8n_bridge",
# 		"logo": "/assets/omnexa_n8n_bridge/logo.png",
# 		"title": "Omnexa n8n Bridge",
# 		"route": "/omnexa_n8n_bridge",
# 		"has_permission": "omnexa_n8n_bridge.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/omnexa_n8n_bridge/css/omnexa_n8n_bridge.css"
# app_include_js = "/assets/omnexa_n8n_bridge/js/omnexa_n8n_bridge.js"

# include js, css files in header of web template
# web_include_css = "/assets/omnexa_n8n_bridge/css/omnexa_n8n_bridge.css"
# web_include_js = "/assets/omnexa_n8n_bridge/js/omnexa_n8n_bridge.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "omnexa_n8n_bridge/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "omnexa_n8n_bridge/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "omnexa_n8n_bridge.utils.jinja_methods",
# 	"filters": "omnexa_n8n_bridge.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "omnexa_n8n_bridge.install.before_install"
after_install = "omnexa_n8n_bridge.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "omnexa_n8n_bridge.uninstall.before_uninstall"
# after_uninstall = "omnexa_n8n_bridge.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "omnexa_n8n_bridge.utils.before_app_install"
# after_app_install = "omnexa_n8n_bridge.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "omnexa_n8n_bridge.utils.before_app_uninstall"
# after_app_uninstall = "omnexa_n8n_bridge.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "omnexa_n8n_bridge.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"*": {
		"after_insert": "omnexa_n8n_bridge.services.event_dispatcher.dispatch_doc_event",
		"on_update": "omnexa_n8n_bridge.services.event_dispatcher.dispatch_doc_event",
		"on_submit": "omnexa_n8n_bridge.services.event_dispatcher.dispatch_doc_event",
		"on_cancel": "omnexa_n8n_bridge.services.event_dispatcher.dispatch_doc_event",
		"on_trash": "omnexa_n8n_bridge.services.event_dispatcher.dispatch_doc_event",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"omnexa_n8n_bridge.tasks.all"
# 	],
# 	"daily": [
# 		"omnexa_n8n_bridge.tasks.daily"
# 	],
# 	"hourly": [
# 		"omnexa_n8n_bridge.tasks.hourly"
# 	],
# 	"weekly": [
# 		"omnexa_n8n_bridge.tasks.weekly"
# 	],
# 	"monthly": [
# 		"omnexa_n8n_bridge.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "omnexa_n8n_bridge.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "omnexa_n8n_bridge.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "omnexa_n8n_bridge.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["omnexa_n8n_bridge.utils.before_request"]
# after_request = ["omnexa_n8n_bridge.utils.after_request"]

# Job Events
# ----------
# before_job = ["omnexa_n8n_bridge.utils.before_job"]
# after_job = ["omnexa_n8n_bridge.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"omnexa_n8n_bridge.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

