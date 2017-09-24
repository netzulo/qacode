import unittest, os, logging, ast
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.loggers.LoggerManager import LoggerManager

logger_manager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)

class TestConfig(TestInfoBase):
    '''
    Comprueba el fichero que se pasa por parametro a Nose, si contiene un JSON con la estructura pedida en los tests
    '''
    msgs = [
        "Settings file doesn't found, copy from settings.example.ini",#0
        "Some missing section on settings.ini file",
        "BOT mode just can be : local,remote",
        "BOT browser just can be : firefox , chrome , iexplorer, phantomjs",
        "BOT url_hub just can be match with this regular expression : {}",
        "BOT url_node just can be match with this regular expression : {}",
        "BOT profile_path, optional key: file not found or not provided",
        "BOT drivers_path: path not found or not provided",
        "BOT drivers_names: path not found for driver_name={}",
        "BOT log_name can't be empty name",
        "BOT log_output_file can't be empty name",#10
        "TESTLINK url, optional key, not provided or not matching regular expression: {} ",
        "TESTLINK devkey, optional key: file not found",
        "TEST_UNITARIES url just can be match with this regular expression : {}",
        "TEST_FUNCTIONALS url_login just can be match with this regular expression : {}",
        "TEST_FUNCTIONALS url_logout just can be match with this regular expression : {}",
        "TEST_FUNCTIONALS url_logged_ok just can be match with this regular expression : {}",
        "TEST_FUNCTIONALS url_logged_ko just can be match with this regular expression : {}",
        "TEST_FUNCTIONALS selectors can't be empty array and can't contain empty selectors",
        "TEST_FUNCTIONALS creed_user, can't be empty string",
        "TEST_FUNCTIONALS creed_pass, can't be empty string", #20
        "BUILD skip_travis_tests, can't be None, just bool values"
        ]
    regexs = ["http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"]

    def __init__(self, method_name="TestConfig"):
        super(TestConfig, self).__init__(method_name, logger_manager=logger_manager)

    def test_000_config_exist(self):
        """Test : test_000_config_exist"""
        exist = os.path.exists("qacode/configs/settings.ini")
        self.assertEqual(exist,True,self.msgs[0])

    def test_001_config_nose_loaded(self):
        """Test : test_001_config_nose_loaded"""
        sections = [cfg["BOT"],cfg["TESTLINK"],cfg["TEST_UNITARIES"]]
        self.assertNotIn(None,sections,self.msgs[1])

    def test_002_config_has_key_bot_mode(self):
        """Test : test_002_config_has_key_bot_mode"""
        valid_values = ["local", "remote"]
        self.assertIn(cfg.get("BOT")["mode"],valid_values,self.msgs[2])

    def test_003_config_has_key_bot_browser(self):
        """Test : test_003_config_has_key_bot_browser"""
        valid_values = ["firefox" , "chrome" , "iexplorer", "phantomjs"]
        self.assertIn(cfg.get("BOT")["browser"],valid_values,self.msgs[3])

    def test_004_config_has_key_bot_url_hub(self):
        """Test : test_004_config_has_key_bot_url_hub"""
        self.assertRegexpMatches(cfg.get("BOT")["url_hub"],self.regexs[0],
                         self.msgs[4].format(self.regexs[0]))

    def test_005_config_has_key_bot_url_node(self):
        """Test : test_005_config_has_key_bot_url_node"""
        self.assertRegexpMatches(cfg.get("BOT")["url_node"],self.regexs[0],
                         self.msgs[5].format(self.regexs[0]))    

    def test_006_config_has_key_bot_drivers_path(self):
        """Test : test_006_config_has_key_bot_drivers_path"""
        value = cfg.get("BOT")["drivers_path"]
        exist = os.path.exists(value)
        if not exist:
            self.log.warn(self.msgs[7])

    def test_007_config_has_key_bot_drivers_names(self):
        """Test : test_007_config_has_key_bot_drivers_names"""
        values = ast.literal_eval(cfg.get("BOT")["drivers_names"])        
        file_path = "{}{}{}".format(cfg.get("BOT")["drivers_path"],"{}", "{}")
        if os.name == "nt":
            file_path = file_path.format("\\","{}")
        else:
            file_path = file_path.format("/","{}")        
        for driver_name in values :
            file_path = file_path.format(driver_name)
            exist = os.path.exists(file_path)
            if not exist:
                self.log.warn(self.msgs[8].format(driver_name))

    def test_008_config_has_key_bot_log_name(self):
        """Test : test_008_config_has_key_bot_log_name"""
        value = cfg.get("BOT")["log_name"]
        self.assertNotEqual(value,"",self.msgs[9])

    def test_009_config_has_key_bot_log_output_file(self):
        """Test : test_009_config_has_key_bot_log_output_file"""
        value = cfg.get("BOT")["log_output_file"]
        self.assertNotEqual(value,"",self.msgs[10])

    def test_010_config_has_key_testlink_url(self):
        """Test : test_010_config_has_key_testlink_url"""
        value = cfg.get("TESTLINK")["url"]
        exist_length = len(value)
        if exist_length <= 0:
            self.log.warn(self.msgs[11].format(self.regexs[0]))
        else:
            self.assertRegexpMatches(value,self.regexs[0],self.msgs[11])

    def test_011_config_has_key_testlink_devkey(self):
        """Test : test_011_config_has_key_testlink_devkey"""
        value = cfg.get("TESTLINK")["devkey"]
        exist_length = len(value)
        if exist_length <= 0:
            self.log.warn(self.msgs[12])

    def test_012_config_has_key_test_unitaries_url(self):
        """Test : test_012_config_has_key_test_unitaries_url"""
        self.assertRegexpMatches(cfg.get("TEST_UNITARIES")["url"],self.regexs[0],self.msgs[13])

    def test_013_config_has_key_test_functionals_url_login(self):
        """Test : test_013_config_has_key_test_functionals_url_login"""
        self.assertRegexpMatches(cfg.get("TEST_FUNCTIONALS")["url_login"],self.regexs[0],self.msgs[14])

    def test_014_config_has_key_test_functionals_url_logout(self):
        """Test : test_014_config_has_key_test_functionals_url_logout"""
        self.assertRegexpMatches(cfg.get("TEST_FUNCTIONALS")["url_logout"],self.regexs[0],self.msgs[15])

    def test_015_config_has_key_test_functionals_url_logged_ok(self):
        """Test : test_015_config_has_key_test_functionals_url_logged_ok"""
        self.assertRegexpMatches(cfg.get("TEST_FUNCTIONALS")["url_logged_ok"],self.regexs[0],self.msgs[16])

    def test_016_config_has_key_test_functionals_url_logged_ko(self):
        """Test : test_016_config_has_key_test_functionals_url_logged_ko"""
        self.assertRegexpMatches(cfg.get("TEST_FUNCTIONALS")["url_logged_ko"],self.regexs[0],self.msgs[17])

    def test_017_config_has_key_test_functionals_selectors_login(self):
        """Test : test_017_config_has_key_test_functionals_selectors_login"""
        values = ast.literal_eval(cfg.get("TEST_FUNCTIONALS")["selectors_login"])
        self.assertEqual(len(values),3,self.msgs[18])
        for value in values:
            self.assertNotEqual(value,"",self.msgs[18])

    def test_018_config_has_key_test_functionals_creed_user(self):
        """Test : test_018_config_has_key_test_functionals_creed_user"""
        value = cfg.get("TEST_FUNCTIONALS")["creed_user"]
        self.assertNotEqual(value,"",self.msgs[19])

    def test_019_config_has_key_test_functionals_creed_pass(self):
        """Test : test_019_config_has_key_test_functionals_creed_pass"""
        value = cfg.get("TEST_FUNCTIONALS")["creed_pass"]
        self.assertNotEqual(value,"",self.msgs[20])

    def test_020_config_has_key_build_skip_travis_tests(self):
        """Test : test_020_config_has_key_build_skip_travis_tests"""
        value = cfg.get("BUILD")["skip_travis_tests"]
        self.assertNotEqual(value,None,self.msgs[21])
        self.assertNotEqual(value,"",self.msgs[21])

if __name__ == '__main__':
    unittest.main()
