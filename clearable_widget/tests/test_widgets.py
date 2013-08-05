# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.test import TestCase

from ..widgets import ClearableInput


class ClearableInputTest(TestCase):

    def test_jinja_template(self):
        old_USE_JINJA = getattr(settings, 'USE_JINJA', False)
        settings.USE_JINJA = True
        self.field = forms.CharField(required=False, widget=ClearableInput)
        response = self.field.widget.render('value', 'test', {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and 'test' in response)

        settings.USE_JINJA = old_USE_JINJA

    def test_django_template(self):
        old_USE_JINJA = getattr(settings, 'USE_JINJA', False)
        settings.USE_JINJA = False

        self.field = forms.CharField(required=False, widget=ClearableInput)
        response = self.field.widget.render('value', 'test', {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and 'test' in response)

        settings.USE_JINJA = old_USE_JINJA

    def test_empty(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)

        response = self.field.widget.render('value', None, {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and not "None" in response)
