# -*- coding: utf-8 -*-
"""All Bot Base functionality for inherit class and expand library"""


from qacode.core.exceptions.core_exception import CoreException


class BotConfig(object):
    """Bot configuration for BotBase or inherit classes"""

    bot_keys = [
        'mode',
        'browser',
        'url_hub',
        'drivers_path',
        'drivers_names',
        'log_name',
        'log_output_file',
        'log_level'
    ]
    logger_manager = None
    config = None
    log = None

    def __init__(self, config, logger_manager):
        """Load all defined options for configure new bots
            (listed on settings.example.ini)
            https://github.com/netzulo/qacode/blob/master/qacode/configs/settings.json#L1
            https://github.com/netzulo/qacode/blob/master/qacode/configs/settings.json#L31

        Arguments:
            config {dict} -- JSON example, key bot, lanes 1-31
            logger_manager {LoggerManager} -- class to manage logging messages
        """
        self._load_config(config)
        self._load_logger_manager(logger_manager)
        for key in self.bot_keys:
            if self.config['mode'] == 'remote' and key == 'drivers_names':
                msg = 'drivers_names, not showing drivers for remote session'
                self._log_key_loaded(msg)
            else:
                self._log_key_loaded(self.config[key])

    def _load_config(self, config):
        """Load config from config param and validates key 'bot'

        Arguments:
            config {BotConfig} -- validates instance and keys
                before to start any bot

        Raises:
            CoreException -- param config is None
            CoreException -- param config is not instance
                of BotConfig
            CoreException -- config doesn't have key
                named 'bot'
            CoreException -- config doesn't have key
                named 'bot.mode'
            CoreException -- config doesn't have key
                named 'bot.browser'
            CoreException -- config doesn't have key
                named 'bot.url_hub'
            CoreException -- config doesn't have key
                named 'bot.drivers_path'
            CoreException -- config doesn't have key
                named 'bot.drivers_names'
            CoreException -- config doesn't have key
                named 'bot.log_output_file'
            CoreException -- config doesn't have key
                named 'bot.log_name'
            CoreException -- config doesn't have key
                named 'bot.log_level'
        """
        if config is None:
            raise CoreException("Bot config provived it's None")
        if not isinstance(config, dict):
            raise CoreException(
                "Bot config it's not instance of dict class")
        if 'bot' not in config.keys() or config['bot'] is None:
            raise CoreException(
                "Bot config provived don't have key named 'bot'")
        self.config = config['bot']
        config_bot_keys = config['bot'].keys()
        if 'mode' not in config_bot_keys:
            raise CoreException(
                "Bot config provived don't have key named 'bot.mode'")
        if 'browser' not in config_bot_keys:
            raise CoreException(
                "Bot config provived don't have key named 'bot.browser'")
        if 'url_hub' not in config_bot_keys:
            raise CoreException(
                "Bot config provived don't have key named 'bot.url_hub'")
        if 'drivers_path' not in config_bot_keys:
            raise CoreException(
                "Bot config provived don't have "
                "key named 'bot.drivers_path'")
        if 'drivers_names' not in config_bot_keys:
            raise CoreException(
                "Bot config provived don't have "
                "key named 'bot.drivers_names'")
        if 'log_output_file' not in config_bot_keys:
            raise CoreException(
                "Bot config provived don't have "
                "key named 'bot.log_output_file'")
        if 'log_name' not in config_bot_keys:
            raise CoreException(
                "Bot config provived don't have "
                "key named 'bot.log_name'")
        if 'log_level' not in config_bot_keys:
            raise CoreException(
                "Bot config provived don't have "
                "key named 'bot.log_level'")

    def _load_logger_manager(self, logger_manager):
        """Initialize new logger_manager for BotConfig object
            and return it

        Arguments:
            logger_manager {LoggerManager} -- manager for
                handling logging messages

        Raises:
            CoreException -- if logger_manager param is None

        Returns:
            LoggerManager -- manager for logger
        """
        if logger_manager is None:
            raise CoreException(
                "Can't start bot config without logger_manager")
        self.logger_manager = logger_manager
        self.log = self.logger_manager.logger

    def _log_key_loaded(self, option="EMPTY"):
        """Write log message with bot option value or show
            EMPTY as value on log

        Keyword Arguments:
            option {str} -- name of option (default: {"EMPTY"})
        """
        msg = 'Bot option={} : {}'
        if option is None:
            self.log.warning(str(msg.format(option, 'Loaded failed')))
        else:
            self.log.debug(str(msg.format(option, 'Loaded success')))
