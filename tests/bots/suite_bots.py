# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.bots.bot import Bot
from qacode.core.testing.asserts import Assert

_assert = Assert()

@pytest.mark.dependency(name="bot_create")
def test_bot_create():
    """TODO: doc method"""
    bot = Bot()
    _assert.equals(type(bot), Bot)


@pytest.mark.dependency(depends=['bot_create'])
def test_bot_browsers():
    """TODO: doc method"""
    pytest.fail("Not developed yet")


@pytest.mark.dependency(depends=['bot_create'])
def test_bot_pages():
    """TODO: doc method"""
    pytest.fail("Not developed yet")


@pytest.mark.dependency(depends=['bot_create'])
def test_bot_controls():
    """TODO: doc method"""
    pytest.fail("Not developed yet")