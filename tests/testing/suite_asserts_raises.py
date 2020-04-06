# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.testing.asserts import (ASSERT_REGEX_URL, Assert)


@pytest.mark.dependency(name="asserts_create")
def test_asserts_create():
    """TODO: doc method"""
    asserts = Assert()
    assert type(asserts) == Assert


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_equals_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().equals("equals", "notequals")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notequals_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().not_equals("equals", "equals")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_isinstance_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().is_instance("text", int)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_greater_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().greater(0, 1)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_lower_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().lower(1, 0)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_greaterorequals_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().greater_or_equals(0, 1)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_lowerorequals_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().lower_or_equals(1, 0)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_inlist_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().in_list(0, [1, 2])


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notinlist_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().not_in_list(1, [1, 2])


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_regex_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().regex("doesnotexist", ASSERT_REGEX_URL)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notregex_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().not_regex("http://netzulo.tk:83", ASSERT_REGEX_URL)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_regexurl_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().regex_url("noturl")


@pytest.mark.dependency(depends=['asserts_create'])
@pytest.mark.parametrize("path", ["doesnotexist", "logs/qacode.log"])
def test_asserts_pathexist_raises(path):
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().path_exist(path)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_pathnotexist_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().path_not_exist("./")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_true_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().true(False)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_false_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().false(True)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_none_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().none(":)")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notnone_raises():
    """TODO: doc method"""
    with pytest.raises(AssertionError):
        Assert().not_none(None)
