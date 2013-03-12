# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import os

version = '1.0a1'
long_description = open("README.rst").read() + "\n" + \
                   open(os.path.join("docs", "INSTALL.txt")).read() + "\n" + \
                   open(os.path.join("docs", "CREDITS.txt")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='sc.blog',
      version=version,
      description="A content type describing a blog.",
      long_description=long_description,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 4.2",
#          "Framework :: Plone :: 4.3",
          "Intended Audience :: End Users/Desktop",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: JavaScript",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Topic :: Office/Business :: News/Diary",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='plone dexterity blog',
      author='Héctor Velarde',
      author_email='hector@simplesconsultoria.com.br',
      url='https://github.com/simplesconsultoria/sc.blog',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['sc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'collective.nitf',
          'collective.prettydate',
          'five.grok',
          'Pillow',
          'plone.app.dexterity[grok]',
          'plone.namedfile[blobs]',
          'plone.app.referenceablebehavior',
          'plone.app.registry',
          'plone.app.textfield',
          'plone.app.vocabularies',
          'plone.autoform',
          'plone.dexterity',
          'plone.directives.dexterity',
          'plone.directives.form',
          'Products.CMFPlone>=4.2',
          'setuptools',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.testing',
              'robotframework-selenium2library',
              'robotsuite',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )