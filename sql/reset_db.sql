use collector;
select "Delete C items";
delete from Charge_Items where CU_Id in (select CU_Id from Charge_Units where CI_Id in (select CI_Id from Configuration_Items where CI_Name="CI NO NAME"));
select count(*) from Charge_Items where CU_Id in (select CU_Id from Charge_Units where CI_Id in (select CI_Id from Configuration_Items where CI_Name="CI NO NAME"));
select "Delete C Units";
delete from Charge_Units where CI_Id in (select CI_Id from Configuration_Items where CI_Name="CI NO NAME");
select count(*) from Charge_Units where CI_Id in (select CI_Id from Configuration_Items where CI_Name="CI NO NAME");
select "Delete CIs";
delete from Configuration_Items where CI_Name="CI NO NAME";
select count(*) from Configuration_Items where CI_Name="CI NO NAME";

select count(*) from Charge_Items;
select count(*) from Charge_Units;
select count(*) from Configuration_Items;

