#!/usr/bin/env python

from setuptools import setup
from toggl.__init__ import __version__ as ver

setup(
	name='TogglAPI',
	version=ver,
	description='API library for toggl.com',
	author='Colin von Heuring',
	author_email='colin@von.heuri.ng',
	url='http://www.github.com/divitu/toggl-api/',
	packages=['toggl'],
	package_dir={'toggl': 'toggl'},
	install_requires=['requests', 'dateparser', 'tabulate'],
	# scripts=['bin/foo'],
)
