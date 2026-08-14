django-clearable-widget
=======================

.. image:: https://badge.fury.io/py/django-clearable-widget.svg
    :target: https://badge.fury.io/py/django-clearable-widget

.. image:: https://img.shields.io/pypi/pyversions/django-clearable-widget.svg
    :target: https://pypi.python.org/pypi/django-clearable-widget/

.. image:: https://img.shields.io/pypi/djversions/django-clearable-widget.svg
    :target: https://pypi.python.org/pypi/django-clearable-widget/

.. image:: https://github.com/bashu/django-clearable-widget/actions/workflows/test.yml/badge.svg
    :target: https://github.com/bashu/django-clearable-widget/actions/workflows/test.yml

django-clearable-widget is a custom widget that adds a input clearing
button on any input fields that are using it. It clears the value, and
returns focus to that field.

.. raw:: html

    <p align="center">
        <img src="https://raw.githubusercontent.com/bashu/django-clearable-widget/develop/showcase.gif">
    </p>

Installation
------------

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: bash

    pip install django-clearable-widget

External dependencies
~~~~~~~~~~~~~~~~~~~~~

* jQuery - this is not included in the package since it is expected
  that in most scenarios this would already be available.

Setup
-----

Add ``clearable_widget`` to  ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS += (
        'clearable_widget',
    )

and just include ``clearable_widget`` templates

.. code-block:: html+django

    {% include "clearable_widget/clearable_widget_css.html" %} {# Before the closing head tag #}
    {% include "clearable_widget/clearable_widget_js.html" %} {# Before the closing body tag #}

When deploying on production server, don't forget to run:

.. code-block:: shell

    python manage.py collectstatic

Usage
-----

All you need now is to import ``ClearableInput`` class and override
field's widget, for example:

.. code-block:: python

    from clearable_widget import ClearableInput

    class Form(forms.Form):

        field = forms.CharField(widget=ClearableInput)

Please see ``example`` application. This application is used to
manually test the functionalities of this package. This also serves as
a good example.

You need only Django 1.4 or above to run that. It might run on older
versions but that is not tested.

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

License
-------

``django-clearable-widget`` is released under the BSD license.
