from django import forms
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class MediaMixin:
    class Media:  # pylint: disable=C1001
        css = {
            "screen": (
                staticfiles_storage.url(
                    "clearable_widget/css/clearable.min.css",
                ),
            ),
        }
        js = (staticfiles_storage.url("clearable_widget/js/clearable.min.js"),)


class ClearableInput(MediaMixin, forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""

        output = super().render(name, value, attrs, renderer)
        return mark_safe(  # noqa: S308 -- rendering our own trusted template
            render_to_string(
                "clearable_widget/input.html",
                {"widget": output, "name": name},
            ),
        )
