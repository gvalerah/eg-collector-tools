
query="""
SELECT
    `Configuration_Items`.`Cus_Id` AS `Cus_Id`, 
    '2020-03-01' AS `CR_Date_From`, 
    '2020-03-31' AS `CR_Date_To`, 
    `Charge_Items_202003`.`CIT_Status` AS `CIT_Status`, 
    `Cost_Centers`.`Cur_Code` AS `Cur_Code`, 
    count(*) AS `CIT_Count`, 
    sum(`Charge_Items_202003`.`CIT_Quantity`) 
    AS `CIT_Quantity`, 
    `Charge_Units`.`CIT_Generation` AS `CIT_Generation`, 
    `Charge_Units`.`CU_Id` AS `CU_Id`, 
    `Configuration_Items`.`CC_Id` AS `CI_CC_Id`, 
    `Charge_Units`.`CU_Operation` AS `CU_Operation`, 
    `Charge_Units`.`Typ_Code` AS `Typ_Code`, 
    `Cost_Centers`.`Cur_Code` AS `CC_Cur_Code`, 
    `Configuration_Items`.`CI_Id` AS `CI_Id`, 
    `Rates`.`Rat_Id` AS `Rat_Id`, 
    `Rates`.`Rat_Price` AS `Rat_Price`, 
    `Rates`.`MU_Code` AS `Rat_MU_Code`, 
    `Rates`.`Cur_Code` AS `Rat_Cur_Code`, 
    `Rates`.`Rat_Period` AS `Rat_Period`, 
    0 AS `Rat_Hourly`, 
    0 AS `Rat_Daily`, 
    0 AS `Rat_Monthly`, 
    0 AS `CR_Quantity`, 
    0 AS `CR_Quantity_at_Rate`, 
    1 AS `CC_XR`, 
    1 AS `CR_Cur_XR`, 
    0 AS `CR_ST_at_Rate_Cur`, 
    0 AS `CR_ST_at_CC_Cur`, 
    0 AS `CR_ST_at_Cur`, 
    `Customers`.`Cus_Name` AS `Cus_Name`, 
    `Cost_Centers`.`CC_Description` AS `CC_Description`, 
    `Configuration_Items`.`CI_Name` AS `CI_Name`, 
    `Charge_Units`.`CU_Description` AS `CU_Description`, 
    NULL AS `Rat_Period_Description`, 
    `Configuration_Items`.`Pla_Id` AS `Pla_Id`, 
    `Platforms`.`Pla_Name` AS `Pla_Name`
FROM
    `Charge_Items_202003` 
        INNER JOIN `Charge_Units` ON `Charge_Units`.`CU_Id` = `Charge_Items_202003`.`CU_Id` 
        INNER JOIN `Configuration_Items` ON `Configuration_Items`.`CI_Id` = `Charge_Units`.`CI_Id` 
        INNER JOIN `Cost_Centers` ON `Cost_Centers`.`CC_Id` = `Configuration_Items`.`CC_Id` 
        INNER JOIN `Customers` ON `Customers`.`Cus_Id` = `Configuration_Items`.`Cus_Id` 
        INNER JOIN `Platforms` ON `Platforms`.`Pla_Id` = `Configuration_Items`.`Pla_Id` 
        INNER JOIN `Rates` ON `Rates`.`Rat_Id` = `Charge_Units`.`Rat_Id`
WHERE 
    `Charge_Items_202003`.`CIT_Status` = %(CIT_Status_1)s AND 
    `Charge_Items_202003`.`CIT_DateTime` >= "%(CIT_DateTime_1)s" AND 
    `Charge_Items_202003`.`CIT_DateTime` <= "%(CIT_DateTime_2)s" AND 
    `Configuration_Items`.`Cus_Id` = %(Cus_Id_1)s AND 
    `Charge_Units`.`CI_Id` = %(CI_Id_1)s
GROUP BY 
    `Charge_Items_202003`.`CU_Id` 
ORDER BY 
    `Configuration_Items`.`Cus_Id`, 
    `Configuration_Items`.`CC_Id`, 
    `Configuration_Items`.`CI_Id`, 
    `Charge_Items_202003`.`CU_Id`
    """
data={
    "CIT_Status_1":1,
    "CIT_DateTime_1":"2020-03-01",
    "CIT_DateTime_2":"2020-03-31",
    "Cus_Id_1":2,
    "CI_Id_1":2879
    }

print(query%data)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
cs="mysql+pymysql://collector:Password1$@localhost:3306/collector"
engine=create_engine(cs)
Session=sessionmaker(bind=engine)
session=Session()
rows=session.execute(query%data)
#print(dir(rows))
print("rowcount=",rows.rowcount)
print(rows)
if rows is not None:
    #print("got %d rows"%len(rows))
    for row in rows:
        print(row)
else:
    print("rows=",rows)
