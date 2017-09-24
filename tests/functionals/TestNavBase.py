import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TesInfoBot import TestInfoBot
from qacode.core.loggers.LoggerManager import LoggerManager

logger_manager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)

class TestNavBase(TestInfoBot):
    """Test Suite for class NavBase"""
    
    def __init__(self, method_name="TestNavBase"):
        super(TestNavBase, self).__init__(method_name, logger_manager=logger_manager)

    def test_001_page_base_go_url_without_wait_param(self):
        try:
            self.bot.navigation.get_url(cfg['TEST_UNITARIES']['url'])
        except Exception as err:
            raise Exception(err)

    def test_001_page_base_go_url_with_wait_param(self):
        try:
            self.bot.navigation.get_url(cfg['TEST_UNITARIES']['url'], wait_for_load=0)
        except Exception as err:
            raise Exception(err)

if __name__ == '__main__':
    unittest.main()
