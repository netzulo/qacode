# -*- coding: utf-8 -*-
"""TODO: making new library , totally outdated testlink"""


import os
from testlink.testlinkapi import TestlinkAPIClient
from testlink.testlinkhelper import TestLinkHelper
from qacode.core.exceptions.CoreException import CoreException


class TlBase(object):
    """Testlink API manager class"""

    # Testlink connection
    conn = None
    # Testlink Proyects list
    proyects = None
    # Testlink TestPlans list by proyect id
    plans = None
    # Testlink Builds list by testplan id
    builds = None

    def __init__(self, logger_manager=None, url_api=None, dev_key=None, data=None, generate=False):
        """Instance testlink api and save as self.conn property"""
        if logger_manager is None:
            raise CoreException(message='Testlink logger_manager can\'t be None')
        self.logger_manager = logger_manager
        if url_api is None:
            raise CoreException(message='Testlink url_api can\'t be None')
        self.url_api = url_api
        if dev_key is None:
            raise CoreException(message='Testlink dev_key can\'t be None')
        self.dev_key = dev_key
        if generate is None:
            raise CoreException(message='Testlink create can\'t be None')
        self.generate = generate
        # connect with success params
        self.conn = self.connect()
        # verify content exist
        self.load(data=data)

    def connect(self, url_api=None, dev_key=None):
        """
        SETs 2 environments vars and connect to Testlink API
        + TESTLINK_API_PYTHON_SERVER_URL
        + TESTLINK_API_PYTHON_DEVKEY
        """
        selected_url_api = None
        selected_dev_key = None
        if url_api is None or dev_key is None:
            selected_url_api = self.url_api
            selected_dev_key = self.dev_key
        else:
            selected_url_api = url_api
            selected_url_api = dev_key
        os.environ['TESTLINK_API_PYTHON_SERVER_URL'] = selected_url_api
        os.environ['TESTLINK_API_PYTHON_DEVKEY'] = selected_dev_key
        msg_err = 'Error at connect testlink, api_url={}, dev_key={}'.format(
            selected_url_api, selected_dev_key
        )
        conn = TestLinkHelper().connect(TestlinkAPIClient)
        if conn is None:
            raise CoreException(message=msg_err)

    def load(self, data=None):
        """
        Load all TestProyects, TestPlans, Builds, Testsuites y TestCases
        """
        if self.generate:
            # TODO: Load all param data
            self.proyects = self.get_test_proyects(
                names=data.get('test_proyects'))
        else:
            # TODO: Load all Testlink data
            pass

    def get_test_proyects(self, names=None):
        """
        Obtain from testlink connection: Test Proyects
          Can ensure proyects exists passing list as param
        """
        test_proyects = list()
        if self.generate:
            # TODO: verify if exist and create if not
            pass
        else:
            if names is None:
                test_proyects = self.conn.getProjects()
            for name in names:
                # TODO: test_proyects.append(self.conn.)
                pass
        return test_proyects
