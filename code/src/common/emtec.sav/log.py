# Import logging functions
import logging
# Import time formatter fuctions
from time import strftime

AUDIT_LEVEL_NUM = 60

def audit(self,message,*args,**kws):
        # Yes, logger takes its '*args' as 'args'.
        self._log(AUDIT_LEVEL_NUM, message, args, **kws) 

def addLoggingLevel(levelName, levelNum, methodName=None):
        """
        Comprehensively adds a new logging level to the `logging` module and the
        currently configured logging class.
    
        `levelName` becomes an attribute of the `logging` module with the value
        `levelNum`. `methodName` becomes a convenience method for both `logging`
        itself and the class returned by `logging.getLoggerClass()` (usually just
        `logging.Logger`). If `methodName` is not specified, `levelName.lower()` is
        used.
    
        To avoid accidental clobberings of existing attributes, this method will
        raise an `AttributeError` if the level name is already an attribute of the
        `logging` module or if the method name is already present 
    
        Example
        -------
        >>> addLoggingLevel('TRACE', logging.DEBUG - 5)
        >>> logging.getLogger(__name__).setLevel("TRACE")
        >>> logging.getLogger(__name__).trace('that worked')
        >>> logging.trace('so did this')
        >>> logging.TRACE
        5

        """
        if not methodName:
            methodName = levelName.lower()

        if hasattr(logging, levelName):
           #raise AttributeError('{} already defined in logging module'.format(levelName))
           #print( 'AttributeError : {} already defined in logging module'.format(levelName))
           logging.log(logging.INFO,"addLoggingLevel(%s,%s,%s)"%(levelName, levelNum, methodName))
           logging.log(logging.WARNING, 'AttributeError : {} already defined in logging module'.format(levelName))
        else:
            if hasattr(logging, methodName):
               raise AttributeError('{} already defined in logging module'.format(methodName))
            if hasattr(logging.getLoggerClass(), methodName):
               raise AttributeError('{} already defined in logger class'.format(methodName))

            # This method was inspired by the answers to Stack Overflow post
            # http://stackoverflow.com/q/2183233/2988730, especially
            # http://stackoverflow.com/a/13638084/2988730
            def logForLevel(self, message, *args, **kwargs):
                if self.isEnabledFor(levelNum):
                    self._log(levelNum, message, args, **kwargs)
                                 
            def logToRoot(message, *args, **kwargs):
                logging.log(levelNum, message, *args, **kwargs)
    
            logging.addLevelName(levelNum, levelName)
            setattr(logging, levelName, levelNum)
            setattr(logging.getLoggerClass(), methodName, logForLevel)
            setattr(logging, methodName, logToRoot)        
        
class Log:
    """ Emtec 'Log' Class """

    """ Members """
    logger              = None
    fh                  = None
#    ch                  = None
#    ah                  = None
    formatter           = ''
    file_name           = None
#    audit_file_name     = None
    level               = None
    app_folder          = None
    log_folder          = None
    log_format          = None
    log_format_debug    = None
#    audit_folder          = None
#    audit_format          = None
    
    LEVEL_NAME = {0:"NONE",5:"TRACE",10:"DEBUG",20:"INFO",30:"WARNING",40:"ERROR",50:"CRITICAL",60:"AUDIT"}
    
    
    """ Methods """
    def __init__(self,app_name,log_folder,log_format,log_format_debug,level,logger=None):
        # Create logger
        addLoggingLevel('TRACE', logging.DEBUG      - 5 )
        addLoggingLevel('AUDIT', logging.CRITICAL   + 10)
        
        #logging.addLevelName(AUDIT_LEVEL_NUM,"AUDIT")
        #print("Log: Initialize logger from %s"%logger,id(logger))
        if logger is None:
            self.logger = logging.getLogger(app_name)
        else:
            self.logger = logger
            
        #print("Log: self.logger = %s"%self.logger,id(self.logger))    
        self.logger.setLevel(level)
        self.level = level;
        self.log_folder = log_folder;
        self.log_format = log_format;
        #self.audit_folder = "%s/audit"%log_folder;
        #self.audit_format = log_format;

        # create file handler which logs even debug messages
        file_name = strftime(self.log_format)
        self.file_name=log_folder+'/'+file_name
        self.fh = logging.FileHandler(self.file_name)
        self.fh.setLevel(logging.DEBUG)

        ## create file handler which logs audit messages
        #file_name = strftime(self.audit_format)
        #self.audit_file_name=self.audit_folder+'/'+file_name
        #self.ah = logging.FileHandler(self.audit_file_name)
        #self.ah.setLevel(logging.AUDIT)

        # create console handler with a higher log level
        #self.ch = logging.StreamHandler()
        #self.ch.setLevel(logging.ERROR)

        # create formatter and add it to the handlers
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #self.ah.setFormatter(self.formatter)
        #self.ch.setFormatter(self.formatter)
        self.fh.setFormatter(self.formatter)

        # add the handlers to logger
        #self.logger.addHandler(self.ah)
        #self.logger.addHandler(self.ch)
        self.logger.addHandler(self.fh)
        #print("Log.__init__: New log handler added: %s"%self.fh)
        #print("Log.__init__: logger handlers      : %s"%len(self.logger.handlers))
        
    def Reset_Log_File_Name(self):
        # Reset Log File Name
        if (self.fh):
            self.logger.removeHandler(self.fh)
        if self.level == logging.DEBUG:
            file_name = strftime(self.log_format_debug)
        else:
            file_name = strftime(self.log_format)
        self.file_name=self.log_folder+'/'+file_name
        self.fh = logging.FileHandler(self.file_name)
        self.fh.setFormatter(self.formatter)
        # add the handler to logger
        self.logger.addHandler(self.fh)
        #print("Log.reset_Log_File_Name: New log handler added: %s",self.fh)
        #print("Log.reset_Log_File_Name: logger handlers      : %s",len(self.logger.handlers))
        
        """
        # Reset Audit File Name
        if (self.ah):
            self.logger.removeHandler(self.ah)
        else:
            file_name = strftime(self.audit_format)
        self.audit_file_name=self.audit_folder+'/'+file_name
        self.ah = logging.FileHandler(self.audit_file_name)
        self.ah.setFormatter(self.formatter)
        # add the handler to logger
        self.logger.addHandler(self.ah)
        """
                
    def Get_File_Name(self):
        return self.fh.baseFilename
        
    def Get_Level_Name(self):
        return self.LEVEL_NAME[self.level]
        
"""
    def Get_Audit_File_Name(self):
        return self.ah.baseFilename
"""        

        
