# -*- coding: utf-8 -*-
"""
Utils tasks
- files operations
- settings operations
"""


from sys import version_info
from os import path
import json


def get_path_join(file_path=None, file_name=None):
    """Return absolute path for __file__ instance"""
    if file_path is None or not path.exists(file_path):
        raise IOError("Path '{0!s}' doesn't exists")
    if file_name is None or not path.exists(file_name):
        raise IOError("File '{0!s}' doesn't exists")
    return path.join(file_path, file_name)

def read_file(is_json=False, file_path=None, encoding='utf-8', is_encoding=True):
    """Returns file object from file_path,
       compatible with all py versiones
    optionals:
      can be use to return dict from json path
      can modify encoding used to obtain file
    """
    if is_json:
        return json.load(file_path)
    if file_path is None:
        raise Exception("File path received it's None")
    if version_info.major >= 3:
        if not is_encoding:
            encoding = None
        with open(file_path, encoding=encoding) as buff:
            return buff.read()
    if version_info.major <= 2:
        with open(file_path) as buff:
            if is_encoding:
                return buff.read().decode(encoding)
            else:
                return buff.read()

def settings():
    """Returns file settings as a dict to be use on qacode lib"""
    return read_file(is_json=True,
                     file_path=get_path_join(file_path='qacode/configs/',
                                             file_name='settings.json'))
