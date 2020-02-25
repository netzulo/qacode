# -*- coding: utf-8 -*-
"""Test Suite module for tests.utils package"""


from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


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


def setup_login_selectors():
    """TODO: doc method"""
    # field username
    usr_sel = CFG.get('bot').get('controls')[1].get('selector')
    ASSERT.is_instance(usr_sel, str)
    ASSERT.greater(len(usr_sel), 0, "invalid empty selector")
    # field password
    pwd_sel = CFG.get('bot').get('controls')[2].get('selector')
    ASSERT.is_instance(pwd_sel, str)
    ASSERT.greater(len(pwd_sel), 0, "invalid empty selector")
    # button submit
    submit_sel = CFG.get('bot').get('controls')[3].get('selector')
    ASSERT.is_instance(submit_sel, str)
    ASSERT.greater(len(submit_sel), 0, "invalid empty selector")
    return {"username": usr_sel, "password": pwd_sel, "submit": submit_sel}


def setup_input_selectors():
    """TODO: doc method"""
    title_buttons = CFG.get('bot').get('controls')[6].get('selector')
    ASSERT.is_instance(title_buttons, str)
    ASSERT.greater(len(title_buttons), 0, "invalid empty selector")

    btn_invisible = CFG.get('bot').get('controls')[7].get('selector')
    ASSERT.is_instance(btn_invisible, str)
    ASSERT.greater(len(btn_invisible), 0, "invalid empty selector")

    btn_visible = CFG.get('bot').get('controls')[8].get('selector')
    ASSERT.is_instance(btn_visible, str)
    ASSERT.greater(len(btn_visible), 0, "invalid empty selector")
    return {
        "title": title_buttons,
        "invisible": btn_invisible,
        "visible": btn_visible,
    }


def setup_controls():
    """TODO: doc method"""
    title_buttons = CFG.get('bot').get('controls')[6]
    ASSERT.is_instance(title_buttons, dict)

    btn_invisible = CFG.get('bot').get('controls')[7]
    ASSERT.is_instance(btn_invisible, dict)

    btn_visible = CFG.get('bot').get('controls')[8]
    ASSERT.is_instance(btn_visible, dict)
    return {
        "title": title_buttons,
        "invisible": btn_invisible,
        "visible": btn_visible,
    }


def do_login(browser):
    """TODO: doc method"""
    browser.commons.get_maximize_window()
    # load urls and elements
    url_login = CFG.get('bot').get('pages')[0].get('url')
    ASSERT.not_none(url_login)
    browser.commons.get_url(url_login)
    url_logged = CFG.get('bot').get('pages')[2].get('url')
    ASSERT.not_none(url_logged)
    selectors = setup_login_selectors()
    usr = browser.elements.find(selectors.get("username"))
    pwd = browser.elements.find(selectors.get("password"))
    submit = browser.elements.find(selectors.get("submit"))
    # Do login
    browser.elements.write(usr, "admin")
    browser.elements.write(pwd, "admin")
    browser.elements.click(submit)
    curr_url = browser.commons.get_current_url()
    ASSERT.not_none(curr_url)
    ASSERT.equals(curr_url, url_logged)
