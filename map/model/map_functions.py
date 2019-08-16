    """ Functions for CIT_Generations """
    """ Functions for CIT_Statuses """
    """ Functions for CU_Operations """
    """ Functions for CU_Types """
    """ Functions for Charge_Items """
    """ Functions for Charge_Resumes """
    def get_Charge_Resumes_id_from_code(code):
       id=session.query(Charge_Resumes.Rat_Id).filter(Charge_Resumes.Cur_Code==code).one_or_None()
       return id

    def get_Charge_Resumes_code_from_id(id):
       code=session.query(Charge_Resumes.Cur_Code).filter(Charge_Resumes.Rat_Id==id).one_or_None()
       return code

)    """ Functions for Charge_Units """
    def get_Charge_Units_id_from_code(code):
       id=session.query(Charge_Units.Rat_Id).filter(Charge_Units.Typ_Code==code).one_or_None()
       return id

    def get_Charge_Units_code_from_id(id):
       code=session.query(Charge_Units.Typ_Code).filter(Charge_Units.Rat_Id==id).one_or_None()
       return code

)    """ Functions for Configuration_Items """
    """ Functions for Cost_Centers """
    def get_Cost_Centers_id_from_code(code):
       id=session.query(Cost_Centers.CC_Id).filter(Cost_Centers.CC_Code==code).one_or_None()
       return id

    def get_Cost_Centers_code_from_id(id):
       code=session.query(Cost_Centers.CC_Code).filter(Cost_Centers.CC_Id==id).one_or_None()
       return code

)    """ Functions for Countries """
    """ Functions for Countries_Currencies """
    """ Functions for Currencies """
    def get_Currencies_id_from_code(code):
       id=session.query(Currencies.Cur_Id).filter(Currencies.Cur_Code==code).one_or_None()
       return id

    def get_Currencies_code_from_id(id):
       code=session.query(Currencies.Cur_Code).filter(Currencies.Cur_Id==id).one_or_None()
       return code

)    """ Functions for Customers """
    """ Functions for Dev_Forms """
    """ Functions for Dev_Tables """
    """ Functions for Exchange_Rates """
    def get_Exchange_Rates_id_from_code(code):
       id=session.query(Exchange_Rates.ER_Id).filter(Exchange_Rates.Cur_Code==code).one_or_None()
       return id

    def get_Exchange_Rates_code_from_id(id):
       code=session.query(Exchange_Rates.Cur_Code).filter(Exchange_Rates.ER_Id==id).one_or_None()
       return code

)    """ Functions for Measure_Units """
    """ Functions for Platforms """
    """ Functions for Rat_Periods """
    """ Functions for Rates """
    def get_Rates_id_from_code(code):
       id=session.query(Rates.CI_Id).filter(Rates.Typ_Code==code).one_or_None()
       return id

    def get_Rates_code_from_id(id):
       code=session.query(Rates.Typ_Code).filter(Rates.CI_Id==id).one_or_None()
       return code

)    """ Functions for Roles """
    """ Functions for Trace """
    """ Functions for User_Resumes """
    def get_User_Resumes_id_from_code(code):
       id=session.query(User_Resumes.Rat_Id).filter(User_Resumes.Cur_Code==code).one_or_None()
       return id

    def get_User_Resumes_code_from_id(id):
       code=session.query(User_Resumes.Cur_Code).filter(User_Resumes.Rat_Id==id).one_or_None()
       return code

)    """ Functions for Users """
