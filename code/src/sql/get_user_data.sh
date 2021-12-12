source colors.sh
source get_config.sh

COST_CENTER=30000000
CUSTOMER=3
QUERY="
SELECT
    Configuration_Items.Cus_Id,
    CC_Id,CC_Description,
    CI_Id,CI_Name,
    CU_Id,Typ_Code
    FROM Charge_Units
    JOIN Configuration_Items USING (CI_Id)
    JOIN Cost_Centers        USING (CC_Id)
    WHERE CI_NAME NOT LIKE 'NBUBVG%'
      AND Configuration_Items.Cus_Id >= ${CUSTOMER}
    ORDER BY CC_Id,CI_Name,CU_Description
"
echo
echo -e ${yellow}${bold}"User Data ..."${normal}
echo
#echo mysql -u ${USER} -p${PASS} -h ${HOST} ${SCHEMA} -e "${QUERY}"
     mysql -N -B -u ${USER} -p${PASS} -h ${HOST} ${SCHEMA} -e "${QUERY}" > user_data.tsv 
echo

