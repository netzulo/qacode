import time, unittest, logging
from testconfig import config as cfg # just works when nose command it's launched>
from qacode.core.exceptions.TestAssertionError import TestAssertionError
from qacode.core.testing.testlink.TestlinkBase import TestlinkBase
from qacode.core.loggers.LoggerManager import LoggerManager
    

class TestInfoBase(unittest.TestCase):

    logger_manager = None
    log = None

    def __init__(self, method_name="NO_TESTCASE_NAME", logger_manager=None):
        super(TestInfoBase, self).__init__(method_name)
        if logger_manager is None:
            self.logger_manager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)
        else:
            self.logger_manager = logger_manager
        self.log = self.logger_manager.get_log()

    @classmethod
    def setUp(cls):
        """
        Just starting testcase instance dependencies
        """
        print("TestInfoBase.setup@classmethod: code mark")

    def setUp(self):        
        """
        Just starting testcase instance dependencies
        Dependencies:
          [core] Instance testlink dependencies
        """
        self.log.debug("TestInfoBase.setup: starting testsuite...")
        # TODO: integrate TestlinkBase class and load testlink data at instance
        #self.testlink = TestlinkBase(url=cfg['TESTLINK']['url'],devkey=cfg['TESTLINK']['devkey'])
        
    
    def tearDown(self):
        """
        Just stoping testcase instance dependencies
        """
        self.log.debug("TestInfoBase.tearDown: finishing testsuite...")

    @classmethod
    def tearDownClass(self):
        """
        Just stoping testcase class dependencies
        """
        print("TestInfoBase.tearDownClass@classmethod: finishing testsuite...")

    def timer(self,wait=5, print_each=5, log=None):
        """
        Notes:
          logger:
          wait: default value it's 5
          print_each: default value it's 5, must be divisible by 5, negatives are accepted
        """
        if log is None:
            raise Exception("Can't execute timer without log")
        if (print_each % 5) != 0:                             
            raise Exception("Can't print timer if print_each is not divisible by 5")
            
        while wait > 0:
            log("Sleeping {} seconds, remaining {} seconds".format(print_each, wait))
            self.sleep(print_each)
            wait -= print_each
        log("Timer terminated...")

    def sleep(self, wait=0):
        """
        Just call to native python time.sleep() method
        Notes:
          Wait time on Runtime execution before execute next lane of code           
        """
        if wait > 0 : 
            time.sleep(wait)

    def assert_equals_url(self, actual, expected, msg='', wait=0):
        """
        Allow to compare 2 urls and check if 1st it's equals to 2nd url
        """
        self.sleep(wait)
        if not actual == expected:
            raise TestAssertionError(actual, expected, 'Wrong URL, not equals: actual='+actual + '| expected='+ expected , msg)        

    def assert_not_equals_url(self, actual, expected, msg='', wait=0):
        """
        Allow to compare 2 urls and check if 1st it isn't equals to 2nd url
        """
        self.sleep(wait)
        if actual == expected:
            raise TestAssertionError(actual, expected, 'Wrong URL, is equals: actual='+actual + '| expected='+ expected , msg)

    def assert_contains_url(self, current, contains, msg='', wait=0):
        """
        Allow to compare 2 urls and check if 1st contains 2nd url
        """
        self.sleep(wait)
        if current not in contains:
            raise TestAssertionError(current, contains, "Wrong URL, current doesn't contains expected: current={}, contains={}".format(current, contains), msg)    

if __name__ == '__main__':
    unittest.main()
