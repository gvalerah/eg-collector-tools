source colors.sh
source get_config.sh
echo
echo -e ${yellow}${bold}"List of Volume Groups per Node ..."${normal}
echo
ENDPOINT="https://${PE1HOST}:${PE1PORT}/${PE1ROUTE}/volume_groups/"
ACCEPT="Accept: application/json"
AUTHENTICATION="${PE1USERNAME}:${PE1PASSWORD}"
OPTIONS="-k" 
PROTOCOL="GET"
CURL="curl ${OPTIONS} \
     -u ${AUTHENTICATION} \
     -X ${PROTOCOL} \
     -H '${ACCEPT}' \
     ${ENDPOINT}"
#echo ${CURL}
eval ${CURL} 2>/dev/null 1>/tmp/PE1_volume_groups.json
PE1VG=$(cat /tmp/PE1_volume_groups.json|jq .metadata.count)
echo -e ${cyan}PE 1 Volume Groups = ${normal}${PE1VG}

ENDPOINT="https://${PE2HOST}:${PE2PORT}/${PE2ROUTE}/volume_groups/"
ACCEPT="Accept: application/json"
AUTHENTICATION="${PE2USERNAME}:${PE2PASSWORD}"
OPTIONS="-k" 
PROTOCOL="GET"
CURL="curl ${OPTIONS} \
     -u ${AUTHENTICATION} \
     -X ${PROTOCOL} \
     -H '${ACCEPT}' \
     ${ENDPOINT}"

#echo ${CURL}
eval ${CURL} 2>/dev/null 1>/tmp/PE2_volume_groups.json
PE2VG=$(cat /tmp/PE2_volume_groups.json|jq .metadata.count)
echo -e ${cyan}PE 2 Volume Groups = ${normal}${PE2VG}
echo


