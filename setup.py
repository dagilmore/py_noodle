__author__ = 'dgilmore'

#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='py_noodle',
    version='0.1',
    author='David Gilmore',
    author_email='info@dagilmore.com',
    url='http://www.github.com/dagilmore/py_noodle',
    packages=find_packages(),
    install_requires=[
        'Flask==0.10.1',
        'Jinja2==2.7',
        'MarkupSafe==0.18',
        'Werkzeug==0.9.1',
        'itsdangerous==0.21',
        'nose==1.3.0',
        'wsgiref==0.1.2',
    ]
)