from django import forms
from django.test import TestCase

from clearable_widget.widgets import ClearableInput


class ClearableInputDjangoTest(TestCase):
    def setUp(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)

    def test_render(self):
        response = self.field.widget.render("value", "test", {"id": "id_field"})
        assert all(s in response for s in ("clear-holder", "test"))


class ClearableInputFallbackTest(TestCase):
    def setUp(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)

    def test_render(self):
        response = self.field.widget.render("value", None, {"id": "id_field"})
        assert "clear-holder" in response
