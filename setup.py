# -*- coding: utf-8 -*-
"""
Peter Nilson 2017 -- http://www.github.com/petenilson
"""
from setuptools import setup

packages = [
    'pexelpie',
]

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pexelpie',
    version='0.0.0.1',
    description='python client for Pexel images',
    packages=packages,
    include_package_data=True,
    install_requires=required,
)