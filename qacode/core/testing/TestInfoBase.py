import time, unittest
from testconfig import config as cfg # just works when nose command it's launched>
from qacode.core.bots.BotBase import BotBase
from qacode.core.exceptions.TestAssertionError import TestAssertionError
from qacode.core.testing.testlink.TestlinkBase import TestlinkBase
    

class TestInfoBase(unittest.TestCase):

    def __init__(self, methodName="NO_TESTCASE_NAME"):
        super(TestInfoBase, self).__init__(methodName)

    @classmethod
    def setUp(cls):
        """
        Just starting testcase instance dependencies
        """
        pass

    def setUp(self):        
        """
        Just starting testcase instance dependencies
        Dependencies:
          [core] Instance testlink dependencies
        """
        # TODO: integrate TestlinkBase class and load testlink data at instance
        #self.testlink = TestlinkBase(url=cfg['TESTLINK']['url'],devkey=cfg['TESTLINK']['devkey'])
        
    
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

    def assertEqualUrl(self, actual, expected, msg='', wait=0):
        """
        Allow to compare 2 urls and check if 1st it's equals to 2nd url
        """
        self.sleep(wait)
        if not actual == expected:
            raise TestAssertionError(actual, expected, 'Wrong URL, not equals: actual='+actual + '| expected='+ expected , msg)        

    def assertNotEqualUrl(self, actual, expected, msg='', wait=0):
        """
        Allow to compare 2 urls and check if 1st it isn't equals to 2nd url
        """
        self.sleep(wait)
        if actual == expected:
            raise TestAssertionError(actual, expected, 'Wrong URL, is equals: actual='+actual + '| expected='+ expected , msg)

    def assertContainsUrl(self, current, contains, msg='', wait=0):
        """
        Allow to compare 2 urls and check if 1st contains 2nd url
        """
        self.sleep(wait)
        if current not in contains:
            raise TestAssertionError(current, contains, "Wrong URL, current doesn't contains expected: current={}, contains={}".format(current, contains), msg)

    def tearDown(self):
        """
        Just stoping testcase instance dependencies
        """
        pass

    @classmethod
    def tearDownClass(self):
        """
        Just stoping testcase class dependencies
        """
        pass

if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(verbosity=1, failfast=True))
