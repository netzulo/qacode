# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.bots.bot import Bot
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="bot_create")
def test_bot_create_raises():
    """TODO: doc method"""
    with pytest.raises(Exception):
        Bot(None)
