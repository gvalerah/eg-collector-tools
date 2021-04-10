DROP TABLE IF EXISTS NEW_CUS;

CREATE TABLE NEW_CUS SELECT 
    0                           AS CU_Id,
    Charge_Units.CI_Id          AS CI_Id,
    CONCAT(CI_Name," - DSU")    AS CU_Description,
    NULL                        AS CU_UUID,
    1                           AS CU_Is_Billeable,
    1                           AS CU_Is_AlwaysBilleable, 
    SUM(CU_Quantity)            AS CU_Quantity  , 
    "NONE"                      AS CU_Operation, 
    "DSU"                       AS Typ_Code , 
    3                           AS CIT_Generation , 
    NULL                        AS Rat_Id , 
    NULL                        AS CU_Reference_1 , 
    NULL                        AS CU_Reference_2 , 
    NULL                        AS CU_reference_3 
FROM Charge_Units     
    JOIN Configuration_Items USING(CI_ID)  
WHERE Typ_Code='DSK' 
GROUP BY Charge_Units.CI_Id;

SELECT COUNT(*) AS NEWCUS FROM NEW_CUS;

SELECT COUNT(*) AS CUS1 FROM Charge_Units;
SELECT COUNT(*) AS CIT1 FROM Charge_Items JOIN Charge_Units USING (CU_Id)  WHERE Typ_Code="DSU";


DELETE FROM Charge_Items WHERE CU_Id IN (SELECT CU_Id from Charge_Units WHERE Typ_Code="DSU");;
SELECT COUNT(*) AS CIT2 FROM Charge_Items JOIN Charge_Units USING (CU_Id)  WHERE Typ_Code="DSU";


DELETE FROM Charge_Units WHERE Typ_Code='DSU';
SELECT COUNT(*) AS CUS2 FROM Charge_Units;

INSERT INTO Charge_Units SELECT * FROM NEW_CUS;

SELECT COUNT(*) AS CUS3 FROM Charge_Units;

