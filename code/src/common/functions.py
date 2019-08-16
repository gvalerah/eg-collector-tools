# Import logging functions
import              logging
from time   import  strftime

class LevelFilter(object):
    def __init__(self, level):
        self.level = level
        #rint("object %s (%d) filter level is %s"%(self,id(self),level))

    def filter(self, record):
        #rint("record.levelno=%s vs filter level is %s %s"%(record.levelno,self.level,record.levelno != self.level))
        return record.levelno != self.level


def audit(self,message,*args,**kws):
        # Yes, logger takes its '*args' as 'args'.
        self._log(logging.CRITICAL+10, message, args, **kws) 
        
def trace(self,message,*args,**kws):
        # Yes, logger takes its '*args' as 'args'.
        self._log(logging.DEBUG-5, message, args, **kws) 
        
def add_Logging_Level(levelName, levelNum, methodName=None):
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

            
def add_Logging_Handler(logger,level,log_folder,log_format,lh=None):            
        #print("Log: self.logger = %s"%self.logger,id(self.logger))
        if lh is not None:
            logger.removeHandler(lh)

        #logger.setLevel(level)
        # create file handler which logs even debug messages
        file_name = strftime(log_format)
        if level == logging.AUDIT:
            file_name=log_folder+'/aud_'+file_name
        else:
            file_name=log_folder+'/'+file_name
        
        lh = logging.FileHandler(file_name)
        lh.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        lh.setFormatter(formatter)

        logger.addHandler(lh)
        return lh
        
def add_Logging_Levels():            
        add_Logging_Level('TRACE', logging.DEBUG      - 5 )
        add_Logging_Level('AUDIT', logging.CRITICAL   + 10)        
        print(" * Collector's special logging levels TRACE & AUDIT added ...")
        
def Reset_Log_File_Name(logger,log_folder,log_name_format,log_level=logging.INFO,fh=None,Formatter='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
                
        if (fh):
            logger.removeHandler(fh)
            
        if log_level == logging.DEBUG:
            file_name = strftime(log_name_format.replace(".","_%H."))
        else:
            file_name = strftime(log_name_format)
            
        file_name=log_folder+'/'+file_name
        
        
        
        newfh = logging.FileHandler(file_name)

        # create formatter and add it to the handlers

        formatter = logging.Formatter(Formatter)
        newfh.setFormatter(formatter)
        newfh.setLevel(log_level)

        # add the handler to logger
        logger.addHandler(newfh)
        logger.propagate=False
        logger.debug("Reset_Log_File_Name: New FileHandler = %s"%(newfh))
        
        #print()
        return newfh,file_name
                
