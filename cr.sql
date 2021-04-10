select
    count(*),
    Charge_Items_202003.CU_Id,
    Charge_Units.CU_Id,
    Charge_Units.CI_Id,
    Charge_Units.Rat_Id, 
    Configuration_Items.CI_Id,
    Configuration_Items.Cus_Id,
    Configuration_Items.CC_Id,
    SUM(CIT_Quantity),
    Cost_Centers.CC_Description,
    Platforms.Pla_Name,
    Rates.Rat_Price,
    min(CIT_DateTime),
    max(CIT_DateTime)

from Charge_Items_202003 
    join Charge_Units           on Charge_Units.CU_Id = Charge_Items_202003.CU_Id
    join Configuration_Items    on Configuration_Items.CI_Id=Charge_Units.CI_Id 
    join Cost_Centers           on Cost_Centers.CC_Id = Configuration_Items.CC_Id 
    join Customers              on Customers.Cus_Id = Configuration_Items.Cus_Id  
    Join Platforms              on Platforms.Pla_Id = Configuration_Items.Pla_Id 
    join Rates                  on Rates.Rat_Id = Charge_Units.Rat_Id
where
    Charge_Items_202003.CIT_Status    =  1             and
    -- Charge_Items_202003.CIT_DateTime  between str_to_date("2020-03-01","%Y-%m-%d")  and str_to_date("2020-03-01","%Y-%m-%d") and
    Charge_Items_202003.CIT_DateTime  >= str_to_date("2020-03-01","%Y-%m-%d")  and
    Charge_Items_202003.CIT_DateTime  <= str_to_date("2020-04-01","%Y-%m-%d")  and
    Configuration_Items.Cus_Id        =  2             and
    Charge_Units.CI_Id                =  23
group by
    Charge_Items_202003.CU_Id
order by
    Configuration_Items.Cus_Id,
    Charge_Units.CI_Id,
    Charge_Items_202003.CU_Id
    ;

-- select *
-- from Charge_Items_202003
--    join Charge_Units           on Charge_Units.CU_Id = Charge_Items_202003.CU_Id
--    join Configuration_Items    on Configuration_Items.CI_Id=Charge_Units.CI_Id 
--    join Cost_Centers           on Cost_Centers.CC_Id = Configuration_Items.CC_Id 
--    join Customers              on Customers.Cus_Id = Configuration_Items.Cus_Id  
--    Join Platforms              on Platforms.Pla_Id = Configuration_Items.Pla_Id 
--    join Rates                  on Rates.Rat_Id = Charge_Units.Rat_Id
-- where
--    Charge_Items_202003.CIT_Status    =  1            and
--    Charge_Units.CI_Id                =  23
--    ;
