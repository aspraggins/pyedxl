#!/usr/bin/env python
"""EDXL Distribution Element: XML element

The EDXL Distribution Element provides pythonic objects for manipulating
EDXL-DE based on lxml.etree.
"""

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: LGPL
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: Microsoft :: Windows
Operating System :: Unix
"""

from edxl import __version__
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup,find_packages
import sys

if sys.version_info < (2,3):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key('classifiers'):
            del kwargs['classifiers']
        _setup(**kwargs)

setup(name='pyedxl',
      version=__version__,
      packages=find_packages(exclude=['*.tests','*.tests.*','tests.*','tests']),

      install_requires=['lxml>=1.0.3',
                        'python-dateutil'],

      author='Sugree Phatanapherom',
      author_email='sugree@gmail.com',
      description='Python library for handling OASIS EDXL',
      license='LGPL',
      keywords='edxl',
      url='http://code.google.com/p/py-edxl',
      long_description='''\
Python library for handling OASIS Emergency Data Exchange Language (EDXL)
Distribution Element that provides a collection of modules for manipulating
OASIS Emergency Data Exchange Language (EDXL) Distribution Element''',

      maintainer='Sugree Phatanapherom',
      maintainer_email='sugree@gmail.com',
      platforms=['any'],
      classifiers=filter(None,classifiers.split('\n')),
     )
