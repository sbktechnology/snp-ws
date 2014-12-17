app_name = "snp_ws"
app_title = "S&P Marketing, Inc."
app_publisher = "Systematrix"
app_description = "App for managing S&P Marketing, Inc. Website"
app_icon = "icon-globe"
app_color = "#AFD57D"
app_email = "info@systematrix.co.in"
app_url = "https://frappe.io/apps/snp_ws"
app_version = "0.0.1"

web_include_css = ["assets/snp_ws/css/frappe-io-web.css", "assets/frappe/css/hljs.css"]
web_include_js = "/assets/frappe/js/lib/highlight.pack.js"


fixtures = [
	"Website Settings",
	"Website Script",
	"Contact Us Settings",
	"Web Form"
]


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/snp_ws/css/snp_ws.css"
# app_include_js = "/assets/snp_ws/js/snp_ws.js"

# include js, css files in header of web template
# web_include_css = "/assets/snp_ws/css/snp_ws.css"
# web_include_js = "/assets/snp_ws/js/snp_ws.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "snp_ws.install.before_install"
# after_install = "snp_ws.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "snp_ws.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"snp_ws.tasks.all"
# 	],
# 	"daily": [
# 		"snp_ws.tasks.daily"
# 	],
# 	"hourly": [
# 		"snp_ws.tasks.hourly"
# 	],
# 	"weekly": [
# 		"snp_ws.tasks.weekly"
# 	]
# 	"monthly": [
# 		"snp_ws.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "snp_ws.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "snp_ws.event.get_events"
# }

