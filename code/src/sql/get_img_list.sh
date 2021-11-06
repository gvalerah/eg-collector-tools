source colors.sh
source get_config.sh
echo
echo -e ${yellow}${bold}"List of images per Node ..."${normal}
echo
ENDPOINT="https://${PE1HOST}:${PE1PORT}/${PE1ROUTE}/images/?include_vm_disk_sizes=true"
ACCEPT="Accept: application/json"
AUTHENTICATION="${PE1USERNAME}:${PE1PASSWORD}"
OPTIONS="-k" 
PROTOCOL="GET"
DATA="{\"kind\":\"image\"}"
CURL="curl ${OPTIONS} \
     -u ${AUTHENTICATION} \
     -X ${PROTOCOL} \
     -H '${ACCEPT}' \
     ${ENDPOINT}"
#echo ${CURL}
eval ${CURL} 2>/dev/null 1>/tmp/PE1_images.json
#METADATA=$(cat /tmp/PE1_images.json|jq .metadata)
#echo METADATA=${METADATA}
PE1IMG=$(cat /tmp/PE1_images.json|jq .metadata.total_entities)
echo -e ${cyan}PE 1 Images = ${normal}${PE1IMG}

ENDPOINT="https://${PE2HOST}:${PE2PORT}/${PE2ROUTE}/images/?include_vm_disk_sizes=true"
AUTHENTICATION="${PE2USERNAME}:${PE2PASSWORD}"
CURL="curl ${OPTIONS} \
     -u ${AUTHENTICATION} \
     -X ${PROTOCOL} \
     -H '${ACCEPT}' \
     ${ENDPOINT}"

#echo ${CURL}
eval ${CURL} 2>/dev/null 1>/tmp/PE2_images.json
PE2IMG=$(cat /tmp/PE2_images.json|jq .metadata.total_entities)
echo -e ${cyan}PE 2 Images = ${normal}${PE2IMG}
echo


