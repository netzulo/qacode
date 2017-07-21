import logging, os


class LoggerManager(object):
    '''
    @use: self.get_log()
    TODO: convertir constructor a gestor de loggers
    TODO: cambiar el codigo del constructor que no sea validacion de datos hacia una funcion create
    '''

    def __init__(self,
                 log_path="",
                 log_name="qacode", log_level=logging.DEBUG,
                 is_output_console=True, is_output_file=True):        
        if len(log_path) <= 0 :
            raise Exception("bad format at logger log_path={}".format(log_path))

        if len(log_name) <= 0 and log_name != "qalab-core":
            raise Exception("bad log name provided , log_path={}".format(log_path,))

        if log_level is None:
            log_level = logging.DEBUG

        if not is_output_console and not is_output_file:
            raise Exception("Can't start LoggerManager without any handler, is_output_console={} , is_output_file=".format(is_output_console, is_output_file))

        if os.name == "nt":
            self.log_file_path = "{}\\{}.log".format(log_path, log_name)        
        else:
            self.log_file_path = "{}/{}.log".format(log_path, log_name)        

        # create logger
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_level)
        # add handlers to logger, level and formatter
        self.log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')                
        if is_output_console :
            self.logger.addHandler(self.create_console_handler(log_level,self.log_formatter))
        if is_output_file:
            self.logger.addHandler(self.create_file_handler(log_level,self.log_formatter, self.log_file_path))

    def create_console_handler(self, log_level, log_formatter):
        """create console handler and set logfile level"""
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(log_level)
        consoleHandler.setFormatter(log_formatter)
        return consoleHandler

    def create_file_handler(self, log_level, log_formatter, log_file_path):
        """create console handler and set logfile level"""
        # create file handler
        fileHandler = logging.FileHandler(log_file_path);
        fileHandler.setLevel(log_level)
        fileHandler.setFormatter(log_formatter)
        return fileHandler

    def get_log(self):
        return self.logger
