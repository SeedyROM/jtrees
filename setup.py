#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of jtrees.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Chris and Zack <zackkollar@gmail.com>

from setuptools import setup, find_packages
from jtrees import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='jtrees',
    version=__version__,
    description='We got jTrees yo.',
    long_description='''
We got jTrees yo.
''',
    keywords='weed trees json',
    author='Chris and Zack',
    author_email='zackkollar@gmail.com',
    url='https://github.com/someuser/somepackage',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'jtrees=jtrees.cli:main',
        ],
    },
)
