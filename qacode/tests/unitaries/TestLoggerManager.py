import unittest, logging
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.loggers.LoggerManager import LoggerManager


class TestLoggerManager(unittest.TestCase):
    '''
    Comprueba que funciona la clase LoggerManager y todos sus metodos
    '''
    loggerManager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)
    log = loggerManager.get_log()

    def test_001_logger_debug(self):        
        self.log.debug("Prueba unitaria para el logger, mensaje tipo DEBUG")

    def test_002_logger_info(self):     
        self.log.info("Prueba unitaria para el logger, mensaje tipo INFO")

    def test_003_logger_warn(self):     
        self.log.warn("Prueba unitaria para el logger, mensaje tipo WARNING")

    def test_004_logger_error(self):     
        self.log.error("Prueba unitaria para el logger, mensaje tipo ERROR")

    def test_005_logger_critical(self):
        self.log.critical("Prueba unitaria para el logger, mensaje tipo CRITICAL")    

if __name__ == '__main__':
    unittest.main()
