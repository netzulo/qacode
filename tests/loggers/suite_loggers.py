# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.loggers.log import Log
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(file_path="qacode/configs/", file_name="settings.json")


def log_create(cfg, level=None):
    """TODO: doc mehotd"""
    cfg = cfg.get('log').copy()
    if level is not None:
        cfg.update({"level": level})
    return Log(**cfg)


@pytest.mark.dependency(name="log_create")
def test_log_create():
    """TODO: doc method"""
    log = log_create(CFG)
    ASSERT.is_instance(log, Log)


@pytest.mark.dependency(depends=['log_create'])
def test_log_debug():
    """TODO: doc method"""
    log = log_create(CFG, level="DEBUG")
    log.debug("Test DEBUG level")


@pytest.mark.dependency(depends=['log_create'])
def test_log_info():
    """TODO: doc method"""
    log = log_create(CFG, level="INFO")
    log.info("Test INFO level")


@pytest.mark.dependency(depends=['log_create'])
def test_log_warning():
    """TODO: doc method"""
    log = log_create(CFG, level="WARNING")
    log.warning("Test WARNING level")


@pytest.mark.dependency(depends=['log_create'])
def test_log_error():
    """TODO: doc method"""
    log = log_create(CFG, level="ERROR")
    log.error("Test ERROR level")


@pytest.mark.dependency(depends=['log_create'])
def test_log_critical():
    """TODO: doc method"""
    log = log_create(CFG, level="CRITICAL")
    log.critical("Test CRITICAL level")
