#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools.command.test import test as TestCommand
import metacollect

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the
        #eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


readme = open('README.rst').read()
doclink = """
Documentation
=============

The full documentation is at http://metacollect.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='metacollect',
    version=metacollect.__version__,
    description='Linux shell utility for manage collections',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Marek Wywiał',
    author_email='onjinx@gmail.com',
    url='https://github.com/onjin/metacollect',
    packages=[
        'metacollect',
    ],
    package_dir={'metacollect': 'metacollect'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='metacollect',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    tests_require=['pytest>=2.3.5'],
    cmdclass = {'test': PyTest},
)
