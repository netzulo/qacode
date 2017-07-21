from setuptools import setup
from os import path
from os import name

CURR_PATH = path.abspath(path.dirname(__file__))

setup(name='qacode',
      version='0.0.3',
      packages=['qacode'],
      description = 'Main automation lib',
      author = 'Netzulo Open Source',
      author_email = 'netzuleando@gmail.com',
      url = 'https://github.com/netzulo/qacode',
      download_url = 'https://github.com/netzulo/qacode/tarball/v0.0.3',
      keywords = ['testing', 'logging', 'functional','selenium', 'test'],
      install_requires=[
          'appdirs==1.4.2','packaging==16.8','pyparsing==2.1.10',
          'selenium==3.0.2','six==1.10.0','nose==1.3.7','nose-testconfig==0.10',
          'TestLink-API-Python-client==0.6.2']
      )
