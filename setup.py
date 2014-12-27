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
from setuptools import find_packages, setup

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

setup(
    name='zope.processlifetime',
    version='2.0.1.dev0',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    description="Zope process lifetime events",
    long_description=(read('README.rst') + '\n\n' +
                      read('CHANGES.rst')),
    license='ZPL 2.1',
    keywords="zope process lifetime events",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3',
        'Framework :: Zope2',
        ],
    url='http://pypi.python.org/pypi/zope.processlifetime',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    test_suite='zope.processlifetime.tests',
    namespace_packages=['zope'],
    install_requires=['setuptools',
                      'zope.interface',
                     ],
    include_package_data=True,
    zip_safe=False,
    )
