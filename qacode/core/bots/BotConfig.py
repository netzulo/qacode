import logging, ast
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.exceptions.CoreException import CoreException


class BotConfig(object):
    '''
    Bot configuration for BotBase or inherit classes
    '''
    bot_mode = None
    bot_browser = None
    bot_url_hub = None
    bot_url_node = None
    bot_drivers_path = None
    bot_drivers_names = None
    bot_log_name = None
    bot_log_output_file = None
    logger_manager = None
    log = None    

    def __init__(self, nose_config=cfg, logger_manager=None):
        """
        Load all defined options for configure new bots (listed on settings.example.ini)
        """
        self.bot_mode = nose_config['BOT']['mode']
        self.bot_browser = nose_config['BOT']['browser']
        self.bot_url_hub = nose_config['BOT']['url_hub']
        self.bot_url_node = nose_config['BOT']['url_node']
        self.bot_drivers_path = nose_config['BOT']['drivers_path']
        self.bot_drivers_names = ast.literal_eval(nose_config['BOT']['drivers_names'])
        self.bot_log_name = nose_config['BOT']['log_name']
        self.bot_log_output_file = nose_config['BOT']['log_output_file']               

        try:
            self.init_logger_manager(logger_manager)
            self.log_option_loaded(self.bot_mode)
            self.log_option_loaded(self.bot_browser)
            self.log_option_loaded(self.bot_url_hub)
            self.log_option_loaded(self.bot_url_node)
            self.log_option_loaded(self.bot_drivers_path)
            self.log_option_loaded(self.bot_drivers_names)
            self.log_option_loaded(self.bot_log_name)
            self.log_option_loaded(self.bot_log_output_file)                                      
            self.init_logger_manager(logger_manager)
        except Exception as err:
           raise Exception(err,'Error: at create LoggerManager for  BotConfig class')

    def init_logger_manager(self, logger_manager=None):        
        """
        Initialize new logger_manager fot BotConfig object and return it
        """
        if logger_manager is None:
            self.logger_manager = LoggerManager(log_path=self.bot_log_output_file,log_name=self.bot_log_name)            
        else:
            self.logger_manager = logger_manager   
        self.log = self.logger_manager.get_log()
        return self.logger_manager

    def log_option_loaded(self, option="EMPTY"):
        """
        Write log message with bot option value or show EMPTY as value on log
        """
        if option is None : 
            self.log.info('UNLOADED Bot option : {}'.format(option))
        else:
            self.log.info('LOADED Bot option : {}'.format(str(option)))
