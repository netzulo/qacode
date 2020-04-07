# -*- coding: utf-8 -*-
"""Package qacode module can be installed and configured from here"""


import json
from os import path
from setuptools import setup, find_packages
from sys import version_info


def path_format(file_path=None, file_name=None, is_abspath=False,
                ignore_raises=False):
    """
    Get path joined checking before if path and filepath exist,
     if not, raise an Exception
     if ignore_raise it's enabled, then file_path must include '/' at end lane
    """
    path_formatted = "{}{}".format(file_path, file_name)
    if ignore_raises:
        return path_formatted
    if file_path is None or not path.exists(file_path):
        raise IOError("Path '{}' doesn't exists".format(file_path))
    if file_name is None or not path.exists(path_formatted):
        raise IOError(
            "File '{}{}' doesn't exists".format(file_path, file_name))
    if is_abspath:
        return path.abspath(path.join(file_path, file_name))
    else:
        return path.join(file_path, file_name)


def read_file(is_json=False, file_path=None, encoding='utf-8',
              is_encoding=True, ignore_raises=False):
    """Returns file object from file_path,
       compatible with all py versiones
    optionals:
      can be use to return dict from json path
      can modify encoding used to obtain file
    """
    text = None
    try:
        if file_path is None:
            raise Exception("File path received it's None")
        if version_info.major >= 3:
            if not is_encoding:
                encoding = None
            with open(file_path, encoding=encoding) as buff:
                text = buff.read()
        if version_info.major <= 2:
            with open(file_path) as buff:
                if is_encoding:
                    text = buff.read().decode(encoding)
                else:
                    text = buff.read()
        if is_json:
            return json.loads(text)
    except Exception as err:
        if not ignore_raises:
            raise Exception(err)
    return text


def read(file_path='./', file_name=None, is_encoding=True, ignore_raises=False):
    """Read file"""
    if file_name is None:
        raise Exception("File name not provided")
    return read_file(
        is_encoding=is_encoding,
        ignore_raises=ignore_raises,
        file_path=path_format(
            file_path=file_path,
            file_name=file_name,
            ignore_raises=ignore_raises))


VERSION = "0.6.4"
CURR_PATH = "{}{}".format(path.abspath(path.dirname(__file__)), '/')
INSTALL_REQUIRES = [
    'selenium==3.141.0',
    'qatestlink',
]
SETUP_REQUIRES = [
    'pytest-runner',
    'tox',
]
TESTS_REQUIRE = []
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


setup(
    name='qacode',
    version=VERSION,
    license=LICENSE_FILE,
    packages=find_packages(exclude=['tests']),
    description='Main automation library to wrap selenium and automate webs',
    long_description=README_FILE,
    author='Netzulo Open Source',
    author_email='netzuleando@gmail.com',
    url=GIT_URL,
    download_url=GIT_URL_DOWNLOAD,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES,
    setup_requires=SETUP_REQUIRES,
    tests_require=TESTS_REQUIRE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
