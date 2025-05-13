import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def digitizationknowledge_theme_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "digitizationknowledge_theme_get_sum": digitizationknowledge_theme_get_sum,
    }
