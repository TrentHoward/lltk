#!/usr/bin/python
# -*- coding: UTF-8 -*-

from builtins import object
import pytest

class TestConfig(object):

	def test_import(self):
		''' Asserts that the module import works. '''

		import lltk.decorators

