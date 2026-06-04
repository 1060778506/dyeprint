app_name = "dyeprint"
app_title = "Dyeprint"
app_publisher = "Fengmaode"
app_description = "ERP system for textile dyeing and printing"
app_email = "1060778506@qq.com"
app_license = "mit"







fixtures = [
    {
        "dt": "Workspace",
        "filters": [
            ["name", "=", "印染系统"]
        ]
    },
    {
        "dt": "Workspace Link",
        "filters": [
            ["parent", "=", "印染系统"]
        ]
    },
    {
        "dt": "Workspace Shortcut",
        "filters": [
            ["parent", "=", "印染系统"]
        ]
    },
    {
        "dt": "Workspace Number Card",
        "filters": [
            ["parent", "=", "印染系统"]
        ]
    },
    {
        "dt": "Workspace Chart",
        "filters": [
            ["parent", "=", "印染系统"]
        ]
    },
    {
        "dt": "Workspace Custom Block",
        "filters": [
            ["parent", "=", "印染系统"]
        ]
    },
    {
        "dt": "Workspace Sidebar"
    }
]




# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "dyeprint",
# 		"logo": "/assets/dyeprint/logo.png",
# 		"title": "Dyeprint",
# 		"route": "/dyeprint",
# 		"has_permission": "dyeprint.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dyeprint/css/dyeprint.css"
# app_include_js = "/assets/dyeprint/js/dyeprint.js"

# include js, css files in header of web template
# web_include_css = "/assets/dyeprint/css/dyeprint.css"
# web_include_js = "/assets/dyeprint/js/dyeprint.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dyeprint/public/scss/website"

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
# app_include_icons = "dyeprint/public/icons.svg"

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

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "dyeprint.utils.jinja_methods",
# 	"filters": "dyeprint.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dyeprint.install.before_install"
# after_install = "dyeprint.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dyeprint.uninstall.before_uninstall"
# after_uninstall = "dyeprint.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "dyeprint.utils.before_app_install"
# after_app_install = "dyeprint.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "dyeprint.utils.before_app_uninstall"
# after_app_uninstall = "dyeprint.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "dyeprint.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dyeprint.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dyeprint.tasks.all"
# 	],
# 	"daily": [
# 		"dyeprint.tasks.daily"
# 	],
# 	"hourly": [
# 		"dyeprint.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dyeprint.tasks.weekly"
# 	],
# 	"monthly": [
# 		"dyeprint.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "dyeprint.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "dyeprint.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dyeprint.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dyeprint.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["dyeprint.utils.before_request"]
# after_request = ["dyeprint.utils.after_request"]

# Job Events
# ----------
# before_job = ["dyeprint.utils.before_job"]
# after_job = ["dyeprint.utils.after_job"]

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
# 	"dyeprint.auth.validate"
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

