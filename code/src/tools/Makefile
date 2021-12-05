all: egc_tools_get_charge_resume

egc_tools_get_charge_resume:	egc_tools_get_charge_resume.py
	pyinstaller --onefile --hidden-import mysql --hidden-import pymysql egc_tools_get_charge_resume.py
	
