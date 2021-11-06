source colors.sh
source get_config.sh
echo
echo -e ${yellow}${bold}"List of Virtual Machines in Prism Central ..."${normal}
echo
      ENDPOINT="https://${PCHOST}:${PCPORT}/${PCROUTE}vms/list"
       CONTENT="Content-Type: application/json"
        ACCEPT="Accept: application/json"
AUTHENTICATION="${PCUSERNAME}:${PCPASSWORD}"
       OPTIONS="-k -v" 
      PROTOCOL="POST"
          DATA="{\"kind\":\"vm\"}"

CURL="curl ${OPTIONS} \
     -u ${AUTHENTICATION} \
     -X ${PROTOCOL} \
     -H '${CONTENT}' \
     -H '${ACCEPT}' \
     -d '$DATA' \
     ${ENDPOINT}"
#echo curl $CURL
     eval $CURL 2>/dev/null 1>/tmp/PC_virtual_machines.json
PCVM=$(cat /tmp/PC_virtual_machines.json|jq .metadata.total_matches)
echo -e ${cyan}PC Virtual Machines = ${normal}${PCVM}
echo

