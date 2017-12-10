#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of jtrees.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Chris and Zack <zackkollar@gmail.com>

from preggy import expect

from jtrees import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        print(f'{2 + 2}')
        expect(__version__).to_equal('0.1.0')
