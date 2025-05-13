from flask import Blueprint


digitizationknowledge_theme = Blueprint(
    "digitizationknowledge_theme", __name__)


def page():
    return "Hello, digitizationknowledge_theme!"


digitizationknowledge_theme.add_url_rule(
    "/digitizationknowledge_theme/page", view_func=page)


def get_blueprints():
    return [digitizationknowledge_theme]
