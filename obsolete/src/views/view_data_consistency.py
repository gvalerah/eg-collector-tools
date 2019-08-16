# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================


# Support Constants, Variables & Functions
RAT_TYPE        =0x01
RAT_PLATFORM    =0x02
RAT_CUSTOMER    =0x04
RAT_CC          =0x08
RAT_CU          =0x10

Valid_Rat_Types = [   RAT_TYPE,
                RAT_TYPE|RAT_PLATFORM,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC|RAT_CU
                ]

def Get_Rat_Type(Rate):
    rate_type = 0x00
    if Rate.Typ_Code != 'NUL'   :   rate_type |= RAT_TYPE    
    if Rate.Pla_Id != 1         :   rate_type |= RAT_PLATFORM
    if Rate.Cus_Id != 1         :   rate_type |= RAT_CUSTOMER
    if Rate.CC_Id  != 1         :   rate_type |= RAT_CC
    if Rate.CU_Id  != 1         :   rate_type |= CU
    return rate_type

def is_valid_rate(Rate):
    return Rate in Valid_Rat_Types
    

def Update_Rates_Type():
    #for t in Valid_Rat_Types:
    #    #print("Valid Rat Type ",t)
    
    rate_rows=rate.query.all()
    for rat in rate_rows:
        #print(rat,Get_Rat_Type(rat),is_valid_rate(Get_Rat_Type(rat)))
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
    
    """
    query = "SELECT * FROM Configuration_Items "\
                "JOIN Customers         USING (Cus_Id) "\
                "JOIN Platforms         USING (Pla_Id) "\
                "JOIN Cost_Centers      ON (Configuration_Items.CC_Id=Cost_Centers.CC_Id) "\
                "JOIN CIT_Generations   USING (CIT_Generation) "\
                "WHERE Configuration_Items.CC_Id = Customers.CC_Id "\
                "OR Configuration_Items.CC_Id = 1"
                
    ci_rows=db.engine.execute(query).fetchall()
    """
    ci_rows=configuration_item.query\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(cost_center,cost_center.CC_Id==configuration_item.CC_Id)  .add_column(cost_center.CC_Description)\
                .join(cit_generation)                                           .add_column(cit_generation.Value)\
                .filter(or_(    configuration_item.CC_Id==customer.CC_Id\
                                ,configuration_item.CC_Id==1))\
                .all()
                
                
    data.update({'ci_rows': ci_rows})
    
    Update_Rates_Type()
    
    rate_rows=rate.query\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(cost_center,cost_center.CC_Id==rate.CC_Id)                .add_column(cost_center.CC_Description)\
                .join(charge_unit)                                              .add_column(charge_unit.CU_Description)\
                .order_by(rate.Pla_Id,rate.Cus_Id,rate.CC_Id,rate.CU_Id,rate.Typ_Code)\
                .all()
    
    data.update({'rate_rows': rate_rows})

    
    return render_template('report_data_consistency.html',data=data,is_valid_rate=is_valid_rate)

# =============================================================================


