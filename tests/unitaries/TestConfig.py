import unittest, os, logging
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.loggers.LoggerManager import LoggerManager

class TestConfig(unittest.TestCase):
    '''
    Comprueba el fichero que se pasa por parametro a Nose, si contiene un JSON con la estructura pedida en los tests
    '''
    log = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG).get_log()
    msgs = [
        "Settings file doesn't found, copy from settings.example.ini",
        "Some missing section on settings.ini file",
        "BOT mode just can be : local,remote",
        "BOT browser just can be : firefox , chrome , iexplorer, phantomjs",
        "BOT url_hub just can be match with this regular expression : {}",
        "BOT url_node just can be match with this regular expression : {}",
        "BOT profile_path, optional key: file not found or not provided",
        "BOT drivers_path: path not found or not provided",
        "BOT log_name can't be empty name",
        "BOT log_output_file can't be empty name",
        "TESTLINK url, optional key, not provided or not matching regular expression: {} ",
        "TESTLINK devkey, optional key: file not found",
        "TEST_UNITARIES url just can be  match with this regular expression : {}"
        ]
    regexs = ["http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"]

    def test_000_config_exist(self):
        exist = os.path.exists("qacode/configs/settings.ini")
        self.assertEqual(exist,True,self.msgs[0])

    def test_001_config_nose_loaded(self):
        sections = [cfg["BOT"],cfg["TESTLINK"],cfg["TEST_UNITARIES"]]
        self.assertNotIn(None,sections,self.msgs[1])

    def test_002_config_has_key_bot_mode(self):
        valid_values = ["local", "remote"]
        self.assertIn(cfg.get("BOT")["mode"],valid_values,self.msgs[2])

    def test_003_config_has_key_bot_browser(self):
        valid_values = ["firefox" , "chrome" , "iexplorer", "phantomjs"]
        self.assertIn(cfg.get("BOT")["browser"],valid_values,self.msgs[3])

    def test_004_config_has_key_bot_url_hub(self):
        self.assertRegexpMatches(cfg.get("BOT")["url_hub"],self.regexs[0],
                         self.msgs[4].format(self.regexs[0]))

    def test_005_config_has_key_bot_url_node(self):
        self.assertRegexpMatches(cfg.get("BOT")["url_node"],self.regexs[0],
                         self.msgs[5].format(self.regexs[0]))

    def test_006_config_has_key_bot_profile_path(self):
        value = cfg.get("BOT")["profile_path"]
        exist = os.path.exists(value)
        if not exist:
            self.log.warn(self.msgs[6])

    def test_007_config_has_key_bot_drivers_path(self):
        value = cfg.get("BOT")["drivers_path"]
        exist = os.path.exists(value)
        if not exist:
            self.log.warn(self.msgs[7])

    def test_008_config_has_key_bot_log_name(self):
        value = cfg.get("BOT")["log_name"]
        self.assertNotEqual(value,"",self.msgs[8])

    def test_009_config_has_key_bot_log_output_file(self):
        value = cfg.get("BOT")["log_output_file"]
        self.assertNotEqual(value,"",self.msgs[9])

    def test_010_config_has_key_testlink_url(self):        
        value = cfg.get("TESTLINK")["url"]
        exist_length = len(value)
        if exist_length <= 0:
            self.log.warn(self.msgs[10].format(self.regexs[0]))
        else:
            self.assertRegexpMatches(value,self.regexs[0],self.msgs[10])

    def test_011_config_has_key_testlink_devkey(self):
        value = cfg.get("TESTLINK")["devkey"]
        exist_length = len(value)
        if exist_length <= 0:
            self.log.warn(self.msgs[11])

    def test_012_config_has_key_test_unitaries_url(self):
        self.assertRegexpMatches(cfg.get("TEST_UNITARIES")["url"],self.regexs[0],self.msgs[12])

if __name__ == '__main__':
    unittest.main()
