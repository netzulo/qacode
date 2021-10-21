# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.controls.control import Control
from qacode.core.exceptions.control_error import ControlError
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from tests.utils import (do_login, menu_left)


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_control_raises_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()
    do_login(browser)


@pytest.mark.dependency(depends=["browser_open"])
@pytest.mark.parametrize("cfg", [CFG.get('bot').get('controls')[0]])
def test_control_checkelementready_raises(browser, cfg):
    """TODO: doc method"""
    ASSERT.not_none(cfg)
    ctl = Control(browser, **cfg)
    with pytest.raises(ControlError):
        ctl.click()


@pytest.mark.dependency(depends=["browser_open"])
def test_control_reload_raises(browser):
    """TODO: doc method"""
    # 1. USE CASE
    # 2. USE CASE
    menu_left(browser, "login")
    ctl = Control(browser, **{"selector": ".alert-heading", "search": True})
    menu_left(browser, "logout")
    with pytest.raises(ControlError):
        ctl.click()
    # 3. USE CASE
