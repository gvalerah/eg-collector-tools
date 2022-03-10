source colors.sh
source get_config.sh

PERIOD=$1

USER=collector
PASS=Password1$
SCHEMA=collector

QUERY="
SELECT
	Cus_Id AS CUSTOMER,
	CI_Name AS NAME,
	count(*) AS ITEMS 
FROM Charge_Items_3_${PERIOD}
JOIN Charge_Units using (CU_Id) 
JOIN Configuration_Items using (CI_Id) 
GROUP BY Cus_Id,CI_Name
ORDER BY Cus_Id,CI_Name
"
echo
echo -e ${yellow}${bold}"Configuration Items's USED IN PERIOD ${PERIOD} ..."${normal}
echo
echo mysql -B -u ${USER} -p${PASS} ${SCHEMA} -e "${QUERY}"
     mysql    -u ${USER} -p${PASS} ${SCHEMA} -e "${QUERY}" 2>/dev/null
     mysql -B -u ${USER} -p${PASS} ${SCHEMA} -e "${QUERY}">get_period_cis_${PERIOD}.csv 2>/dev/null 
echo

