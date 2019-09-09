# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018,2019
# GLVH @ 2019-03-11
# =============================================================================


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
    logger.debug('Enter: reports_Data_Consistency()'%())

    # Prepare query
    version  = db.engine.execute("SELECT VERSION()").fetchall()
    hostname = db.engine.execute("SELECT @@HOSTNAME").fetchall()
    data={}
    data.update({'version': version[0][0]})
    data.update({'hostname': hostname[0][0]})
    
    ci_rows=db.session.query(configuration_item)\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(cost_center,cost_center.CC_Id==configuration_item.CC_Id)  .add_column(cost_center.CC_Description)\
                .filter(or_(    configuration_item.CC_Id==customer.CC_Id\
                                ,configuration_item.CC_Id==1))\
                .all()
                
    data.update({'ci_rows': ci_rows})
    
    # Updates Rate Types in Rates Table in order to validate them in report
    Update_Rates_Type()
    
    """
    query=db.session.query(rate)\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(configuration_item)                                       .add_column(configuration_item.CI_Name)\
                .join(cost_center,cost_center.CC_Id==rate.CC_Id)                .add_column(cost_center.CC_Description)\
                .order_by(rate.Pla_Id,rate.Cus_Id,rate.CC_Id,rate.CI_Id,rate.Typ_Code)
    
    flash(query)
    """
    """
    rate_rows=None
    rate_rows=db.session.query(rate)\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(configuration_item)                                       .add_column(configuration_item.CI_Name)\
                .join(cost_center,cost_center.CC_Id==rate.CC_Id)                .add_column(cost_center.CC_Description)\
                .order_by(rate.Pla_Id,rate.Cus_Id,rate.CC_Id,rate.CI_Id,rate.Typ_Code)\
                .all()
    """
    """
    query = "SELECT * "\
                "FROM Rates "\
                    "JOIN Customers             USING   (Cus_Id) "\
                    "JOIN Platforms             USING   (Pla_Id) "\
                    "JOIN Configuration_Items   USING   (CI_Id) "\
                    "JOIN Cost_Centers          ON      Cost_Centers.CC_Id=Rates.CC_id "\
                "ORDER BY Typ_Code,Rates.Pla_Id,Rates.Cus_Id,Rates.CC_Id,Rates.CI_Id"
    """
    # GV 20190907
    query = db.query(Rates,Customers,Platforms,Configuration_Items,Cost_Centes).\
                join(Customers          , Rates.Cus_Id == Customers.Cus_Id).\
                join(Platforms          , Rates.Pla_Id == Platforms.Pla_Id).\
                join(Configuration_Items, Rates.CI_Id  == Configuration_Items.CI_Id).\
                join(Cost_Centers       , Rates.CC_Id  == Cost_Centers.CC_Id).\
                order_by(   Rates.Typ_Code,
                            Rates.Pla_Id,
                            Rates.Cus_Id,
                            Rates.CC_Id,
                            Rates.CI_Id)
                 
    rate_rows=[]

    try:
        rate_rows = db.session.execute(query).fetchall()
    except Exception as e:
        print("**************************************")
        print(e)
        print("**************************************")

    data.update({'rate_rows': rate_rows})

    """ GV 20190907 AQUI AUN HAY QUE CONSTRUIR UN ALGORITMO EQUIVALENTE
    query = "SELECT CU_Id,CU_Description,Typ_Code,Pla_Id,Cus_Id,CI.CC_Id AS CC_ID,Rat_Id,"\
                    "Get_Rate_Id (Typ_Code,Pla_Id,Cus_Id,CI.CC_Id,CU_Id) AS RATE, "\
                    "Pla_Name,Cus_Name,CC_Description,CI_Name "\
                "FROM Charge_Units AS CU "\
                    "JOIN Configuration_Items AS CI  USING (CI_Id) "\
                    "JOIN Platforms           AS PLA USING (Pla_Id) "\
                    "JOIN Customers           AS CUS USING (Cus_Id) "\
                    "JOIN Cost_Centers        AS CC  ON CC.CC_Id = CI.CC_Id "\
                "WHERE Rat_Id != Get_Rate_Id(Typ_Code,Pla_Id,Cus_Id,CI.CC_Id,CU_Id)"
    """

    cu_rows = []
    
    try:
        cu_rows = db.session.execute(query).fetchall()
    except Exception as e:
        print("**************************************")
        print(e)
        print("**************************************")

    data.update({'cu_rows': cu_rows})

    return render_template('report_data_consistency.html',data=data,is_valid_rate=is_valid_rate)

# =============================================================================


