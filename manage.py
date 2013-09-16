# -*- coding: utf-8 -*-

import os

from django.core.management import execute_manager

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
        }
    }

STATIC_URL = '/site_media/static/'

TEMPLATE_LOADERS = (
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
)

PROJECT_APPS = [
    'clearable_widget',
    ]

INSTALLED_APPS = [
    'django_jinja',
    'django_jenkins',
    'discover_runner',
    ] + PROJECT_APPS

TEST_RUNNER = 'discover_runner.DiscoverRunner'

JENKINS_TASKS = (
    'django_jenkins.tasks.run_flake8',
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_jshint',
    'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.with_coverage',
    )

COVERAGE_EXCLUDES_FOLDERS = ['clearable_widget/tests/*']
PYLINT_RCFILE = os.path.join(PROJECT_ROOT, 'pylint.rc')

if __name__ == "__main__":
    from django.conf import settings
    settings.configure(
        DATABASES = DATABASES,
        INSTALLED_APPS = INSTALLED_APPS,
        STATIC_URL = STATIC_URL,
        PROJECT_APPS = PROJECT_APPS,
        TEST_RUNNER = TEST_RUNNER,
        JENKINS_TASKS = JENKINS_TASKS,
        COVERAGE_EXCLUDES_FOLDERS = COVERAGE_EXCLUDES_FOLDERS,
        PYLINT_RCFILE = PYLINT_RCFILE,
        TEMPLATE_LOADERS = TEMPLATE_LOADERS,
        TEMPLATE_DEBUG = TEMPLATE_DEBUG
        )
    execute_manager(settings)
