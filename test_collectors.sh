q#!/bin/bash
# NUTANIX Prism Element API v2

echo 
echo '******************************************************'
echo testing Lab Sertechno 142 v2
echo '******************************************************'
echo

USER=gvalera
PASSWORD=Pass1010
HOST=10.26.1.142
PORT=9440
ROUTE=PrismGateway/services/rest/v2.0
OFFSET=0
LENGTH=100
INCLUDE_DISK='true'
INCLUDE_NIC='true'
OUTPUT_FILE=Lab_Nutanix_142_v2.json
XCALL=vms/\?offset=$OFFSET\&length=$LENGTH\&include_vm_disk_config=$INCLUDE_DISK\&include_vm_nic_config=$INCLUDE_NIC
HEADER='Accept: application/json'

echo Call is=$XCALL

URL=https://$HOST:$PORT/$ROUTE/$XCALL


echo URL is=$URL

curl -k -u $USER:$PASSWORD -X GET --header '$HEADER' $URL > $OUTPUT_FILE


# https://10.26.1.142:9440/PrismGateway/services/rest/v2.0/vms/?offset=0&length=100&include_vm_disk_config=true&include_vm_nic_config=true


#NUTANIX Prism Element API v3
echo 
echo '******************************************************'
echo testing Lab Sertechno 142 v3
echo '******************************************************'
echo

CONTENT='Content-Type: application/json'
AUTHORIZATION="Authorization: Basic Z3ZhbGVyYTpQYXNzMTAxMA==" 
ROUTE=api/nutanix/v3
XCALL=vms/list
URL=https://$HOST:$PORT/$ROUTE/$XCALL
OUTPUT_FILE=Lab_Nutanix_142_v3.json

curl -k -X POST --header "$CONTENT" --header "$HEADER" --header "$AUTHORIZATION" -d "{
  \"kind\": \"vm\",
  \"offset\": $OFFSET,
  \"length\": $LENGTH
}" $URL > $OUTPUT_FILE

#}" "https://10.26.1.142:9440/api/nutanix/v3/vms/list" >> Lab_Nutanix_142_v3.json

#https://10.26.1.142:9440/api/nutanix/v3/vms/list

#NUTANIX Prism Central 147 API v3
echo 
echo '******************************************************'
echo testing Lab Sertechno 147 v3
echo '******************************************************'
echo

HOST=10.26.1.147
URL=https://$HOST:$PORT/$ROUTE/$XCALL
OUTPUT_FILE=Lab_Nutanix_147_v3.json

curl -k -X POST --header "$CONTENT" --header "$HEADER" --header "$AUTHORIZATION" -d "{
  \"kind\": \"vm\",
  \"offset\": $OFFSET,
  \"length\": $LENGTH
}" $URL > $OUTPUT_FILE

#https://10.26.1.147:9440/api/nutanix/v3/vms/list

