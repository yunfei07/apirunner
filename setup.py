#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
import os

from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))
setup_requirements = []

VERSION = '0.1'


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    author="Jeff Yang",
    author_email='yangyunfei07@gmail.com',
    description='Auto genearate api tests for swagger',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",  # 新参数
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'apirunner', 'swagger', 'swagger test',
    ],
    name='hostz',
    packages=find_packages(include=['apirunner']),
    setup_requires=setup_requirements,
    url='https://github.com/yunfei07/apirunner',
    version=VERSION,
    zip_safe=True,
    install_requires=[]
)
