# Import logging functions
import logging
# Import time formatter fuctions
from time import strftime

class Audit:
    """ Nutanix ETL Class """

    """ Members """
    auditor             = None
    fh                  = None
    formatter           = ''
    file_name           = None
    level               = None
    app_folder          = None
    audit_folder          = None
    audit_format          = None
    audit_format_debug    = None
    
    # Level names shared with Log System
    LEVEL_NAME = {0:"NONE",10:"DEBUG",20:"INFO",30:"WARNING",40:"ERROR",50:"CRITICAL"}
    
    """ Methods """
    def __init__(self,app_name=None,audit_folder=None,audit_format=None,level=logging.INFO):
        # Create auditor
        APP="%s_audit"%app_name
        self.auditor    = logging.getLogger(APP)
        self.auditor.setLevel(level)
            
        self.level      = level;
        self.audit_folder = audit_folder;
        self.audit_format = audit_format;

        # create file handler which logs even debug messages
        file_name       = strftime(self.audit_format)
        self.file_name  = audit_folder+'/'+file_name
        self.fh         = logging.FileHandler(self.file_name)
        
        self.fh.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)

        # add the handlers to auditor
        self.auditor.addHandler(self.fh)
        
    def Reset_Audit_File_Name(self):
        if (self.fh):
            self.auditor.removeHandler(self.fh)
        if self.level == logging.DEBUG:
            file_name = strftime(self.audit_format_debug)
        else:
            file_name = strftime(self.audit_format)
        self.file_name=self.audit_folder+'/'+file_name
        self.fh = logging.FileHandler(self.file_name)
        self.fh.setFormatter(self.formatter)
        # add the handler to auditor
        self.auditor.addHandler(self.fh)
                
    def Get_File_Name(self):
        return self.fh.baseFilename
        
    def Get_Level_Name(self):
        return self.LEVEL_NAME[self.level]
