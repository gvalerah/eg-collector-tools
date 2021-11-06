if [ -z $1 ]
then
    ROOT=~/GIT/EG-Collector
else
    ROOT=$1
fi
if [ -z $2 ]
then
    INIFILE=${ROOT}/collector.ini
else
    INIFILE=${ROOT}/$2
fi
         USER=$(ReadIni DB user user ${INIFILE})
         PASS=$(echo $(ReadIni DB password password ${INIFILE}))
         HOST=$(ReadIni DB host localhost ${INIFILE})
         PORT=$(ReadIni DB port 3306 ${INIFILE})
       SCHEMA=$(ReadIni DB schema collector ${INIFILE})

#echo USER   = "${USER}"
#echo PASS   = "${PASS}"
#printf "%q\n" $PASS
#printf "%s\n" $PASS
#echo HOST   = "${HOST}"
#echo PORT   = "${PORT}"
#echo SCHEMA = "${SCHEMA}"
       
       
 PRISMCENTRAL=Nutanix_1_PC_3
PRISMELEMENT1=Nutanix_1_PE_1
PRISMELEMENT2=Nutanix_1_PE_2
PRISMELEMENT3=Nutanix_1_PE_3

#echo ${USER}:${PASS}@${HOST}:${PORT}/${SCHEMA}

 PCUSERNAME=$(ReadIni ${PRISMCENTRAL}  username username         ${INIFILE})
 PCPASSWORD=$(ReadIni ${PRISMCENTRAL}  password password         ${INIFILE})
     PCHOST=$(ReadIni ${PRISMCENTRAL}  host     host             ${INIFILE})
     PCPORT=$(ReadIni ${PRISMCENTRAL}  port     9440             ${INIFILE})
    PCROUTE=$(ReadIni ${PRISMCENTRAL}  route    api/nutanix/v3   ${INIFILE})
PE1USERNAME=$(ReadIni ${PRISMCENTRAL}  username username         ${INIFILE})
PE1PASSWORD=$(ReadIni ${PRISMCENTRAL}  password password         ${INIFILE})
    PE1HOST=$(ReadIni ${PRISMELEMENT1} host     host             ${INIFILE})
    PE1PORT=$(ReadIni ${PRISMCENTRAL}  port     9440             ${INIFILE})
   PE1ROUTE=$(ReadIni ${PRISMELEMENT1} route    api/nutanix/v2.0 ${INIFILE})
PE2USERNAME=$(ReadIni ${PRISMELEMENT2} username username         ${INIFILE})
PE2PASSWORD=$(ReadIni ${PRISMCENTRAL}  password password         ${INIFILE})
    PE2HOST=$(ReadIni ${PRISMELEMENT2} host     host             ${INIFILE})
    PE2PORT=$(ReadIni ${PRISMCENTRAL}  port     9440             ${INIFILE})
   PE2ROUTE=$(ReadIni ${PRISMELEMENT2} route    api/nutanix/v2.0 ${INIFILE})
PE3USERNAME=$(ReadIni ${PRISMELEMENT2} username username         ${INIFILE})
PE3PASSWORD=$(ReadIni ${PRISMCENTRAL}  password password         ${INIFILE})
    PE3HOST=$(ReadIni ${PRISMELEMENT3} host     host             ${INIFILE})
    PE3PORT=$(ReadIni ${PRISMCENTRAL}  port     9440             ${INIFILE})
   PE3ROUTE=$(ReadIni ${PRISMELEMENT3} route    api/nutanix/v2.0 ${INIFILE})


#echo ${PRISMCENTRAL}: ${PCUSERNAME}:${PCPASSWORD}@${PCHOST}:${PCPORT}/${PCROUTE}
#echo ${PRISMELEMENT1}: ${PE1USERNAME}:${PE1PASSWORD}@${PE1HOST}:${PE1PORT}/${PE1ROUTE}
#echo ${PRISMELEMENT2}: ${PE2USERNAME}:${PE2PASSWORD}@${PE2HOST}:${PE2PORT}/${PE2ROUTE}
#echo ${PRISMELEMENT3}: ${PE3USERNAME}:${PE3PASSWORD}@${PE3HOST}:${PE3PORT}/${PE3ROUTE}


