# -*- coding: utf-8 -*-
"""All Bot Base functionality for inherit class and expand library"""


from qacode.core.exceptions.core_exception import CoreException


class BotConfig(object):
    """Bot configuration for BotBase or inherit classes"""

    logger_manager = None

    config = None
    log = None

    def __init__(self, config, logger_manager):
        """
        Load all defined options for configure new bots
        (listed on settings.example.ini)

        :args:
            config: JSON example
            {
                "bot": {
                    "mode": "remote",
                    "browser": "chrome",
                    "url_hub": "http://146.255.101.51:11000/wd/hub",
                    "drivers_path": "../qadrivers",
                    "drivers_names": [
                        "chromedriver_32.exe",
                        "chromedriver_64.exe",
                        "chromedriver_32",
                        "chromedriver_64",
                        "firefoxdriver_32.exe",
                        "firefoxdriver_64.exe",
                        "firefoxdriver_64.exe",
                        "firefoxdriver_32",
                        "phantomjsdriver_32.exe",
                        "phantomjsdriver_64.exe",
                        "phantomjsdriver_32",
                        "phantomjsdriver_64",
                        "iexplorerdriver_32.exe",
                        "iexplorerdriver_64.exe",
                        "edgedriver_32.exe",
                        "edgedriver_64.exe"
                    ],
                    "log_output_file": "logs",
                    "log_name": "qacode"
                }
            }
        """
        if config is None:
            raise CoreException("Bot config provived it's None")
        if config['bot'] is None:
            raise CoreException(
                "Bot config provived don't have key named 'bot'")
        self.config = config['bot']
        props = [
            'mode',
            'browser',
            'url_hub',
            'drivers_path',
            'drivers_names',
            'log_name',
            'log_output_file',
            'log_level'
        ]
        self._load_logger_manager(logger_manager)
        for prop in props:
            if self.config['mode'] == 'remote' and prop == 'drivers_names':
                msg = 'drivers_names, not showing drivers for remote session'
                self._log_option_loaded(msg)
            else:
                self._log_option_loaded(self.config[prop])

    def _load_logger_manager(self, logger_manager):
        """
        Initialize new logger_manager fot BotConfig object and return it
        """
        if logger_manager is None:
            raise CoreException(
                "Can't start bot config without logger_manager")
        self.logger_manager = logger_manager
        self.log = self.logger_manager.logger

    def _log_option_loaded(self, option="EMPTY"):
        """
        Write log message with bot option value or show EMPTY as value on log
        """
        msg = 'Bot option={} : {}'
        if option is None:
            self.log.warning(str(msg.format(option, 'Loaded failed')))
        else:
            self.log.debug(str(msg.format(option, 'Loaded success')))
