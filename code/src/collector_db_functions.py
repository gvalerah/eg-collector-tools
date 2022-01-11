""" Collector DB Suport an "Storage Procedures" Functions """

""" Imports """
from models import *

# GV Non DB Functions

def Convert_Unit(Q,Operation):
    if      Operation == 'NONE':    return Q
    elif  Operation == 'BTOKB':   return Q/1024
    elif  Operation == 'BTOMB':   return Q/1024/1024
    elif  Operation == 'BTOGB':   return Q/1024/1024/1024
    elif  Operation == 'KBTOB':   return Q*1024
    elif  Operation == 'KBTOMB':  return Q/1024
    elif  Operation == 'KBTOGB':  return Q/1024/1024
    elif  Operation == 'MBTOB':   return Q*1024*1024
    elif  Operation == 'MBTOKB':  return Q*1024
    elif  Operation == 'MBTOGB':  return Q/1024
    elif  Operation == 'GBTOB':   return Q*1024*1024*1024
    elif  Operation == 'GBTOKB':  return Q*1024*1024
    elif  Operation == 'GBTOMB':  return Q*1024
    elif  Operation == 'HTOD':    return Q/24
    elif  Operation == 'HTOM':    return Q/24/30
    elif  Operation == 'DTOH':    return Q*24
    elif  Operation == 'DTOM':    return Q/30
    elif  Operation == 'MTOH':    return Q*24*30
    elif  Operation == 'MTOD':    return Q*24
    
    
def Get_CU_Id_From_UUID(CU_UUID,CI_ID,CU_TYPE):    
    CU_Id = charge_unit.query(CU_Id).filter(CU_UUID=CU_UUID,CI_Id=CI_ID,Typ_Code=CU_TYPE).limit(1)
    return CU_Id     
     
def Create_Charge_Unit(CI_ID=None, DESCRIPTION="", CU_UUID=None, ISBILLEABLE=True, ISALLWAYS=True, QUANTITY=None, OPERATION="NONE", CU_TYPE=None, CC_ID=1, CIT_GENERATION=1, REF1=None, REF2=None, REF3=None):
    
    
    # GV Checks for CU existence
    CU_ID = Get_CU_Id_From_UUID(CU_UUID,CI_ID,CU_TYPE);

    # GV If CU does not exist then creates it
    if CU_ID is None:
            try:
                CU=charge_unit(     CI_Id           = CI_ID,\
                                    CU_Description  = DESCRIPTION,\
                                    CU_UUID         = CU_UUID,\
                                    CU_Is_Billeable = ISBILLEABLE,\
                                    CU_Is_Allways   = ISALLWAYS,\
                                    CU_Quantity     = QUANTITY,\
                                    CU_Operation    = OPERATION,\
                                    Typ_Code        = CU_TYPE,\
                                    CC_Id           = CC_ID,\
                                    CIT_Generation  = CIT_GENERATION,\
                                    CU_Reference_1  = REF1,\
                                    CU_Reference_2  = REF2,\
                                    CU_Reference_3  = REF3\
                              )
                db.session.add(CU)
                db.session.commit()
                CU_ID = CU.CU_Id
            except:
                print("No se pudo crear CU reportar")
    return CU_ID
    
    
