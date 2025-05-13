"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.digitizationknowledge_theme.logic import validators


def test_digitizationknowledge_theme_reauired_with_valid_value():
    assert validators.digitizationknowledge_theme_required("value") == "value"


def test_digitizationknowledge_theme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.digitizationknowledge_theme_required(None)
