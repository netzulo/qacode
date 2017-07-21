
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='qacode',
      version='0.0.1',
      packages=['qacode'],
      description = 'Main automation lib',
      author = 'Netzulo Open Source',
      author_email = 'netzuleando@gmail.com',
      url = 'https://github.com/netzulo/qacode', # use the URL to the github repo
      download_url = 'https://github.com/netzulo/qacode/tarball/v0.0.1',
      keywords = ['testing', 'logging', 'functional','selenium', 'test'],
      install_requires=requirements,
      )
