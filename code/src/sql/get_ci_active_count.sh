source colors.sh
source get_config.sh

QUERY="
SELECT
    Cus_Id AS 'ID',
    IF(CI_Decommissioning_DateTime IS NULL,'ACTIVE','INACTIVE') AS 'ACTIVE',
    count(*) AS 'COUNT'
    FROM Configuration_Items 
    GROUP BY Cus_Id,ACTIVE
    ORDER BY Cus_Id,ACTIVE
"
echo
echo -e ${yellow}${bold}"Configuration Items's status per customer ..."${normal}
echo
#echo mysql -u ${USER} -p${PASS} ${SCHEMA} -e "${QUERY}"
     mysql -u ${USER} -p${PASS} ${SCHEMA} -e "${QUERY}" 2>/dev/null
echo

