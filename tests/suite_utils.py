# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import (path_format, read_file, settings)


ASSERTS = Assert()


@pytest.mark.parametrize("ignore_raises", [True, False])
def test_utils_pathformat(ignore_raises):
    """TODO: doc method"""
    path = path_format(
        path="logs/", name="qacode.log", ignore_raises=ignore_raises)
    ASSERTS.is_instance(path, str)


def test_utils_readfile():
    """TODO: doc method"""
    ASSERTS.is_instance(
        read_file(path="qacode/configs/settings.json"), str)


def test_utils_settings():
    """TODO: doc method"""
    ASSERTS.is_instance(
        settings(path="qacode/configs/", name="settings.json"),
        dict)
