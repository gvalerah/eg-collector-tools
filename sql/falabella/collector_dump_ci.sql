SELECT CI_Id,CI_Name,CC_Id 
    FROM Configuration_Items 
    WHERE CI_Id=23;

SELECT * 
    FROM Cost_Centers 
    WHERE CC_Id 
        IN (SELECT CC_Id 
                FROM Configuration_Items 
                WHERE CI_Id=23);

SELECT CI_Id,CU_Id,CU_Description,CU_Quantity 
    FROM Charge_Units 
    WHERE CI_Id=23;

SELECT COUNT(*),SUM(CU_Quantity) 
    FROM Charge_Units 
    WHERE CI_Id=23 AND Typ_Code='DSK'
    INTO @CI_DISKS,@CI_DISK_CAPACITY;

SELECT CU_Id 
    FROM Charge_Units 
    WHERE CI_Id=23 AND TYP_CODE="DSK";


SELECT 
    CU_Id,COUNT(*),
    SUM(CIT_Quantity) AS GB_HR,
    SUM(CIT_Quantity)/count(*) AS AVERAGE,
    SUM(CIT_Quantity)/720  AS GB_MONTH
    FROM Charge_Items_202003 
    WHERE CU_Id IN (SELECT CU_Id 
                        FROM Charge_Units 
                        WHERE CI_Id=23 AND TYP_CODE="DSK")
    GROUP BY CU_Id;
    
SELECT COUNT(*),
    SUM(CIT_Quantity),
    SUM(CIT_Quantity)/COUNT(*),
    SUM(CIT_Quantity)/720
    FROM Charge_Items_202003 
    WHERE CU_Id IN (SELECT CU_Id 
                        FROM Charge_Units 
                        WHERE CI_Id=23 AND TYP_CODE="DSK");
    


SELECT COUNT(*) 
    FROM Charge_Items_202003 
    WHERE CU_Id IN (SELECT CU_Id 
                        FROM Charge_Units 
                        WHERE CI_Id=23 AND TYP_CODE="DSK"
                    )
    INTO @DSK_SLICES;

SELECT CIT_Quantity 
    FROM Charge_Items_202003 
    WHERE CU_Id IN (SELECT CU_Id 
                        FROM Charge_Units 
                        WHERE CI_Id=23 AND TYP_CODE="DSU"
                    )
    INTO @DSU_QUANTITY;

SELECT CU_Id,CIT_Quantity AS DSK_USAGE_QUANTITY 
    FROM Charge_Items_202003 
    WHERE CU_Id IN (SELECT CU_Id 
                        FROM Charge_Units 
                        WHERE CI_Id=23 AND TYP_CODE="DSU"
                    );

SELECT DAY("2020-03-31")-DAY("2020-03-01")+1 INTO @DAYS_IN_MARCH;
SELECT 24*(DAY("2020-03-31")-DAY("2020-03-01")+1) INTO @SLICES_IN_MARCH;

-- ---------------------------------------------------------------------
-- Adjust intented to consider actual Commissioning period with in month
-- ---------------------------------------------------------------------
-- SELECT CI_Commissioning_DateTime
--    FROM Configuration_Items WHERE CI_Id=23;
--
-- SELECT DAY("2020-03-31")-DAY(CI_Commissioning_DateTime)+1
--    FROM Configuration_Items WHERE CI_Id=23 INTO @DAYS_IN_MARCH;
-- 
-- SELECT 24*@DAYS_IN_MARCH INTO @SLICES_IN_MARCH;
-- ---------------------------------------------------------------------

SELECT
    @DAYS_IN_MARCH,
    @SLICES_IN_MARCH,
    @CI_DISKS,
    @CI_DISK_CAPACITY,
    @SLICES_IN_MARCH*@CI_DISKS AS EXPECTED_SLICES,
    @DSK_SLICES,
    @DSK_SLICES/(@SLICES_IN_MARCH*@CI_DISKS) AS RATIO,
    @DSU_QUANTITY,
    @DSU_QUANTITY*@DSK_SLICES/(@SLICES_IN_MARCH*@CI_DISKS) AS BILLEABLE
    ;
