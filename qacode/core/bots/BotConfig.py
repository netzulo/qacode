# -*- coding: utf-8 -*-
"""
All Bot Base functionality for inherit class and expand library
"""


from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.exceptions.CoreException import CoreException


class BotConfig(object):
    '''
    Bot configuration for BotBase or inherit classes
    '''
    config = None
    logger_manager = None
    log = None

    def __init__(self, config=None, logger_manager=None):
        """
        Load all defined options for configure new bots
        (listed on settings.example.ini)
        """
        if config is None:
            raise CoreException("Bot config provived it's None")
        self.config = config['bot']
        props = [
            'mode',
            'browser',
            'url_hub',
            'url_node',
            'drivers_path',
            'drivers_names',
            'log_name',
            'log_output_file',
        ]
        self.init_logger_manager(logger_manager)
        for prop in props:
            if self.config['mode'] == 'remote' and prop == 'drivers_names':
                self.log_option_loaded('drivers_names, not showing remote node drivers path')
            else:
                self.log_option_loaded(self.config[prop])

    def init_logger_manager(self, logger_manager=None):
        """
        Initialize new logger_manager fot BotConfig object and return it
        """
        if logger_manager is None:
            self.logger_manager = LoggerManager()
        else:
            self.logger_manager = logger_manager
        self.log = self.logger_manager.get_log()
        return self.logger_manager

    def log_option_loaded(self, option="EMPTY"):
        """
        Write log message with bot option value or show EMPTY as value on log
        """
        msg = 'Bot option={} : {}'
        if option is None:
            self.log.warning(str(msg.format(option, 'Loaded failed')))
        else:
            self.log.debug(str(msg.format(option, 'Loaded success')))
