# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers package"""


import pytest


@pytest.mark.dependency(depends=['browser_open'])
def test_mod_screenshots_dummy():
    """TODO: doc method"""
    pytest.fail("WIP: not developed yet")
