DROP TABLE IF EXISTS NEW_CIT;

CREATE TABLE NEW_CIT
SELECT
    CU_Id,
    "2020-03-31" AS CIT_Date,
    "23:00:00" AS CIT_Time,
    RAND()*CU_Quantity as CIT_Quantity,
    1 AS CIT_Status,
    1 AS CIT_Is_Active,
    "2020-03-31 23:00:00 " AS CIT_DateTime
FROM Charge_Units WHERE Typ_Code="DSU";

