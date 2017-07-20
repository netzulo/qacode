import os, testlink
from qacode.core.exceptions.CoreException import CoreException

class TestlinkBase(object):
    """
    Testlink API manager

    example: 
    $ export TESTLINK_API_PYTHON_SERVER_URL=http://10.0.32.66/lib/api/xmlrpc/v1/xmlrpc.php \n
    $ export TESTLINK_API_PYTHON_DEVKEY=014d1ab7cf6232863fd831d87c2879d1 \n
    $ python
    >>> import testlink
    >>> tl = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient) \n
    >>> tc = api.getTestCase(None, testcaseexternalid='prefix-1')
    """

    conn = None # Testlink connection
    proyects = None # Testlink Proyects list
    plans = None # Testlink TestPlans list by proyect id
    builds = None # Testlink Builds list by testplan id

    def __init__(self, url="", devkey=""):
        """
        Instance testlink api and save as self.conn property
        """
        try:
            if ((str(url) == "" or url is None) or (str(devkey) == "" or devkey is None)):
                raise CoreException("Didn't started testlink connection because bad format params : url={} , devkey={}".format(url,devkey))
            else:
                # connect with success params            
                self.url = url
                self.devkey = devkey
                self.conn = self.connect(self.url,self.devkey)
        except (CoreException, Exception) as err:
                raise Exception("FAILED at instance testlink object")

    def connect(self,url, devkey):
        """
        SETs 2 environments vars and connect to Testlink API

        + TESTLINK_API_PYTHON_SERVER_URL
        + TESTLINK_API_PYTHON_DEVKEY
        """
        os.environ['TESTLINK_API_PYTHON_SERVER_URL'] = url
        os.environ['TESTLINK_API_PYTHON_DEVKEY'] = devkey
        conn = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)            
        return conn

    
    def load_all(self):
        """
        Load all TestProyects, TestPlans, Builds, Testsuites y TestCases
        """
        #TODO: make functional ...
        if self.conn is None:
            raise CoreException("None property","self.conn it's null at TestlinkBase class")
        self.proyects = self.get_tl_proyects()
        self.plans = self.get_tl_plans(proyect_ids=[0])
        self.builds = self.get_tl_builds(testplan_ids=[])

    def get_tl_proyects(self):
        proyects = self.conn.getProjects()
        return proyects

        
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
        pass

    def get_tl_milestones(self):
        pass

    def get_tl_milestones(self):
        pass

    def get_tl_testsuites(self):
        pass

    def get_tl_testcases(self):
        pass

# platforms

# tags


#custom fields
