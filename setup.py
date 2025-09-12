##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.processlifetime package
"""
import os

from setuptools import setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


setup(
    name='zope.processlifetime',
    version='4.0',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    description="Zope process lifetime events",
    long_description=(read('README.rst') + '\n\n' +
                      read('CHANGES.rst')),
    license='ZPL-2.1',
    keywords="zope process lifetime events",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope :: 3',
        'Framework :: Zope :: 5',
    ],
    url='http://github.com/zopefoundation/zope.processlifetime',
    python_requires='>=3.9',
    install_requires=[
        'setuptools',
        'zope.interface',
    ],
    extras_require={
        'test': [
            'zope.testrunner >= 6.4',
        ],
        'docs': [
            'Sphinx',
            'repoze.sphinx.autointerface',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
