# Collector Services Configuration

Runs as a service in linux environment

1. Create symbolic link for Collector Service Daemon script

    cd /usr/local/bin
    sudo ln -s <Collector Root Folder>/collectord collectord

2. Create symbolic link for Collector Service Configuration

    cd /lib/systemd/system
    sudo ln -s <Collector Service Folder>/collectord.service collectord.service

3. Standard service call will work now ...

    sudo systemctl start collectord
    sudo systemctl enable collectord
    sudo systemctl stop collectord
    sudo systemctl restart collectord
    
Service logging is as per "log_format" defines in <Collector Root Folder>/collector.ini (Configuration File)
        
## New Collectors definition:

A new Collector activity is configuring by creating a configuration file with in : 

**<Collector Root Folder>/service/plugins**
    
A new collector needs to include:

Collector's .ini file           Collector configuration file (<Collector Root Folder>/service/plugins)
                                this references Plug In Code in key: [General] collector
Collector's Plug In Code        Actual PlugIn Code (<Collector Root Folder>/service/collectors)
                                this shouuld imports actual platform specific code from (<Collector Root Folder>/service/platforms)
    
From our previous example, our first collector should have:

Using:
    /home/collector                     <Collector Root Folder>
    /home/collector/service             <Collector Service Folder>
    /home/collector/service/plugins     <Collector Plugins Folder>
    /home/collector/service/collectors  <Collector Collectors Folder>
    /home/collector/service/platforms   <Collector Platforms Folder>

<Collector Plugins Folder>/demo_platform_1.ini     Configuration for demo platform 1 (References Nutanix_ETL Collector)
<Collector Collectors Folder>/Nutanix_ETL.py       Collector For Nutanix Platform (can be referenced/used for various platforms)
<Collector Platforms Folder>/nutanix_etl.py        Actual Nutanix Platform specific code (low level ETL Code)
    
    
NOTES:
<Configuration File>            Defaults to <Collector Root Folder>/collector.ini
<Collector Root Folder>         Defined in <Configuration File> as [app_folder]
<Collector Service Folder>      Defined in <Configuration File> as [service_folder]

In development mode Flask Web server can be used and also a Web Service can be activated:
service/collectorwd.service must be setup the same way as collectord.service


