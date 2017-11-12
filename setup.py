# -*- coding: utf-8 -*-
# pylint: disable=broad-except
"""qacode module can be installed and configured from here"""

from os import path
from setuptools import setup, find_packages
from qacode.core.utils.Utils import read_file
from qacode.core.utils.Utils import path_format


CURR_PATH = "{}{}".format(path.abspath(path.dirname(__file__)), '/')


def read(file_name=None, is_encoding=True, ignore_raises=False):
    """Read file"""
    if file_name is None:
        raise Exception("File name not provided")
    if ignore_raises:
        try:
            return read_file(is_encoding=is_encoding,
                             file_path=path_format(
                                 file_path=CURR_PATH,
                                 file_name=file_name,
                                 ignore_raises=ignore_raises))
        except Exception:
            #TODO: not silence like this,
            # must be on setup.cfg, README path
            return 'NOTFOUND'
    return read_file(is_encoding=is_encoding,
                     file_path=path_format(
                         file_path=CURR_PATH,
                         file_name=file_name,
                         ignore_raises=ignore_raises))


setup(
    name='qacode',
    version='0.3.5',
    license=read("LICENSE", is_encoding=False, ignore_raises=True),
    packages=find_packages(exclude=['tests']),
    description='Main automation lib',
    long_description=read("README.rst"),
    author='Netzulo Open Source',
    author_email='netzuleando@gmail.com',
    url='https://github.com/netzulo/qacode',
    download_url='https://github.com/netzulo/qacode/tarball/v0.3.5',
    keywords=['testing', 'logging', 'functional', 'selenium', 'test'],
    install_requires=[
        'appdirs',
        'packaging==16.8',
        'pyparsing',
        'selenium==3.5.0',
        'six==1.10.0',
        'nose==1.3.7',
        'nose-testconfig==0.10',
        'pytest',
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest-html',
        'pytest-dependency',
        'pytest-cov',
    ],
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
