#Collector Makefile Structure and dependencies

## Routes

Defines all needed routes

Collector
	Application
		Main
		Common
		Templates
	Service
	
Tools
	code
		src
			common
		output
		auto
			models
			forms
			views
			templates
			includes
			
Creation Rules:
all			${AUTO_TEMPLATES}/base.html
			classes
			collector
			
classes		python gen_collector_menu.py
				base_file_name
				navbar_file_name
			python ${SUITE_TOOLS_FOLDER}/populate_dev_tables.py ${SUITE_TOOLS_FOLDER}/gen_collector.ini
			python ${SUITE_TOOLS_FOLDER}/gen_models_code.py ${SUITE_TOOLS_FOLDER}/gen_collector.ini
	

