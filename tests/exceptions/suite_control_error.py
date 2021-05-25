# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.controls.control import Control
from qacode.core.exceptions.control_error import ControlError
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERTS = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.parametrize("message", ["Failed control"])
@pytest.mark.parametrize("ctl_cfg", [CFG.get('bot').get('controls')[0]])
def test_control_error(browser, message, ctl_cfg):
    """TODO: doc method"""
    exception = ControlError(message, Control(browser, **ctl_cfg))
    ASSERTS.in_list(message, exception.message)
    with pytest.raises(ControlError):
        raise exception
