from emtec.collector.db.orm import *
from emtec.collector.db.orm_model import *

db=Collector_ORM_DB(
    rdbms='mysql',
    dialect='pymysql',
    host='localhost',
    port=3306,
    user='collector',
    password='Password1$',
    instance='collector')
print("db=",db)

def test_Update_Charge_Resume_CI(
                Cus_Id,
                Date_From,
                Date_To,
                Status,
                Cur_Code,
                CI_Id,
                Charge_Items):
            records = db.Update_Charge_Resume_CI(
                Cus_Id,
                Date_From,
                Date_To,
                Status,
                Cur_Code,
                CI_Id,
                Charge_Items)
            print("test_Update_Charge_Resume_CI(): records="%(
                records))
            return records

if __name__ == '__main__':
    Cus_Id=2
    Date_From="2020-03-01"
    Date_To="2020-03-31"
    Status=1
    Cur_Code="USD"
    CI_Id=2879
    test_Update_Charge_Resume_CI(
        Cus_Id,
        Date_From,
        Date_To,
        Status,
        Cur_Code,
        CI_Id,
        Charge_Items
        )
    for record in records:
        print(record)
