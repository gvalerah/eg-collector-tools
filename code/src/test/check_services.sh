SERVICES="collector_services"
TIMESTAMP=$(date +%Y%m%d%H%M%S)
LOG="/tmp/check_services_${TIMESTAMP}.log"
while true
do
        for s in ${SERVICES}
        do
                PID=$(sudo systemctl show ${s} --property MainPID|awk -F "=" '{print $2}')
                TOTAL=$(sudo pmap ${PID}|tail -n 1|awk -F " " '{print $2}')
                TIMESTAMP=$(date +%Y-%m-%d/%H:%M:%S)
                printf '%-25s %17s %8s %s\n' ${s} ${TIMESTAMP} ${PID} ${TOTAL} >>${LOG}
		CHILDREN=$(pgrep -P ${PID})
		#echo children = ${CHILDREN}
		for cpid in ${CHILDREN}
		do
                	CTOTAL=$(sudo pmap ${cpid}|tail -n 1|awk -F " " '{print $2}')
                	printf '%-25s %17s %8s %s\n' ${s} ${TIMESTAMP} ${cpid} ${CTOTAL} >>${LOG}
		done
        done
        sleep 10
done

