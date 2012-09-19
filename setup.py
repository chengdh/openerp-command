# -*- coding: utf-8 -

import os
from setuptools import setup, find_packages
import sys

setup(
    name = 'openerp-command',
    version = '0.0.0',
    description = 'OpenERP command-line tools',
    long_description = '''\
	OpenERP Command provides a set of command-line tools around the OpenERP
        framework: https://launchpad.net/openobject-server. All the tools are
        sub-commands of a single `oe` executable. This project is at its beginning; it
        is not yet ready for public consumption.''',
    author = 'OpenERP s.a.',
    author_email = 'info@openerp.com',
    license = 'AGPL',
    url = 'https://launchpad.net/openerp-command',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Office/Business',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    zip_safe = False,
    packages = find_packages(),
    include_package_data = True,
    entry_points="""
    [console_scripts]
    oe=openerpcommand.main:run
    """,
)
