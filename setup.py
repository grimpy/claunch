#!/usr/bin/env python3
from setuptools import setup

setup(name='claunch',
      version='0.1',
      description='Launch process from vscode launch.json file',
      author='Jo De Boeck',
      author_email='deboeck.jo@gmail.com',
      url='http://github.com/grimpy/claunch',
      install_requires=['jstyleson'],
      packages=['claunch'],
      entry_points={'console_scripts': ['claunch=claunch.__main__:main']}
      )
