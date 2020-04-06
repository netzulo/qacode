# -*- coding: utf-8 -*-
"""Package for suites and tests related to bots.modules package"""


import pytest
from qacode.core.bots.modules.nav_base import NavBase
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.testing.asserts import Assert
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement


ASSERT = Assert()
SETTINGS = settings(file_path="qacode/configs/")
SKIP_NAVS = SETTINGS['tests']['skip']['bot_navigations']
SKIP_NAVS_MSG = 'bot_navigations DISABLED by config file'


class TestNavBase(TestInfoBotUnique):
    """Test Suite for class NavBase"""

    app = None
    page = None

    @classmethod
    def setup_class(cls, **kwargs):
        """Setup class (suite) to be executed"""
        super(TestNavBase, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_NAVS)

    def setup_method(self, test_method, close=True):
        """Configure self.attribute"""
        super(TestNavBase, self).setup_method(
            test_method,
            config=settings(file_path="qacode/configs/"))
        self.add_property('app', self.cfg_app('qadmin'))
        self.add_property('page', self.cfg_page('qacode_login'))
        self.add_property('txt_username', self.cfg_control('txt_username'))
        self.add_property('txt_password', self.cfg_control('txt_password'))
        self.add_property('btn_submit', self.cfg_control('btn_submit'))
        self.add_property('lst_ordered', self.cfg_control('lst_ordered'))
        self.add_property(
            'lst_ordered_child', self.cfg_control('lst_ordered_child'))
        self.add_property('dd_menu_data', self.cfg_control('dd_menu_data'))
        self.add_property(
            'dd_menu_data_lists', self.cfg_control('dd_menu_data_lists'))
        self.add_property(
            'btn_click_invisible', self.cfg_control('btn_click_invisible'))
        self.add_property(
            'btn_click_visible', self.cfg_control('btn_click_visible'))
        self.add_property('title_buttons', self.cfg_control('title_buttons'))

    def setup_login_to_inputs(self):
        """Do login before to exec some testcases"""
        # setup_login
        self.bot.navigation.get_url(self.page.get('url'), wait_for_load=10)
        txt_username = self.bot.navigation.find_element(
            self.txt_username.get("selector"))
        txt_password = self.bot.navigation.find_element(
            self.txt_password.get("selector"))
        btn_submit = self.bot.navigation.find_element(
            self.btn_submit.get("selector"))
        self.bot.navigation.ele_write(txt_username, "admin")
        self.bot.navigation.ele_write(txt_password, "admin")
        self.bot.navigation.ele_click(btn_submit)
        # end setup_login

    def setup_login_to_data(self):
        """Do login before to exec some testcases"""
        # setup_login
        self.bot.navigation.get_url(self.page.get('url'), wait_for_load=10)
        txt_username = self.bot.navigation.find_element(
            self.txt_username.get("selector"))
        txt_password = self.bot.navigation.find_element(
            self.txt_password.get("selector"))
        btn_submit = self.bot.navigation.find_element(
            self.btn_submit.get("selector"))
        self.bot.navigation.ele_write(txt_username, "admin")
        self.bot.navigation.ele_write(txt_password, "admin")
        self.bot.navigation.ele_click(btn_submit)
        self.bot.navigation.ele_click(
            self.bot.navigation.find_element_wait(
                self.dd_menu_data.get("selector")))
        self.bot.navigation.ele_click(
            self.bot.navigation.find_element_wait(
                self.dd_menu_data_lists.get("selector")))
        # end setup_login

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_navbase_instance(self):
        """Testcase: test_navbase_instance"""
        ASSERT.is_instance(self.bot.navigation, NavBase)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_gourl_withoutwaits(self):
        """Testcase: test_gourl_withoutwaits"""
        self.bot.navigation.get_url(self.page.get('url'))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_gourl_withwaits(self):
        """Testcase: test_gourl_withwaits"""
        self.bot.navigation.get_url(
            self.page.get('url'), wait_for_load=1)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getcurrenturl_ok(self):
        """Testcase: test_getcurrenturl_ok"""
        ASSERT.equals(
            self.bot.navigation.get_current_url(),
            self.page.get('url'))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_isurl_true(self):
        """Testcase: test_isurl_true"""
        ASSERT.true(
            self.bot.navigation.is_url(
                self.bot.navigation.get_current_url()))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_isurl_false(self):
        """Testcase: test_isurl_false"""
        ASSERT.false(self.bot.navigation.is_url(""))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_isurl_raiseswhenurlreturnfalse(self):
        """Testcase: test_isurl_false"""
        with pytest.raises(CoreException):
            self.bot.navigation.is_url("", ignore_raises=False)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_reload_ok(self):
        """Testcase: test_reload_ok"""
        self.bot.navigation.reload()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_forward_ok(self):
        """Testcase: test_reload_ok"""
        self.bot.navigation.forward()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getmaximizewindow_ok(self):
        """Testcase: test_getmaximizewindow_ok"""
        self.bot.navigation.get_maximize_window()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getcapabilities_ok(self):
        """Testcase: test_getcapabilities_ok"""
        caps = self.bot.navigation.get_capabilities()
        ASSERT.is_instance(caps, dict)
        ASSERT.is_instance(caps['chrome'], dict)
        ASSERT.equals(caps['browserName'], 'chrome')

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getlog_ok(self):
        """Testcase: test_getlog_ok"""
        self.bot.navigation.get_url(self.page.get('url'))
        log_data = self.bot.navigation.get_log()
        ASSERT.not_none(log_data)
        self.log.debug("selenium logs, browser={}".format(log_data))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    @pytest.mark.parametrize(
        "log_name", [None, 'browser', 'driver', 'client', 'server'])
    def test_getlog_lognames(self, log_name):
        """Testcase: test_getlog_lognames"""
        self.bot.navigation.get_url(self.page.get('url'))
        if log_name is None:
            with pytest.raises(CoreException):
                self.bot.navigation.get_log(log_name=log_name)
            return True
        log_data = self.bot.navigation.get_log(log_name=log_name)
        ASSERT.not_none(log_data)
        msg = "selenium logs, log_name={}, log_data={}".format(
            log_name, log_data)
        self.log.debug(msg)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelement_ok(self):
        """Testcase: test_findelement_ok"""
        ASSERT.is_instance(
            self.bot.navigation.find_element("body"),
            WebElement)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelement_notfound(self):
        """Testcase: test_findelement_notfound"""
        with pytest.raises(CoreException):
            self.bot.navigation.find_element("article")

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelement_notlocator(self):
        """Testcase: test_findelement_notlocator"""
        with pytest.raises(CoreException):
            self.bot.navigation.find_element(
                "body", locator=None)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelementwait_ok(self):
        """Testcase: test_findelementwait_ok"""
        ASSERT.is_instance(
            self.bot.navigation.find_element_wait("body"),
            WebElement)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelementswait_ok(self):
        """Testcase: test_findelementwait_ok"""
        elements = self.bot.navigation.find_elements_wait("body>*")
        ASSERT.is_instance(elements, list)
        for element in elements:
            ASSERT.is_instance(element, WebElement)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelements_ok(self):
        """Testcase: test_findelement_ok"""
        elements = self.bot.navigation.find_elements("body>*")
        ASSERT.is_instance(elements, list)
        for element in elements:
            ASSERT.is_instance(element, WebElement)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelements_notfound(self):
        """Testcase: test_findelements_notfound"""
        with pytest.raises(CoreException):
            self.bot.navigation.find_elements("article")

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelements_notlocator(self):
        """Testcase: test_findelements_notlocator"""
        with pytest.raises(CoreException):
            self.bot.navigation.find_elements(
                "body", locator=None)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getwindowhandle_ok(self):
        """Testcase: test_getwindowhandle_ok"""
        ASSERT.not_none(
            self.bot.navigation.get_window_handle())

    @pytest.mark.skipIf(
        True, "Depends of remote+local webdrivers to get working")
    def test_addcookie_ok(self):
        """Testcase: test_addcookie_ok"""
        cookie = {"name": "test_cookie", "value": "test_value"}
        self.bot.navigation.add_cookie(cookie)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_addcookie_notparams(self):
        """Testcase: test_addcookie_ok"""
        with pytest.raises(CoreException):
            self.bot.navigation.add_cookie(None)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_addcookie_badcookiekeys(self):
        """Testcase: test_addcookie_ok"""
        with pytest.raises(CoreException):
            self.bot.navigation.add_cookie({})

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getcookies_ok(self):
        """Testcase: test_getcookies_ok"""
        ASSERT.is_instance(
            self.bot.navigation.get_cookies(),
            list)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_deletecookiebykey_ok(self):
        """Testcase: test_deleteallcookies_ok"""
        self.bot.navigation.delete_cookie_by_key("")

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_deleteallcookies_ok(self):
        """Testcase: test_deleteallcookies_ok"""
        self.bot.navigation.delete_cookies()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_setwindowsize_ok(self):
        """Testcase: test_setwindowsize_ok"""
        self.bot.navigation.set_window_size(
            pos_x=1024, pos_y=768)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_gettitle_ok(self):
        """Testcase: test_gettitle_ok"""
        ASSERT.not_none(
            self.bot.navigation.get_title())

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getscreenshotasbase64_ok(self):
        """Testcase: test_getscreenshotasbase64_ok"""
        ASSERT.not_none(
            self.bot.navigation.get_screenshot_as_base64())

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_jssettimeout_ok(self):
        """Testcase: test_jssettimeout_ok"""
        self.bot.navigation.js_set_timeout(1)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_eleclick_okbyselector(self):
        """Testcase: test_eleclick_ok"""
        self.bot.navigation.ele_click(selector="body")

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_eleclick_okbyelement(self):
        """Testcase: test_eleclick_ok"""
        self.bot.navigation.ele_click(
            element=self.bot.navigation.find_element("body"))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_eleclick_notparams(self):
        """Testcase: test_eleclick_notparams"""
        with pytest.raises(CoreException):
            self.bot.navigation.ele_click()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_elewrite_ok(self):
        """Testcase: test_elewrite_ok"""
        self.bot.navigation.ele_write(
            self.bot.navigation.find_element("body"),
            text="test")

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_elewrite_okwithouttext(self):
        """Testcase: test_elewrite_ok"""
        self.bot.navigation.ele_write(
            self.bot.navigation.find_element("body"),
            text=None)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_elewrite_notparams(self):
        """Testcase: test_elewrite_notparams"""
        with pytest.raises(CoreException):
            self.bot.navigation.ele_write(None)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_setwebelement_ok(self):
        """Testcase: test_setwebelement_ok"""
        self.bot.navigation.set_web_element("test-element")

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelementchild_ok(self):
        """Testcase: test_findelementchild_ok"""
        self.setup_login_to_data()
        ele_parent = self.bot.navigation.find_element_wait(
            self.lst_ordered.get("selector"))
        ASSERT.is_instance(ele_parent, WebElement)
        ele_child = self.bot.navigation.find_element_child(
            ele_parent, self.lst_ordered_child.get("selector"))
        ASSERT.is_instance(ele_child, WebElement)
        ASSERT.equals(
            "Item list01", self.bot.navigation.ele_text(ele_child))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelementchildren_ok(self):
        """Testcase: test_findelementchildren_ok"""
        self.setup_login_to_data()
        ele_parent = self.bot.navigation.find_element_wait(
            self.lst_ordered.get("selector"))
        ASSERT.is_instance(ele_parent, WebElement)
        ele_children = self.bot.navigation.find_element_children(
            ele_parent, self.lst_ordered_child.get("selector"))
        ASSERT.is_instance(ele_children, list)
        ASSERT.greater(len(ele_children), 1)
        ASSERT.lower(len(ele_children), 5)
        ASSERT.equals(
            "Item list01",
            self.bot.navigation.ele_text(ele_children[0]))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_elewaitinvisible_ok(self):
        """Testcase: test_elewaitinvisible_ok"""
        self.setup_login_to_inputs()
        selector = self.btn_click_invisible.get("selector")
        ele = self.bot.navigation.find_element_wait(selector)
        ele.click()
        # end setup
        ele = self.bot.navigation.ele_wait_invisible(selector, timeout=7)
        ASSERT.is_instance(ele, WebElement)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_elewaitvisible_ok(self):
        """Testcase: test_elewaitvisible_ok"""
        self.setup_login_to_inputs()
        find_ele = self.bot.navigation.find_element_wait
        ele = find_ele(self.btn_click_invisible.get("selector"))
        ele.click()
        ele_invisible = find_ele(self.btn_click_visible.get("selector"))
        # end setup
        ele_visible = self.bot.navigation.ele_wait_visible(
            ele_invisible, timeout=7)
        ASSERT.is_instance(ele_visible, WebElement)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_elewaittext_ok(self):
        """Testcase: test_elewaitvalue_ok"""
        self.setup_login_to_inputs()
        selector = self.btn_click_invisible.get("selector")
        selector_title = self.title_buttons.get("selector")
        ele_text = self.bot.navigation.find_element_wait(selector)
        ele_text.click()
        # end setup
        is_changed = self.bot.navigation.ele_wait_text(
            selector_title, "Buttonss", timeout=12)
        ASSERT.true(is_changed)
        ASSERT.is_instance(
            self.bot.navigation.ele_text(ele_text),
            "Buttonss")

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_elewaitvalue_ok(self):
        """Testcase: test_elewaitvalue_ok"""
        self.setup_login_to_inputs()
        selector = self.btn_click_invisible.get("selector")
        ele_text = self.bot.navigation.find_element_wait(selector)
        ele_text.click()
        # end setup
        is_changed = self.bot.navigation.ele_wait_value(
            selector, "bad_text", timeout=12)
        ASSERT.true(is_changed)
        ASSERT.is_instance(
            self.bot.navigation.ele_attribute(ele_text, "value"),
            "bad_text")
