# -*- coding: utf-8 -*-

from django import forms
from django.template.loader import render_to_string
from django.contrib.staticfiles.storage import staticfiles_storage

__all__ = ['ClearableInput']


class MediaMixin(object):

    class Media:
        css = {
            'screen': (
                staticfiles_storage.url('clearable_widget/css/clearable.min.css'),
                )}
        js = (staticfiles_storage.url('clearable_widget/js/clearable.min.js'),)


class ClearableInput(MediaMixin, forms.TextInput):
    template_name = 'clearable_widget/input.html'

    def render(self, name, value, attrs=None):
        if value is None: value = ''

        return render_to_string(self.template_name, {
                'widget': super(ClearableInput, self).render(name, value, attrs), 'name': name})
