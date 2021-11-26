from django import forms
from django.views.generic import FormView

from clearable_widget import ClearableInput


class TestForm(forms.Form):

    field = forms.CharField(widget=ClearableInput)


class TestView(FormView):
    form_class = TestForm
