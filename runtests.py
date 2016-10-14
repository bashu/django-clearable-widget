#!/usr/bin/env python

import sys
from os import path

import django
from django.conf import settings, global_settings
from django.core.management import execute_from_command_line


if not settings.configured:
    BASE_DIR = path.dirname(path.realpath(__file__))

    settings.configure(
        DEBUG = False,
        TEMPLATE_DEBUG = True,
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                ],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                        'django.template.context_processors.debug',
                        'django.template.context_processors.i18n',
                        'django.template.context_processors.media',
                        'django.template.context_processors.static',
                        'django.template.context_processors.tz',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ],
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.staticfiles',
            'django.contrib.contenttypes',

            'clearable_widget',
        ),
        TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner' if django.VERSION < (1,6) else 'django.test.runner.DiscoverRunner',
        STATIC_URL = '/static/',
    )

def runtests():
    argv = sys.argv[:1] + ['test', 'clearable_widget'] + sys.argv[1:]
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
