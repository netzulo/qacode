# -*- coding: utf-8 -*-
"""Test Suite module for enums package"""


import pytest
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.testing.test_info import TestInfoBase
from qacode.core.webs.css_properties import CssProperty
from qacode.core.webs.html_attrs import HtmlAttr
from qacode.core.webs.html_tags import HtmlTag
from qacode.core.webs.strict_rules import (
    StrictRule, StrictSeverity, StrictType)
from qautils.files import settings


class Teststrictrules(TestInfoBase):
    """Testcases for class TestInfoBase"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(Teststrictrules, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    @pytest.mark.parametrize("name", ['select', 'table'])
    @pytest.mark.parametrize("strict_type", [StrictType.TAG])
    @pytest.mark.parametrize("severity", [
        StrictSeverity.LOW, StrictSeverity.MEDIUM, StrictSeverity.HIGHT])
    def test_strictrule_tags(self, name, strict_type, severity):
        """Test: test_strictrule_tags"""
        strict_rule = StrictRule(name, strict_type, severity)
        self.assert_is_instance(strict_rule, StrictRule)
        self.assert_equals(strict_rule.enum_type, HtmlTag(name))
        self.assert_equals(strict_rule.name, name)
        self.assert_equals(strict_rule.severity, severity)

    @pytest.mark.parametrize("name", ['id', 'class'])
    @pytest.mark.parametrize("strict_type", [StrictType.HTML_ATTR])
    @pytest.mark.parametrize("severity", [
        StrictSeverity.LOW, StrictSeverity.MEDIUM, StrictSeverity.HIGHT])
    def test_strictrule_htmlattrs(self, name, strict_type, severity):
        """Test: test_strictrule_htmlattrs"""
        strict_rule = StrictRule(name, strict_type, severity)
        self.assert_is_instance(strict_rule, StrictRule)
        self.assert_equals(strict_rule.enum_type, HtmlAttr(name))
        self.assert_equals(strict_rule.name, name)
        self.assert_equals(strict_rule.severity, severity)

    @pytest.mark.parametrize("name", ['display', 'visibility'])
    @pytest.mark.parametrize("strict_type", [StrictType.CSS_PROP])
    @pytest.mark.parametrize("severity", [
        StrictSeverity.LOW, StrictSeverity.MEDIUM, StrictSeverity.HIGHT])
    def test_strictrule_cssprops(self, name, strict_type, severity):
        """Test: test_strictrule_htmlattrs"""
        strict_rule = StrictRule(name, strict_type, severity)
        self.assert_is_instance(strict_rule, StrictRule)
        self.assert_equals(strict_rule.enum_type, CssProperty(name))
        self.assert_equals(strict_rule.name, name)
        self.assert_equals(strict_rule.severity, severity)

    @pytest.mark.parametrize("name", [None, 'select'])
    @pytest.mark.parametrize("strict_type", [None, 'bad', StrictType.TAG])
    @pytest.mark.parametrize("severity", [None])
    def test_strictrule_instance_raises(self, name, strict_type, severity):
        """Test: test_strictrule_instance_raises"""
        with pytest.raises(CoreException):
            StrictRule(name, strict_type, severity)

    @pytest.mark.parametrize("name", ['select'])
    @pytest.mark.parametrize("strict_type", [
        StrictType.JS_EVENT, StrictType.BEHAVIOUR,
        StrictType.USABILITY, StrictType.SEO])
    @pytest.mark.parametrize("severity", [
        StrictSeverity.LOW, StrictSeverity.MEDIUM, StrictSeverity.HIGHT])
    def test_strictrule_notimplementedtypes(self, name, strict_type, severity):
        """Test: test_strictrule_instance_raises"""
        with pytest.raises(NotImplementedError):
            StrictRule(name, strict_type, severity)
