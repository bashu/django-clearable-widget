# -*- coding: utf-8 -*-

from django import forms
from django.test import TestCase

from ..widgets import ClearableInput


class ClearableFieldTest(TestCase):

    def test_default(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)

        response = self.field.widget.render('value', 'test', {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and 'test' in response)

    def test_empty(self):
        self.field = forms.CharField(required=False, widget=ClearableInput)

        response = self.field.widget.render('value', None, {'id': 'id_field'})
        self.assertTrue('clear-holder' in response and not "None" in response)
