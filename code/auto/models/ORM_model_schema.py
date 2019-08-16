# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from sqlalchemy                 import Table, Column, MetaData, ForeignKey
from sqlalchemy                 import Integer, String, Date, Time, Numeric, DateTime, Boolean

Meta = MetaData()

def Create_Tables(engine):
    try:
        CIT_Generations = Table(
                'CIT_Generations',Meta,
                Column( 'CIT_Generation',Integer, primary_key=True ),
                Column( 'Value',String(45) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        CIT_Statuses = Table(
                'CIT_Statuses',Meta,
                Column( 'CIT_Status',Integer, primary_key=True ),
                Column( 'Value',String(45) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        CU_Operations = Table(
                'CU_Operations',Meta,
                Column( 'CU_Operation',String(10), primary_key=True ),
                Column( 'Value',String(45) ),
                Column( 'Is_Multiply',Boolean ),
                Column( 'Factor',Integer ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        CU_Types = Table(
                'CU_Types',Meta,
                Column( 'Typ_Code',String(10), primary_key=True ),
                Column( 'Typ_Description',String(45) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Charge_Items = Table(
                'Charge_Items',Meta,
                Column( 'CU_Id',Integer, ForeignKey('Charge_Units.CU_Id'), primary_key=True ),
                Column( 'CIT_Date',Date ),
                Column( 'CIT_Time',Time ),
                Column( 'CIT_Quantity',Numeric(20,6) ),
                Column( 'CIT_Status',Integer, ForeignKey('CIT_Statuses.CIT_Status') ),
                Column( 'CIT_Is_Active',Boolean ),
                Column( 'CIT_DateTime',DateTime, primary_key=True ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Charge_Resumes = Table(
                'Charge_Resumes',Meta,
                Column( 'Cus_Id',Integer, primary_key=True ),
                Column( 'CR_Date_From',Date, primary_key=True ),
                Column( 'CR_Date_To',Date, primary_key=True ),
                Column( 'CIT_Status',Integer, primary_key=True ),
                Column( 'Cur_Code',String(3), primary_key=True ),
                Column( 'CIT_Count',Integer ),
                Column( 'CIT_Quantity',Numeric(20,6) ),
                Column( 'CIT_Generation',Integer ),
                Column( 'CU_Id',Integer, primary_key=True ),
                Column( 'CI_CC_Id',Integer ),
                Column( 'CU_Operation',String(10) ),
                Column( 'Typ_Code',String(10) ),
                Column( 'CC_Cur_Code',String(3) ),
                Column( 'CI_Id',Integer ),
                Column( 'Rat_Id',Integer ),
                Column( 'Rat_Price',Numeric(20,6) ),
                Column( 'Rat_MU_Code',String(3) ),
                Column( 'Rat_Cur_Code',String(3) ),
                Column( 'Rat_Period',Integer ),
                Column( 'Rat_Hourly',Numeric(20,6) ),
                Column( 'Rat_Daily',Numeric(20,6) ),
                Column( 'Rat_Monthly',Numeric(20,6) ),
                Column( 'CR_Quantity',Numeric(20,6) ),
                Column( 'CR_Quantity_at_Rate',Numeric(20,6) ),
                Column( 'CC_XR',Numeric(20,10) ),
                Column( 'CR_Cur_XR',Numeric(20,10) ),
                Column( 'CR_ST_at_Rate_Cur',Numeric(20,6) ),
                Column( 'CR_ST_at_CC_Cur',Numeric(20,6) ),
                Column( 'CR_ST_at_Cur',Numeric(20,6) ),
                Column( 'Cus_Name',String(45) ),
                Column( 'CI_Name',String(45) ),
                Column( 'CU_Description',String(45) ),
                Column( 'CC_Description',String(45) ),
                Column( 'Rat_Period_Description',String(10) ),
                Column( 'Pla_Id',Integer ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Charge_Units = Table(
                'Charge_Units',Meta,
                Column( 'CU_Id',Integer, primary_key=True, autoincrement=True ),
                Column( 'CI_Id',Integer, ForeignKey('Configuration_Items.CI_Id') ),
                Column( 'CU_Description',String(45) ),
                Column( 'CU_UUID',String(45) ),
                Column( 'CU_Is_Billeable',Boolean ),
                Column( 'CU_Is_Always_Billeable',Boolean ),
                Column( 'CU_Quantity',Numeric(20,6) ),
                Column( 'CU_Operation',String(10), ForeignKey('CU_Operations.CU_Operation') ),
                Column( 'Typ_Code',String(10), ForeignKey('CU_Types.Typ_Code') ),
                Column( 'CIT_Generation',Integer, ForeignKey('CIT_Generations.CIT_Generation') ),
                Column( 'Rat_Id',Integer ),
                Column( 'CU_Reference_1',String(45) ),
                Column( 'CU_Reference_2',String(45) ),
                Column( 'CU_Reference_3',String(45) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Configuration_Items = Table(
                'Configuration_Items',Meta,
                Column( 'CI_Id',Integer, primary_key=True, autoincrement=True ),
                Column( 'CI_Name',String(45) ),
                Column( 'CI_UUID',String(45) ),
                Column( 'Pla_Id',Integer, ForeignKey('Platforms.Pla_Id') ),
                Column( 'CC_Id',Integer, ForeignKey('Cost_Centers.CC_Id') ),
                Column( 'Cus_Id',Integer, ForeignKey('Customers.Cus_Id') ),
                Column( 'CI_Commissioning_DateTime',DateTime ),
                Column( 'CI_Decommissioning_DateTime',DateTime ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Cost_Centers = Table(
                'Cost_Centers',Meta,
                Column( 'CC_Id',Integer, primary_key=True, autoincrement=True ),
                Column( 'CC_Code',String(45) ),
                Column( 'CC_Description',String(45) ),
                Column( 'Cur_Code',String(3), ForeignKey('Currencies.Cur_Code') ),
                Column( 'CC_Parent_Code',String(45) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Countries = Table(
                'Countries',Meta,
                Column( 'Cou_Code',String(2), primary_key=True ),
                Column( 'Cou_Name',String(45) ),
                Column( 'Cou_A3',String(3) ),
                Column( 'Cou_N',Integer ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Countries_Currencies = Table(
                'Countries_Currencies',Meta,
                Column( 'Cou_Code',String(2), ForeignKey('Countries.Cou_Code'), primary_key=True ),
                Column( 'Cur_Code',String(3), ForeignKey('Currencies.Cur_Code'), primary_key=True ),
                Column( 'Cou_Cur_Comment',String(45) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Currencies = Table(
                'Currencies',Meta,
                Column( 'Cur_Code',String(3), primary_key=True ),
                Column( 'Cur_Name',String(45) ),
                Column( 'Cur_Id',Integer ),
                Column( 'Cur_Comment',String(128) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Customers = Table(
                'Customers',Meta,
                Column( 'Cus_Id',Integer, primary_key=True, autoincrement=True ),
                Column( 'Cus_Name',String(45) ),
                Column( 'CC_Id',Integer, ForeignKey('Cost_Centers.CC_Id') ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Dev_Forms = Table(
                'Dev_Forms',Meta,
                Column( 'Id',Integer, primary_key=True, autoincrement=True ),
                Column( 'Table',String(45) ),
                Column( 'Field',String(45) ),
                Column( 'Type',String(45) ),
                Column( 'Null',String(45) ),
                Column( 'Key',String(45) ),
                Column( 'Default',String(45) ),
                Column( 'Extra',String(45) ),
                Column( 'Foreign_Key',String(45) ),
                Column( 'Referenced_Table',String(45) ),
                Column( 'Foreign_Field',String(45) ),
                Column( 'Foreign_Value',String(45) ),
                Column( 'Length',Integer ),
                Column( 'Validation',Boolean ),
                Column( 'Validation_Type',String(45) ),
                Column( 'Validation_String',String(128) ),
                Column( 'Caption_String',String(45) ),
                Column( 'Field_Order',Integer ),
                Column( 'Field_Format',String(45) ),
                Column( 'Form_Editable',Boolean ),
                Column( 'ORM_Schema',Boolean ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Dev_Tables = Table(
                'Dev_Tables',Meta,
                Column( 'Id',Integer, primary_key=True, autoincrement=True ),
                Column( 'Name',String(45) ),
                Column( 'Caption',String(45) ),
                Column( 'Entity',String(45) ),
                Column( 'Class_Name',String(45) ),
                Column( 'Child_Table',String(45) ),
                Column( 'Parent_Table',String(45) ),
                Column( 'Use_Pagination',Boolean ),
                Column( 'Use_Children_Pagination',Boolean ),
                Column( 'Generate_Form_One',Boolean ),
                Column( 'Generate_Form_All',Boolean ),
                Column( 'Generate_Form_Filter',Boolean ),
                Column( 'Generate_Children',Boolean ),
                Column( 'Generate_Foreign_Fields',Boolean ),
                Column( 'Permission_View',Boolean ),
                Column( 'Permission_Delete',Boolean ),
                Column( 'Permission_Modify',Boolean ),
                Column( 'Permission_Report',Boolean ),
                Column( 'Permission_Export',Boolean ),
                Column( 'Permission_View_Private',Boolean ),
                Column( 'Permission_Modify_Private',Boolean ),
                Column( 'Permission_Administer',Boolean ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Exchange_Rates = Table(
                'Exchange_Rates',Meta,
                Column( 'ER_Id',Integer, primary_key=True, autoincrement=True ),
                Column( 'Cur_Code',String(3), ForeignKey('Currencies.Cur_Code') ),
                Column( 'ER_Factor',Numeric(20,10) ),
                Column( 'ER_Date',Date ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Measure_Units = Table(
                'Measure_Units',Meta,
                Column( 'MU_Code',String(3), primary_key=True ),
                Column( 'MU_Description',String(45) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Platforms = Table(
                'Platforms',Meta,
                Column( 'Pla_Id',Integer, primary_key=True, autoincrement=True ),
                Column( 'Pla_Name',String(45) ),
                Column( 'Pla_Host',String(45) ),
                Column( 'Pla_Port',String(45) ),
                Column( 'Pla_User',String(45) ),
                Column( 'Pla_Password',String(45) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Rat_Periods = Table(
                'Rat_Periods',Meta,
                Column( 'Rat_Period',Integer, primary_key=True ),
                Column( 'Value',String(45) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Rates = Table(
                'Rates',Meta,
                Column( 'Rat_Id',Integer, primary_key=True, autoincrement=True ),
                Column( 'Typ_Code',String(10), ForeignKey('CU_Types.Typ_Code') ),
                Column( 'Cus_Id',Integer, ForeignKey('Customers.Cus_Id') ),
                Column( 'Pla_Id',Integer, ForeignKey('Platforms.Pla_Id') ),
                Column( 'CC_Id',Integer, ForeignKey('Cost_Centers.CC_Id') ),
                Column( 'CI_Id',Integer, ForeignKey('Configuration_Items.CI_Id') ),
                Column( 'Rat_Price',Numeric(20,6) ),
                Column( 'Cur_Code',String(3), ForeignKey('Currencies.Cur_Code') ),
                Column( 'MU_Code',String(3), ForeignKey('Measure_Units.MU_Code') ),
                Column( 'Rat_Period',Integer, ForeignKey('Rat_Periods.Rat_Period') ),
                Column( 'Rat_Type',Integer ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Roles = Table(
                'Roles',Meta,
                Column( 'id',Integer, primary_key=True ),
                Column( 'name',String(64) ),
                Column( 'default',Boolean ),
                Column( 'permissions',Integer ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        ST_Use_Per_CU = Table(
                'ST_Use_Per_CU',Meta,
                Column( 'CU_Id',Integer, primary_key=True ),
                Column( 'From',DateTime, primary_key=True ),
                Column( 'To',DateTime, primary_key=True ),
                Column( 'Total_Slices',Integer ),
                Column( 'Found_Slices',Integer ),
                Column( 'Not_Found_Slices',Integer ),
                Column( 'Period_Initial_Q',Numeric(20,6) ),
                Column( 'Period_Increase',Numeric(20,6) ),
                Column( 'Period_Increase_Count',Integer ),
                Column( 'Period_Reduction',Numeric(20,6) ),
                Column( 'Period_Reduction_Count',Integer ),
                Column( 'Period_Final_Q',Numeric(20,6) ),
                Column( 'CI_Id',Integer ),
                Column( 'CC_Id',Integer ),
                Column( 'Cus_Id',Integer ),
                Column( 'Rat_Id',Integer ),
                Column( 'Typ_Code',String(10) ),
                Column( 'Pla_Id',Integer ),
                Column( 'Mean',Numeric(20,6) ),
                Column( 'Variance',Numeric(20,6) ),
                Column( 'StdDev',Numeric(20,6) ),
                Column( 'Min',Numeric(20,6) ),
                Column( 'Max',Numeric(20,6) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        ST_Use_Per_Type = Table(
                'ST_Use_Per_Type',Meta,
                Column( 'Typ_Code',String(10), primary_key=True ),
                Column( 'Cus_Id',Integer, primary_key=True ),
                Column( 'Pla_Id',Integer, primary_key=True ),
                Column( 'CC_Id',Integer, primary_key=True ),
                Column( 'CI_Id',Integer, primary_key=True ),
                Column( 'Year',Integer, primary_key=True ),
                Column( 'Month',Integer, primary_key=True ),
                Column( 'Count',Integer ),
                Column( 'Mean',Numeric(20,6) ),
                Column( 'Variance',Numeric(20,6) ),
                Column( 'StdDev',Numeric(20,6) ),
                Column( 'Min',Numeric(20,6) ),
                Column( 'Max',Numeric(20,6) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Trace = Table(
                'Trace',Meta,
                Column( 'ID',Integer, primary_key=True, autoincrement=True ),
                Column( 'LINE',String(128) ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Users = Table(
                'Users',Meta,
                Column( 'id',Integer, primary_key=True, autoincrement=True ),
                Column( 'username',String(64) ),
                Column( 'role_id',Integer, ForeignKey('Roles.id') ),
                Column( 'email',String(64) ),
                Column( 'password_hash',String(128) ),
                Column( 'confirmed',Boolean ),
                Column( 'CC_Id',Integer, ForeignKey('Cost_Centers.CC_Id') ),
        )
    except Exception as e:
        print('EXCEPTION:',e)
    try:
        Meta.create_all(engine)
    except Exception as e:
        print("EXCEPTION: on Meta.create_all(engine=%s)"%engine,e,"!!!!")

# Required for Load_Table Function
import  pandas      as      pandas
from    pathlib     import  Path
# imports orm_model as local definitions for DB popuplation
import  emtec.collector.orm_models   as      orm_model
       
def Load_Table(self,class_name,filename,separator=','):
    my_file = Path(filename)
    if my_file.is_file():
        # file exists
        # Gets type of recodr class by name
        table_class=getattr(orm_model,class_name)
        # reads data from CSV (separator can be specified to change format
        # if needed, no default NaN values will be used
        df=pandas.read_csv(filename,sep=separator,keep_default_na=False)
        # iterate over rows with iterrows()
        for index, row in df.iterrows():
            instance=table_class()
            # access data using column names
            for column in list(df.columns.values):
                value = None if pandas.isnull(row[column]) else row[column]
                setattr(instance, column, value)
                try:
                    self.session.add(instance)
                except Exception as e:
                    print("Load_table: Could not add instance of %s: %s %s"%(instance,class_name,e))
                    return False
        try:
            self.session.commit()
        except Exception as e:
            #print("Load_table: Could not commit session: %s %s"%(self.session,e))
            print("Load_table: Could not commit session: %s %s"%(self.session,'e'))
            self.session.rollback()
            return False
        return True
    else:
        return False

