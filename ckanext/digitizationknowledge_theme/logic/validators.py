import ckan.plugins.toolkit as tk


def digitizationknowledge_theme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "digitizationknowledge_theme_required": digitizationknowledge_theme_required,
    }
