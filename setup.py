# -*- coding: utf-8 -*-
"""Package qacode module can be installed and configured from here"""


from os import path
from setuptools import setup, find_packages
from sys import version_info
try:
    from qautils.files import read
except ImportError:
    raise Exception("Please, install 'qautils' package: pip install qautils")


VERSION = "0.5.5"
CURR_PATH = "{}{}".format(path.abspath(path.dirname(__file__)), '/')
INSTALL_REQUIRES = [
    'appdirs',
    'packaging>=16.8',
    'pyparsing',
    'six==1.10.0',
    'selenium==3.12.0',
    'nose==1.3.7',
    'nose-testconfig==0.10',
    'pytest',
    'qautils==0.0.2',
    'qatestlink==0.1.0',
]
SETUP_REQUIRES = [
    'pytest-runner',
    'tox',
]
TESTS_REQUIRE = [
    'pytest-html',
    'pytest-dependency',
    'coverage==4.3.4',
    'pytest-cov==2.5.0',
    'pytest-benchmark',
    'pytest-benchmark[histogram]',
]
KEYWORDS = ['qacode', 'qa', 'testing', 'logging', 'functional', 'selenium', 'test']
GIT_URL = "https://github.com/netzulo/qacode"
GIT_URL_DOWNLOAD = "{}/tarball/v{}".format(GIT_URL, VERSION)
LICENSE_FILE = read(
    file_path=CURR_PATH,
    file_name="LICENSE",
    is_encoding=False,
    ignore_raises=True)
README_FILE = read(
    file_path=CURR_PATH,
    file_name="README.rst")


def get_install_requires():
    """Get a list of pypi python package dependencies

    Returns:
        list -- list of dependecy package names
    """
    if version_info <= (3, 4):
        INSTALL_REQUIRES.append('enum34')
    return INSTALL_REQUIRES


setup(
    name='qacode',
    version=VERSION,
    license=LICENSE_FILE,
    packages=find_packages(exclude=['tests']),
    description='Main automation lib',
    long_description=README_FILE,
    author='Netzulo Open Source',
    author_email='netzuleando@gmail.com',
    url=GIT_URL,
    download_url=GIT_URL_DOWNLOAD,
    keywords=KEYWORDS,
    install_requires=get_install_requires(),
    setup_requires=SETUP_REQUIRES,
    tests_require=TESTS_REQUIRE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
