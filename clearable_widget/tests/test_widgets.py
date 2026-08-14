from django import forms
from django.conf import settings
from django.template.loader import get_template
from django.test import TestCase

from clearable_widget.widgets import ClearableInput


class ClearableInputDjangoTest(TestCase):
    def setUp(self):
        self.old_USE_JINJA = getattr(settings, "USE_JINJA", False)
        settings.USE_JINJA = False

        self.field = forms.CharField(required=False, widget=ClearableInput)

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_render(self):
        response = self.field.widget.render("value", "test", {"id": "id_field"})
        assert all(s in response for s in ("clear-holder", "test"))


class ClearableInputJinjaTest(TestCase):
    def setUp(self):
        self.old_USE_JINJA = getattr(settings, "USE_JINJA", False)
        settings.USE_JINJA = True

        self.field = forms.CharField(required=False, widget=ClearableInput)

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_render(self):
        response = self.field.widget.render("value", "test", {"id": "id_field"})
        assert all(s in response for s in ("clear-holder", "test"))

    def test_jinja2_backend(self):
        # clearable_widget/input.jinja lives under jinja2/, the app-dirs
        # convention Django's Jinja2 backend uses, so it must be served by
        # a genuine jinja2.Environment rather than falling through to
        # DjangoTemplates just because both accept the same {{ var }} syntax.
        template = get_template("clearable_widget/input.jinja")
        assert template.backend.env.__class__.__module__.startswith("jinja2")


class ClearableInputFallbackTest(TestCase):
    def setUp(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)

    def test_render(self):
        response = self.field.widget.render("value", None, {"id": "id_field"})
        assert "clear-holder" in response
