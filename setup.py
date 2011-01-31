#
# This file is part of python-cli. python-cli is free software that is
# made available under the MIT license. Consult the file "LICENSE" that
# is distributed together with this file for the exact licensing terms.
#
# python-cli is copyright (c) 2011 by the python-cli authors. See the
# file "AUTHORS" for a complete overview.

import os
import sys

from setuptools import setup, Command
from distutils.command.build import build
from setuptools.command.bdist_egg import bdist_egg


class gentab(Command):
    """Generate the PLY parse tables."""

    user_options = []
    description = 'generate parse tables'

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        sys.path.insert(0, 'lib')
        from cli.parser import Parser
        Parser._write_tables()


class mybuild(build):
    """Generate parse tables while building."""

    def run(self):
        self.run_command('gentab')
        build.run(self)
        

class mybdist_egg(bdist_egg):
    """Generate parse tables while building a binary egg."""

    def run(self):
        self.run_command('gentab')
        bdist_egg.run(self)


version_info = {
    'name': 'python-cli',
    'version': '1.0',
    'description': 'A toolkit for CLI construction',
    'author': 'Geert Jansen',
    'author_email': 'gjansen@redhat.com',
    'url': 'http://bitbucket.org/geertj/python-cli',
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python' ],
}


setup(
    package_dir = { '': 'lib' },
    packages = [ 'cli', 'cli.command', 'cli.platform', 'cli.platform.posix' ],
    install_requires = [ 'ply >= 3.3' ],
    entry_points = { 'console_scripts': [ 'cli-test = cli.main:main' ] },
    cmdclass = { 'build': mybuild, 'bdist_egg': mybdist_egg, 'gentab': gentab },
    **version_info
)