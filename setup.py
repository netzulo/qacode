from sys import version_info
from setuptools import setup, find_packages
from os import path


CURR_PATH = path.abspath(path.dirname(__file__))


def get_file(version_py=version_info.major, file_name=None, encoding=None):
    if file_name is None:
        raise Exception('File name couldn\'t be None')
    if encoding is None:
        with open(path.join(CURR_PATH, file_name)) as f:
            return f.read()
    if version_py == 3:
        with open(path.join(CURR_PATH, file_name), encoding=encoding) as f:
            return f.read()
    if version_py== 2:
        with open(path.join(CURR_PATH,file_name)) as f:
            return f.read().decode(encoding)


setup(
    name='qacode',
    version='0.1.9',
    license=get_file(file_name='LICENSE'),
    packages=find_packages(
        exclude=['tests'],
    ),
    description='Main automation lib',
    long_description=get_file(file_name='README.rst', encoding='utf-8'),
    author='Netzulo Open Source',
    author_email='netzuleando@gmail.com',
    url='https://github.com/netzulo/qacode',
    download_url='https://github.com/netzulo/qacode/tarball/v0.1.9',
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
    extras_require={
        'test': 'nose',
    },
)
