import logging
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.exceptions.CoreException import CoreException


class BotOptions(object):
    '''
    TODO: classdocs
    '''
    botMode = None
    botBrowser = None
    botUrlHub = None
    botUrlNode = None
    botProfilePath = None
    botDriversPath = None
    botLogName = None
    botLogOutputFile = None

    loggerManager = None
    log = None

    def __init__(self, iniNoseFile=cfg, loggerManager=None):       
        self.botMode = iniNoseFile['BOT']['mode']
        self.botBrowser = iniNoseFile['BOT']['browser']
        self.botUrlHub = iniNoseFile['BOT']['url_hub']
        self.botUrlNode = iniNoseFile['BOT']['url_node']
        self.botProfilePath = iniNoseFile['BOT']['profile_path']
        self.botDriversPath = iniNoseFile['BOT']['drivers_path']
        self.botLogName = iniNoseFile['BOT']['log_name']
        self.botLogOutputFile = iniNoseFile['BOT']['log_output_file']
        
        
        try:
            if loggerManager is None:
                self.loggerManager = LoggerManager(log_path=self.botLogOutputFile,log_name=self.botLogName)
                self.log = self.loggerManager.get_log()
            else:
                self.loggerManager = loggerManager

            self.log_option_loaded(self.botMode)
            self.log_option_loaded(self.botBrowser)
            self.log_option_loaded(self.botUrlHub)
            self.log_option_loaded(self.botUrlNode)
            self.log_option_loaded(self.botProfilePath)
            self.log_option_loaded(self.botDriversPath)
            self.log_option_loaded(self.botLogName)
            self.log_option_loaded(self.botLogOutputFile)
            # TODO: add missing keys to this object                          
        except Exception as err:
           raise CoreException(err,'Error: at create LoggerManager for Bot')

    def log_option_loaded(self, option="EMPTY"):
       self.log.info('LOADED Bot option : {}'.format(str(option)))
