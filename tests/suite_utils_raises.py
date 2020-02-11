# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import (path_format, read_file, settings)


ASSERTS = Assert()


@pytest.mark.parametrize("path, name", [
    (None, None), ("logs/", "doesnotexist")
])
def test_utils_pathformat_raises(path, name):
    """TODO: doc method"""
    with pytest.raises(IOError):
        path_format(path=path, name=name)


@pytest.mark.parametrize("path,name", [(None, None)])
def test_utils_readfile(path, name):
    """TODO: doc method"""
    with pytest.raises(Exception):
        read_file(path=path, name=name)


@pytest.mark.parametrize("path,name", [(None, None)])
def test_utils_settings(path, name):
    """TODO: doc method"""
    with pytest.raises(Exception):
        settings(path=path, name=name)
