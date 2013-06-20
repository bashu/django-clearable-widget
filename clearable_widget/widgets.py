# -*- coding: utf-8 -*-

from django import forms
from django.utils.safestring import mark_safe
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

    def render(self, name, value, attrs=None):
        if value is None: value = ''

        output = """<div class="clear-holder">%(widget)s<span class="clear-helper hidden">&times;</span></div>
<script type="text/javascript">$(document).ready(function() { $('.clear-holder input[name="%(name)s"]').clearable(); });</script>
""" % {'widget': super(ClearableInput, self).render(name, value, attrs), 'name': name}

        return mark_safe(output)
