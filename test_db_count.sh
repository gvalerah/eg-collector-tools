echo
echo
echo EG Collector data gatherer probe
echo
PASS=Password1$
SECS=10
while true;
do
	CI=$(mysql  -u collector --password=${PASS} -e "select count(*)  from Configuration_Items"  -N --batch collector 2>/dev/null)
	CU=$(mysql  -u collector --password=${PASS} -e "select count(*)  from Charge_Units"  -N --batch collector 2>/dev/null)
	CIT=$(mysql -u collector --password=${PASS} -e "select count(*)  from Charge_Items"  -N --batch collector 2>/dev/null)
	TS=$(date "+%Y-%m-%d %H:%M:%S")
	echo ${TS} CI=${CI} CU=${CU} CIT=${CIT}
	sleep $SECS
done


