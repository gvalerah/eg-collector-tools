# import system modules
import os
import calendar
# Import configuration functions
import configparser
from time                                           import strftime

# Import Emtec's modules
from emtec                                          import *
from emtec.collector.db.orm                         import *
from emtec.collector.db.orm_model                   import *
from emtec.collector.common.context                 import Context
#from emtec.class_whisper                            import *

def EG_Monitor_Collector(C,ini_file):
    C.logger.info("%s: EG Monitor Collector: Execution start"%(__name__))
    C.logger.info("%s: Using Configuration file: %s"%(__name__,ini_file))

    if (os.path.isfile(ini_file)):    
        config          =   configparser.ConfigParser()
        
        config.read(ini_file)
        
        # Dealing with time data
              
        name            =   config['General']['name']
        active          =   config.getboolean('General','active')
        if active:
            today           =   strftime("%Y-%m-%d")

            count_modified = 0
        
            # for every C.U. that has EG Monitor as source
            for CUEGM,CU,CI in C.db.session.query(Charge_Unit_EGM,Charge_Units,Configuration_Items).join(Charge_Units).join(Configuration_Items).all(): # Generates records for EGM CU's
                C.logger.debug("%s: EGM CU=%s  . Will check data for %s"%(__name__,CUEGM,today))
                C.logger.debug("%s:     CU=%s"%(__name__,CU))
                C.logger.debug("%s:     CI=%s"%(__name__,CI))
                # -----------------
                timefrom=datetime.strftime(datetime.now(),"%Y%m%d")
                until=datetime.fromtimestamp(datetime.timestamp(datetime.now())+(24*3600))
                timeuntil=datetime.strftime(until,"%Y%m%d")
                URL="http://%s/graphite/render?target=%s&format=json&from=%s&until=%s"%(CUEGM.Host,CUEGM.Metric,timefrom,timeuntil)
                # Disable warnings
                # This code is required for insecure connections (without proper host certificate)
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                # Creates URL Request Session Environment
                session         = requests.Session()
                session.verify  = False
                #if True:
                try:    # Will try to connect to server
                    serverResponse = session.get(URL,timeout=(float(5),float(10)))
                    if serverResponse.status_code == 200:   # Successfull Request
                        data=json.loads(serverResponse.text)
                        # consolidates will save MAX aggregation per hour slice
                        Aggregates=Graphite_Aggregate(data[0]['datapoints'],MAXIMUM)
                        count_created=count_updated=0
                        for datapoint in Aggregates:
                            slicetimestamp,value=datapoint
                            # update CIT Records in Collector's DB
                            DATETIME=datetime.strftime(datetime.fromtimestamp(slicetimestamp),"%Y-%m-%d %H:%M:%S")
                            created,updated=C.db.Record_Item(
                                    CU.Typ_Code,
                                    CI.CI_UUID,
                                    CU.CU_UUID,
                                    value,
                                    DATETIME,
                                    True)
                            if created: 
                                count_created  += 1
                                count_modified += 1
                            if updated: 
                                count_updated  += 1
                                count_modified += 1
                        C.logger.debug("%s: Created %s / updated %s records out of %s"%(__name__,count_created,count_updated,len(Aggregates)))
                    else:
                        C.logger.warning("%s: invalid response from server: %s"%(__name__,serverResponse))        
                except ConnectionError:
                    C.logger.error("%s: Connection error trying to GET URL=%s"     %(__name__,URL))            
                except ConnectTimeout:
                    C.logger.error("%s: Connection Timeout trying to GET from URL=%s"     %(__name__,URL))            
                except Exception as e:
                    emtec_handle_general_exception(e,logger=C.logger,module=__name__,function='EG_Monitor_Collector')
            if count_modified > 0:
                C.logger.info("%s: Generated/Modified %d EGM Charge Items."%(__name__,count_modified))                
        else:
            C.logger.info("%s: Collector Inactive."%(__name__))        
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,ini_file))
    C.logger.info("%s: EG Monitor Collector: Completed"%(__name__))
