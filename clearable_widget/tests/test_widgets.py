# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.test import TestCase

from ..widgets import ClearableInput


class ClearableInputTest(TestCase):

    def test_default(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)

        response = self.field.widget.render('value', None, {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and not "None" in response)


class ClearableInputDjangoTest(TestCase):

    def setUp(self):
        self.old_USE_JINJA = getattr(settings, 'USE_JINJA', False)
        settings.USE_JINJA = False

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_template(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)
        response = self.field.widget.render('value', 'test', {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and 'test' in response)


class ClearableInputJinjaTest(TestCase):

    def setUp(self):
        self.old_USE_JINJA = getattr(settings, 'USE_JINJA', False)
        settings.USE_JINJA = True

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_template(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)
        response = self.field.widget.render('value', 'test', {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and 'test' in response)
