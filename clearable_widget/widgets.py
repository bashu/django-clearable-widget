# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.staticfiles.storage import staticfiles_storage


class MediaMixin(object):

    class Media:  # pylint: disable=C1001
        css = {
            'screen': (
                staticfiles_storage.url(
                    'clearable_widget/css/clearable.min.css',
                    ),
                )}
        js = (staticfiles_storage.url('clearable_widget/js/clearable.min.js'),)


class ClearableInput(MediaMixin, forms.TextInput):

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''

        if getattr(settings, 'USE_JINJA', False):
            template_name = 'clearable_widget/input.jinja'
        else:
            template_name = 'clearable_widget/input.html'

        output = super(ClearableInput, self).render(name, value, attrs, renderer)
        return mark_safe(render_to_string(template_name, {
            'widget': output, 'name': name}))
