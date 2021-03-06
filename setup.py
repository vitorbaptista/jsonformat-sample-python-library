# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages


with open('jsonformat/__init__.py', 'rb') as f:
    _version_re = re.compile(r'__version__\s+=\s+[\'"](.*)[\'"]')
    version = str(_version_re.search(f.read().decode('utf-8')).group(1))

setup(
    name='jsonformat',
    version=version,
    packages=find_packages(exclude=('tests')),
    entry_points={
        'console_scripts': ['jsonformat=jsonformat.cli:cli'],
    },
    install_requires=[
        'click >= 6.0',
    ],
)
