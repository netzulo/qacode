from setuptools import setup
from os import path
from os import name

CURR_PATH = path.abspath(path.dirname(__file__))
FORMAT_PATH = "{}{}{}"

if name == "nt":
    requirements_path = FORMAT_PATH.format(CURR_PATH,"\\","requirements.txt")
else:
    requirements_path = FORMAT_PATH.format(CURR_PATH,"/","requirements.txt")

with open(requirements_path) as f:
    requirements = f.read().splitlines()

setup(name='qacode',
      version='0.0.2',
      packages=['qacode'],
      description = 'Main automation lib',
      author = 'Netzulo Open Source',
      author_email = 'netzuleando@gmail.com',
      url = 'https://github.com/netzulo/qacode', # use the URL to the github repo
      download_url = 'https://github.com/netzulo/qacode/tarball/v0.0.2',
      keywords = ['testing', 'logging', 'functional','selenium', 'test'],
      install_requires=requirements,
      )
