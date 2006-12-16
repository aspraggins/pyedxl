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

try:
    from setuptools import setup
    from setuptools.extension import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
import sys

if sys.version_info < (2,3):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key('classifiers'):
            del kwargs['classifiers']
        _setup(**kwargs)

doclines = __doc__.split('\n')

setup(name='pyedxl',
      version='0.1',
      maintainer='Sugree Phatanapherom',
      maintainer_email='sugree@gmail.com',
      url='http://code.google.com/p/py-edxl',
      license='http://www.gnu.org/licenses/lgpl.txt',
      platforms=['any'],
      description=doclines[0],
      classifiers=filter(None,classifiers.split('\n')),
      long_description='\n'.join(doclines[2:]),
      packages=['edxl'],
      install_requires=['lxml'],
     )
