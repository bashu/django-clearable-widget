django-clearable-widget
===

django-clearable-widget is a custom widget that adds a input clearing button on any input fields that are using it. It clears the value, and returns focus to that field.

[![Latest Version](https://pypip.in/version/django-clearable-widget/badge.svg)](https://pypi.python.org/pypi/django-clearable-widget/)
[![Downloads](https://pypip.in/download/django-clearable-widget/badge.svg)](https://pypi.python.org/pypi/django-clearable-widget/)
[![License](https://pypip.in/license/django-clearable-widget/badge.svg)](https://pypi.python.org/pypi/django-clearable-widget/)

## Installation
```shell
$ pip install django-clearable-widget
```
### External dependencies

* jQuery - This is not included in the package since it is expected that in most scenarios this would already be available.

## Setup

Add `clearable_widget` to  `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
	...
	'clearable_widget',
]
```
and just include `clearable_widget` templates
```html
{% include "clearable_widget/clearable_widget_css.html" %} {# Before the closing head tag #}
{% include "clearable_widget/clearable_widget_js.html" %} %} {# Before the closing body tag #}
```
When deploying on production server, don't forget to run :
```shell
$ python manage.py collectstatic
```
## Usage

All you need now is to import ``ClearableInput`` class and override field's widget, for example :
```python
from clearable_widget import ClearableInput

class Form(forms.Form):

    field = forms.CharField(widget=ClearableInput)
```
Please see `example` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.

## License

`django-clearable-widget` is authored by [Basil Shubin](http://resume.github.io/?bashu) and released under the BSD license.
