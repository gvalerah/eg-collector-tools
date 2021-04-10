# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018,2019
# GLVH @ 2019-03-11
# =============================================================================

from pprint import pprint
from emtec.collector.db.orm_model import *

# Support Constants, Variables & Functions
RAT_TYPE        =0x01
RAT_PLATFORM    =0x02
RAT_CUSTOMER    =0x04
RAT_CC          =0x08
RAT_CI          =0x10

Valid_Rat_Types = [     RAT_TYPE,
                        RAT_TYPE|RAT_PLATFORM,
                        RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER,
                        RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC,
                        RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC|RAT_CI
                ]

def Get_Rat_Type(Rate):
    rate_type           =  0x00
    if Rate.Typ_Code    != 'NUL'   :   rate_type |= RAT_TYPE    
    if Rate.Pla_Id      != 1         :   rate_type |= RAT_PLATFORM
    if Rate.Cus_Id      != 1         :   rate_type |= RAT_CUSTOMER
    if Rate.CC_Id       != 1         :   rate_type |= RAT_CC
    if Rate.CI_Id       != 1         :   rate_type |= RAT_CI
    return rate_type

def is_valid_rate(Rate):
    return Rate in Valid_Rat_Types
    

def Update_Rates_Type():
    
    rate_rows=rate.query.all()
    for rat in rate_rows:
        rat.Rat_Type=Get_Rat_Type(rat)
        db.session.add(rat)
        db.session.commit()

from babel.numbers  import format_number, format_decimal, format_percent
from sqlalchemy.sql.expression import or_

@main.route('/reports/Data_Consistency', methods=['GET'])
@login_required
def reports_Data_Consistency():
    logger.debug('Enter: reports_Data_Consistency()')

    # Prepare query This working for MySQL Engine Only
    version  = db.engine.execute("SELECT VERSION()").fetchall()
    hostname = db.engine.execute("SELECT @@HOSTNAME").fetchall()
    data={}
    data.update({'version': version[0][0]})
    data.update({'hostname': hostname[0][0]})
    
    # ------------------------------------------------------------------
    ci_rows=db.session.query(Configuration_Items
                ).join(Customers
                    ).add_column(Customers.Cus_Name
                ).join(Platforms
                    ).add_column(Platforms.Pla_Name
                ).join(Cost_Centers,
                    Cost_Centers.CC_Id==Configuration_Items.CC_Id
                    ).add_column(Cost_Centers.CC_Description
                ).filter(or_(
                            Configuration_Items.CC_Id==Customers.CC_Id,
                            Configuration_Items.CC_Id==1
                            )
                ).all()
                
    data.update({'ci_rows': ci_rows})
    
    # ------------------------------------------------------------------
    # Updates Rate Types in Rates Table in order to validate them in report
    Update_Rates_Type()
        
    query = db.session.query(
                Rates,
                Customers,
                Platforms,
                Configuration_Items,
                Cost_Centers
                ).join(Customers, 
                    Rates.Cus_Id == Customers.Cus_Id
                ).join(Platforms, 
                    Rates.Pla_Id == Platforms.Pla_Id
                ).join(Configuration_Items, 
                    Rates.CI_Id  == Configuration_Items.CI_Id
                ).join(Cost_Centers, 
                    Rates.CC_Id  == Cost_Centers.CC_Id
                ).order_by(
                    Rates.Typ_Code,
                    Rates.Pla_Id,
                    Rates.Cus_Id,
                    Rates.CC_Id,
                    Rates.CI_Id
                )
    rate_rows=[]

    try:
        rate_rows = query.all()
    except Exception as e:
        print("**************************************")
        print(e)
        print("**************************************")

    data.update({'rate_rows': rate_rows})
    # ------------------------------------------------------------------
    query = db.session.query(   Charge_Units,
                                Configuration_Items,
                                Platforms,
                                Customers,
                                Cost_Centers
                ).join(Configuration_Items,
                    Charge_Units.CI_Id==Configuration_Items.CI_Id
                ).join(Platforms          ,
                    Platforms.Pla_Id==Configuration_Items.Pla_Id
                ).join(Customers          ,
                    Customers.Cus_Id==Configuration_Items.Cus_Id
                ).join(Cost_Centers       ,
                    Cost_Centers.CC_Id==Configuration_Items.CC_Id
                )
    # El filtro no esta segun lo deseado la idea es ver si el ID de la 
    # tarifa corresponde con un id valido probablemente hay que crear un
    # loop aqui para poblar la lista segun un chequeo python ya que no 
    # hay stored procedure
    
    # Por ahora solo muestra las que estan con Rate = 1 o None

    query = query.filter(or_(   Charge_Units.Rat_Id==1,
                                Charge_Units.Rat_Id==None
                            )
                        )

    rows = query.all()

    # ------------------------------------------------------------------
    cu_rows = []
    
    try:
        # Este loop es redundante por el filtro de arriba
        # se mantiene para opcion adicional
        # es muy lento si se ejecuta para todos los CUs
        # en el sistema Checkqo full de consistecia
        for row in rows:
            rate_id = db.Get_Rate_Id(
                        row.Charge_Units.Typ_Code,
                        row.Configuration_Items.Pla_Id,
                        row.Configuration_Items.Cus_Id,
                        row.Configuration_Items.CC_Id,
                        row.Charge_Units.CU_Id
                        )
            if row.Charge_Units.Rat_Id != rate_id:
                cu_rows.append([row,rate_id])
    except Exception as e:
        print("**************************************")
        print(e)
        print("**************************************")

    data.update({'cu_rows': cu_rows})

    return render_template(
        'report_data_consistency.html',
        data=data,
        is_valid_rate=is_valid_rate
        )

# ======================================================================


