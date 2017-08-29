import unittest, logging
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.loggers.LoggerManager import LoggerManager


class TestLoggerManager(unittest.TestCase):
    '''
    Check LoggerManager class and all logger levels
    '''
    loggerManager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)
    log = loggerManager.get_log()

    def test_001_logger_debug(self):        
        self.log.debug("Unitary test for check messages with level type DEBUG")

    def test_002_logger_info(self):     
        self.log.info("Unitary test for check messages with level type INFO")

    def test_003_logger_warn(self):     
        self.log.warn("Unitary test for check messages with level type WARNING")

    def test_004_logger_error(self):     
        self.log.error("Unitary test for check messages with level type ERROR")

    def test_005_logger_critical(self):
        self.log.critical("Unitary test for check messages with level type CRITICAL")    

if __name__ == '__main__':
    unittest.main()
