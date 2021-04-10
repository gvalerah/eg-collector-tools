source colors.sh
echo -e ${bold}${purple}Updating static files ...
update_statics.sh
echo -e Customizing files and others ...${normal}
customize.sh
sudo /home/collector/bin/update_collector.sh
sudo /home/collector/bin/update_collector_services.sh
sudo /home/collector/bin/update_collector_drv_nutanix.sh
echo -e ${bold}${purple}
echo --------------------------------------------------
echo Collector Suite updated !!!
echo --------------------------------------------------
echo -e ${normal}

