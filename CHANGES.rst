Changes
-------

1.1.0 (2026-08-14)
~~~~~~~~~~~~~~~~~~

* Dropped Python <3.10 / Django <5.2 support; added Django 6.0 / 6.1 support.
* Moved the Jinja2 template into ``clearable_widget/jinja2/`` so it's genuinely
  served by the Jinja2 backend instead of silently falling through to DjangoTemplates.
* Fixed the clear button staying hidden on pre-filled fields until the first keystroke.
* Fixed a dead ``if (form)`` check in ``clearable.js`` that never actually guarded anything.

1.0.0 (2021-11-30)
~~~~~~~~~~~~~~~~~~

* Added Django 3+ support.
* Dropped Python 2.7 support.
* Dropped Django 1.10 / 1.11 support.
