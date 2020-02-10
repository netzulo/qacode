# -*- coding: utf-8 -*-
"""Test Suite module for tests.utils package"""


from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(file_path="qacode/configs/", file_name="settings.json")


def setup_selectors():
    """TODO: doc method"""
    # setup parent
    selector = CFG.get('bot').get('controls')[0].get('selector')
    ASSERT.is_instance(selector, str)
    ASSERT.greater(len(selector), 0, "invalid empty selector")
    # setup child
    child_sel = CFG.get('bot').get('controls')[1].get('selector')
    ASSERT.is_instance(child_sel, str)
    ASSERT.greater(len(child_sel), 0, "invalid empty selector")
    # setup child
    children_sel = "*"
    ASSERT.is_instance(child_sel, str)
    ASSERT.greater(len(child_sel), 0, "invalid empty selector")
    return {"parent": selector, "child": child_sel, "children": children_sel}
