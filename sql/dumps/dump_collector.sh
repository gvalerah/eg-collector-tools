echo Dump Collector Data
echo -n Collector DB Password?; stty -echo;read PASSWORD; stty echo; echo
USER=root
SCHEMA=collector
#echo [$PASSWORD]
tables=$(mysql $SCHEMA -u $USER -p$PASSWORD -se "SHOW TABLES")
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

for table in $tables
do
	echo $table ...
	mysqldump -u $USER -p$PASSWORD $SCHEMA $table > $table.sql 2>/dev/null
done
HOSTNAME=$(hostname)
ARCNAME=bkup/$HOSTNAME"_bkup-collector-db-tables_"$TIMESTAMP.tgz
echo Archiving dumps into $ARCNAME ...
tar zcf $ARCNAME *.sql
rm *.sql
echo Actual archives: 
ls -lh bkup/*.tgz
echo
cp $ARCNAME $HOME/BKUP
cp $ARCNAME $HOME/COMPARTIDO/BKUP
