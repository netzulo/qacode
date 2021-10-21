# -*- coding: utf-8 -*-
"""Utils tasks for files operations and settings operations"""


import json
from os import path as PATH


def path_format(path=None, name=None, is_abspath=False, ignore_raises=False):
    """
    Get path joined checking before if path and filepath exist,
     if not, raise an Exception
     if ignore_raise it's enabled, then file_path must include '/' at end lane
    """
    path_formatted = "{}{}".format(path, name)
    if ignore_raises:
        return path_formatted
    if path is None or not PATH.exists(path):
        raise IOError("Path '{}' doesn't exists".format(path))
    if name is None or not PATH.exists(path_formatted):
        raise IOError(
            "File '{}{}' doesn't exists".format(path, name))
    if is_abspath:
        return PATH.abspath(PATH.join(path, name))
    else:
        return PATH.join(path, name)


def read_file(path=None, is_json=False):
    """Returns file object from file path,
       compatible with all py versiones
    optionals:
      can be use to return dict from json path
      can modify encoding used to obtain file
    """
    text = None
    with open(path, encoding="utf-8") as buff:
        text = buff.read()
    if is_json:
        return json.loads(text)
    return text


def settings(path='./', name='settings.json', is_abspath=True):
    """Returns file settings as a dict to be use on qacode lib"""
    path_formatted = path_format(path=path, name=name, is_abspath=is_abspath)
    return read_file(is_json=True, path=path_formatted)
