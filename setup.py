import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-clearable-widget',
    version='0.1.3',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    license='BSD License',
    description='Custom widget to add a (x) clear button to your input fields',
    long_description=README,
    url='http://github.com/bashu/django-clearable-widget',
    author='Basil Shubin',
    author_email='basil.shubin@gmail.com',
    install_requires=[
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
