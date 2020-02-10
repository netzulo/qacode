# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.testing.asserts import Assert


def asserts_create():
    """TODO: doc mehotd"""
    return Assert()


@pytest.mark.dependency(name="asserts_create")
def test_asserts_create():
    """TODO: doc method"""
    asserts = asserts_create()
    assert type(asserts) == Assert


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_equals():
    """TODO: doc method"""
    asserts = asserts_create()
    asserts.equals("equals", "equals")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notequals():
    """TODO: doc method"""
    asserts = asserts_create()
    asserts.not_equals("equals", "notequals")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_containsurl():
    """TODO: doc method"""
    asserts = asserts_create()
    asserts.contains_url("http://equals.com", "equals.com")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notcontainsurl():
    """TODO: doc method"""
    asserts = asserts_create()
    asserts.not_contains_url("http://equals.com", "notcontains")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_isinstance():
    """TODO: doc method"""
    asserts = asserts_create()
    asserts.is_instance("text", str)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_greater():
    """TODO: doc method"""
    asserts = asserts_create()
    asserts.greater(1, 0)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_lower():
    """TODO: doc method"""
    asserts = asserts_create()
    asserts.lower(0, 1)


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_inlist():
    """TODO: doc method"""
    asserts = asserts_create()
    asserts.in_list(0, [0, 1])


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notinlist():
    """TODO: doc method"""
    asserts = asserts_create()
    asserts.not_in_list(0, [1, 2])


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_regex():
    """TODO: doc method"""
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_regexurl():
    """TODO: doc method"""
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_pathexist():
    """TODO: doc method"""
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_pathnotexist():
    """TODO: doc method"""
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_true():
    """TODO: doc method"""
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_false():
    """TODO: doc method"""
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_none():
    """TODO: doc method"""
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['asserts_create'])
def test_asserts_notnone():
    """TODO: doc method"""
    raise NotImplementedError("WIP: not developed yet")
