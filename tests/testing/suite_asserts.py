# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.testing.asserts import (ASSERT_REGEX_URL, Assert)


@pytest.mark.dependency(name="asserts_create")
def test_asserts_create():
    """TODO: doc method"""
    assert type(Assert()) == Assert


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_equals():
    """TODO: doc method"""
    Assert().equals("equals", "equals")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notequals():
    """TODO: doc method"""
    Assert().not_equals("equals", "notequals")


@pytest.mark.dependency(depends=['asserts_create'])
@pytest.mark.parametrize("class_type", [str, " "])
def test_asserts_isinstance(class_type):
    """TODO: doc method"""
    Assert().is_instance("text", class_type)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_greaterorequals():
    """TODO: doc method"""
    Assert().greater_or_equals(1, 0)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_lowerorequals():
    """TODO: doc method"""
    Assert().lower_or_equals(0, 1)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_greater():
    """TODO: doc method"""
    Assert().greater(1, 0)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_lower():
    """TODO: doc method"""
    Assert().lower(0, 1)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_inlist():
    """TODO: doc method"""
    Assert().in_list(0, [0, 1])


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notinlist():
    """TODO: doc method"""
    Assert().not_in_list(0, [1, 2])


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_regex():
    """TODO: doc method"""
    Assert().regex("https://netzulo.tk:83", ASSERT_REGEX_URL)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notregex():
    """TODO: doc method"""
    Assert().not_regex("htttp://lol", ASSERT_REGEX_URL)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_regexurl():
    """TODO: doc method"""
    Assert().regex_url("https://netzulo.tk:83")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_pathexist():
    """TODO: doc method"""
    Assert().path_exist("./")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_pathnotexist():
    """TODO: doc method"""
    Assert().path_not_exist("doesnotexist/")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_true():
    """TODO: doc method"""
    Assert().true(True)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_false():
    """TODO: doc method"""
    Assert().false(False)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_none():
    """TODO: doc method"""
    Assert().none(None)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notnone():
    """TODO: doc method"""
    Assert().not_none(":)")
