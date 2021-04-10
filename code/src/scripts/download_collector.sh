source colors.sh
FILES="1 2 3 4 5 app_static templates install sample scripts"
echo -e ${bold}${yellow}Going to working folder ...${normal} 
cd /home/collector/download
echo -n -e ${cyan}
pwd
echo -n -e ${normal}
mv -f  /home/collector/download/*.tgz /home/collector/download/bkup
cp -r  /home/collector/download/home  /home/collector/download/bkup
rm -rf /home/collector/download/home
echo Downloading files ...
for file in $FILES
do
	echo -e ${bold}${yellow}Downloading ${cyan}collector_${file}.tgz ...${normal}
	echo
	wget http://desarrollo.sertechno.com/lpar2rrd/EG-Collector/collector_${file}.tgz
done
echo Unpacking files ...
for file in $FILES
do
	echo -e ${bold}${yellow}Unpacking ${cyan}collector_${file}.tgz${normal}
	echo
	tar zxf collector_${file}.tgz
done
echo 
echo -e ${green}Download completed ...
echo
echo -e ${bold}${yellow}Copying data ...
cp -R home/gvalera/collector/* /home/collector
echo
echo -e ${green}Actual binaries ...
ls -l /home/collector/bin
echo
echo -e ${purple}new binaries
ls -l /home/collector/dist
echo -e ${bold}${yellow}
echo ----------------------------------------------------------------
echo Now you need to update binaries, need to stop services first ...
echo ----------------------------------------------------------------
echo -e ${normal}
