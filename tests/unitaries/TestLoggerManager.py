import unittest, logging
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.loggers.LoggerManager import LoggerManager

logger_manager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)

class TestLoggerManager(TestInfoBase):
    '''
    Check LoggerManager class and all logger levels
    '''
    
    def __init__(self, method_name="TestLoggerManager"):
        super(TestLoggerManager, self).__init__(method_name, logger_manager=logger_manager)

    def test_001_logger_debug(self):        
        """Test: test_001_logger_debug"""
        self.log.debug("Unitary test for check messages with level type DEBUG")

    def test_002_logger_info(self):
        """Test: test_002_logger_info"""
        self.log.info("Unitary test for check messages with level type INFO")

    def test_003_logger_warn(self):
        """Test: test_003_logger_warn"""
        self.log.warn("Unitary test for check messages with level type WARNING")

    def test_004_logger_error(self):
        """Test: test_004_logger_error"""
        self.log.error("Unitary test for check messages with level type ERROR")

    def test_005_logger_critical(self):
        """Test: test_005_logger_critical"""
        self.log.critical("Unitary test for check messages with level type CRITICAL")    

if __name__ == '__main__':
    unittest.main()
