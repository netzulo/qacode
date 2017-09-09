from setuptools import setup, find_packages
from os import path
from os import name

CURR_PATH = path.abspath(path.dirname(__file__))

setup(name='qacode',
      version='0.1.5',
      packages=find_packages(exclude=['tests']),
      description = 'Main automation lib',
      author = 'Netzulo Open Source',
      author_email = 'netzuleando@gmail.com',
      url = 'https://github.com/netzulo/qacode',
      download_url = 'https://github.com/netzulo/qacode/tarball/v0.1.5',
      keywords = ['testing', 'logging', 'functional','selenium', 'test'],
      install_requires=[
          'appdirs','packaging==16.8','pyparsing',
          'selenium==3.5.0','six==1.10.0','nose==1.3.7','nose-testconfig==0.10',
          'TestLink-API-Python-client==0.6.2'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'])
