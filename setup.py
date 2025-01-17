#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lltk import __version__
from lltk import __author__
from lltk import __author_email__

#from distutils.core import setup
from setuptools import setup, find_packages

setup(
	name = "lltk",
	description = "The Language Learning Toolkit (LLTK) performs a variety of tasks useful for (human) language learning.",
	url = "http://github.com/lltk/lltk",
	version = __version__,
	author = __author__,
	author_email = __author_email__,
	license = "LGPL",
	keywords = "language learning toolkit lltk",
	install_requires = [
		"requests",
		"lxml",
#		"Pattern",
		"future",
		"textblob",
	],
	extras_require = {
        ':python_version == "2.7"': [
            'functools32',
        ],
        ':python_version == "3.5"': [
            'google',
        ],
		"couchdb" : ["CouchDB>=0.10"],
	},
	packages = find_packages(),
	package_data = {
		"" : ["*.config"],
	},
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Education",
		"Intended Audience :: Developers",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
		"Natural Language :: Dutch",
		"Natural Language :: English",
		"Natural Language :: French",
		"Natural Language :: German",
		"Natural Language :: Italian",
		"Natural Language :: Spanish",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Text Processing :: Linguistic",
	],
)
