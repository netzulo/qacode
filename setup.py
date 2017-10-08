# -*- coding: utf-8 -*-
"""qacode module can be installed and configured from here"""


from setuptools import setup, find_packages
from qacode.core.utils.Utils import read_file
from qacode.core.utils.Utils import path_format


def read(file_name=None, is_encoding=True):
    """Read file"""
    if file_name is None:
        raise Exception("File name not provided")
    return read_file(is_encoding=is_encoding,
                     file_path=path_format(
                         file_path='./',
                         file_name=file_name))


setup(
    name='qacode',
    version='0.2.4',
    license=read("LICENSE", is_encoding=False),
    packages=find_packages(exclude=['tests']),
    description='Main automation lib',
    long_description=read("README.rst"),
    author='Netzulo Open Source',
    author_email='netzuleando@gmail.com',
    url='https://github.com/netzulo/qacode',
    download_url='https://github.com/netzulo/qacode/tarball/v0.2.4',
    keywords=['testing', 'logging', 'functional', 'selenium', 'test'],
    install_requires=[
        'appdirs',
        'packaging==16.8',
        'pyparsing',
        'selenium==3.5.0',
        'six==1.10.0',
        'nose==1.3.7',
        'nose-testconfig==0.10',
        'TestLink-API-Python-client==0.6.2',
    ],
    setup_cfg='setup.cfg',
    setup_requires=['pytest-runner'],
    tests_require=[
        'nose',
        'pytest',
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
