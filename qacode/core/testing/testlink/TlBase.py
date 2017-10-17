# -*- coding: utf-8 -*-
"""TODO"""


import os
from Testlink import TestlinkAPIClient
from Testlink import TestLinkHelper
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

    def __init__(self, logger_manager=None, url_api=None, dev_key=None):
        """
        Instance testlink api and save as self.conn property
        """
        if logger_manager is None:
            raise CoreException(message='Testlink logger_manager can\'t be None')
        self.logger_manager = logger_manager
        if url_api is None:
            raise CoreException(message='Testlink url_api can\'t be None')
        self.url_api = url_api
        if dev_key is None:
            raise CoreException(message='Testlink dev_key can\'t be None')
        self.dev_key = dev_key
        # connect with success params
        self.conn = self.connect()

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
        else:
            self.load_all()

    def load_all(self):
        """
        Load all TestProyects, TestPlans, Builds, Testsuites y TestCases
        """
        if self.conn is None:
            raise CoreException(
                message='Connection can\'t be None at obtain data')
        # TODO: make functional
        self.proyects = self.get_tl_proyects()
        self.plans = self.get_tl_plans(proyect_ids=[0])
        self.builds = self.get_tl_builds(testplan_ids=[])

    def get_tl_proyects(self):
        """Obtain from testlink connection: Test Proyects"""
        return self.conn.getProjects()

    def get_tl_plans(self, proyect_ids=None):
        """
        USE param, pass ids list as argument
        TODO: without params it's bugged, don't load all data
        """
        plans = list()
        if proyect_ids is None:
            for proyect in self.proyects:
                plans.append(self.conn.getProjectTestPlans(proyect.get('id')))
        else:
            for proyect_id in proyect_ids:
                plans.append(self.conn.getProjectTestPlans(proyect_id))
        return plans

    def get_tl_builds(self, testplan_ids=None):
        """
        USE param, pass ids list as argument
        TODO: without params it's bugged, don't load all data
        """
        builds = list()
        if testplan_ids is None:
            for plan in self.plans[0]:
                builds.append(self.conn.getBuildsForTestPlan(plan.get("id")))
        else:
            for testplan_id in testplan_ids:
                builds.append(self.conn.getBuildsForTestPlan(testplan_id))
        return builds

    def get_tl_milestones(self):
        """TODO"""
        # TODO: not implemented
        pass

    def get_tl_testsuites(self):
        """TODO"""
        # TODO: not implemented
        pass

    def get_tl_testcases(self):
        """TODO"""
        # TODO: not implemented
        pass
