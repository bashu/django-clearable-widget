# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.test import TestCase

from clearable_widget.widgets import ClearableInput


class ClearableInputDjangoTest(TestCase):

    def setUp(self):
        self.old_USE_JINJA = getattr(settings, 'USE_JINJA', False)
        settings.USE_JINJA = False

        self.field = forms.CharField(required=False, widget=ClearableInput)

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_render(self):
        response = self.field.widget.render('value', 'test', {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and 'test' in response)


class ClearableInputJinjaTest(TestCase):

    def setUp(self):
        self.old_USE_JINJA = getattr(settings, 'USE_JINJA', False)
        settings.USE_JINJA = True

        self.field = forms.CharField(required=False, widget=ClearableInput)

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_render(self):
        response = self.field.widget.render('value', 'test', {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and 'test' in response)


class ClearableInputEmptyTest(TestCase):

    def setUp(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)

    def test_render(self):
        response = self.field.widget.render('value', None, {'id': 'id_field'})
        self.assertTrue('clear-holder' in response)
