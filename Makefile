# Application folders
COLLECTOR_FOLDER=/home/gvalera/collector
APP_FOLDER=${COLLECTOR_FOLDER}/app
SERVICE_FOLDER=${COLLECTOR_FOLDER}/service
MAIN_FOLDER=${APP_FOLDER}/main
COMMON_FOLDER=${APP_FOLDER}/common
TEMPLATES_FOLDER=${APP_FOLDER}/templates

# Auto Code Folders
TOOLS_FOLDER=/home/gvalera/GIT/EG-Collector-Tools
CODE_FOLDER=${TOOLS_FOLDER}/code
CODE_SRC=${CODE_FOLDER}/src
CODE_COMMON=${CODE_SRC}/common
CODE_OUTPUT=${CODE_FOLDER}/output

AUTO_FOLDER=${CODE_FOLDER}/auto
AUTO_MODELS=${AUTO_FOLDER}/models
AUTO_FORMS=${AUTO_FOLDER}/forms
AUTO_VIEWS=${AUTO_FOLDER}/views
AUTO_TEMPLATES=${AUTO_FOLDER}/templates
AUTO_INCLUDES=${AUTO_FOLDER}/includes

# Emtec Library updates for Collector App
LIB_EMTEC=/home/gvalera/GIT/eg-libraries/emtec/src/emtec
LIB_COLLECTOR=${LIB_EMTEC}/collector
LIB_COLLECTOR_DB=${LIB_COLLECTOR}/db

all:	${AUTO_TEMPLATES}/base.html classes collector 

collector:	${CODE_OUTPUT}/models.py ${CODE_OUTPUT}/ORM_models.py ${CODE_OUTPUT}/forms.py ${CODE_OUTPUT}/views.py ${CODE_SRC}/*.py ${AUTO_TEMPLATES}/base.html
	echo
	echo "***********************************"
	echo "* Updating Collector's  Auto Files *"
	echo "***********************************"
	echo
	echo
	echo "COLLECTOR_FOLDER =" ${COLLECTOR_FOLDER}
	echo "APP_FOLDER       =" ${APP_FOLDER}
	echo "MAIN_FOLDER      =" ${MAIN_FOLDER}
	echo "TEMPLATES_FOLDER =" ${TEMPLATES_FOLDER}
	echo "AUTO_FOLDER      =" ${AUTO_FOLDER}
	echo "AUTO_MODELS      =" ${AUTO_MODELS}
	echo "AUTO_FORMS       =" ${AUTO_FORMS}
	echo "AUTO_VIEWS       =" ${AUTO_VIEWS}
	echo "AUTO_TEMPLATES   =" ${AUTO_TEMPLATES}
	echo "AUTO_INCLUDES    =" ${AUTO_INCLUDES}
	
	echo
	echo updating functions source files ...
	./link_functions.sh
	
	echo updating ${LIB_COLLECTOR_DB}/Flask_models.py ...
	cp ${CODE_OUTPUT}/models.py       		${LIB_COLLECTOR_DB}/Flask_models.py
	
	echo updating ${LIB_COLLECTOR_DB}/ORM_models.py ...
	cp ${CODE_OUTPUT}/ORM_models.py       		${LIB_COLLECTOR_DB}/ORM_models.py
	
	echo updating ${LIB_COLLECTOR}/forms.py ...
	cp ${CODE_OUTPUT}/forms.py       		${LIB_COLLECTOR}/forms.py
	
	echo "updating ${MAIN_FOLDER}/views.py ..."
	cp ${CODE_OUTPUT}/views.py       		${MAIN_FOLDER}/views.py
	
	echo "updating ${TEMPLATES_FOLDER}/base.html ..."
	echo
	cp  ${AUTO_TEMPLATES}/base.html        		${TEMPLATES_FOLDER}/base.html

	echo "updating ${APP_FOLDER}/templates ..."
	echo
	cp  ${AUTO_TEMPLATES}/*.html     		${TEMPLATES_FOLDER}/.
	cp  ${CODE_SRC}/templates/*.html     		${TEMPLATES_FOLDER}/.

	echo "updating COMMON files ..."
	echo
	cp  ${CODE_COMMON}/*.py     			${COMMON_FOLDER}/.

	echo "updating error handlers ..."
	echo
	cp  ${CODE_SRC}/errors.py			${MAIN_FOLDER}/errors.py

	ls -l ${COLLECTOR_FOLDER}/collector.py
	ls -l ${LIB_COLLECTOR_DB}/ORM_models.py
	ls -l ${LIB_COLLECTOR_DB}/Flask_models.py
	ls -l ${LIB_COLLECTOR}/forms.py
	ls -l ${MAIN_FOLDER}/errors.py
	ls -l ${MAIN_FOLDER}/views.py
	ls -l ${TEMPLATES_FOLDER}/base.html
	ls -l ${TEMPLATES_FOLDER}/*_charging_*.html
	echo
 
classes:
	echo
	echo "***********************************"
	echo "* Generating DB Clasess AUTOCODE  *"
	echo "***********************************"
	echo
	python gen_collector_menu.py
	python populate_dev_tables.py
	python gen_collector_model_flask.py


${CODE_OUTPUT}/models.py:	${AUTO_MODELS}/*.py ${CODE_SRC}/*.py ${CODE_SRC}/models/*.py
	echo
	echo "***********************************"
	echo "* Creating models.py *"
	echo "***********************************"
	echo
	cat ${CODE_SRC}/models_py_header.py  		>  ${CODE_OUTPUT}/models.py
	cat ${CODE_SRC}/models_py_header_auth.py  	>> ${CODE_OUTPUT}/models.py
	cat ${AUTO_MODELS}/flask_*.py  				>> ${CODE_OUTPUT}/models.py
	cat ${CODE_SRC}/models/*.py            		>> ${CODE_OUTPUT}/models.py
	ls -l ${CODE_OUTPUT}/models.py

${CODE_OUTPUT}/ORM_models.py:	${AUTO_MODELS}/orm_*.py ${CODE_SRC}/*.py 
	echo
	echo "***********************************"
	echo "* Creating ORM_models.py *"
	echo "***********************************"
	echo
	cat ${CODE_SRC}/orm_models_py_header.py		>  ${CODE_OUTPUT}/ORM_models.py
	cat ${AUTO_MODELS}/base.py					>> ${CODE_OUTPUT}/ORM_models.py
	cat ${AUTO_MODELS}/orm_*.py  				>> ${CODE_OUTPUT}/ORM_models.py
	ls -l ${CODE_OUTPUT}/ORM_models.py

${CODE_OUTPUT}/forms.py:	${AUTO_FORMS}/*.py ${CODE_SRC}/*.py ${CODE_SRC}/forms/*.py
	echo
	echo "***********************************"
	echo "* Creating forms.py *"
	echo "***********************************"
	echo
	cat ${CODE_SRC}/forms_py_header.py  		>  ${CODE_OUTPUT}/forms.py
	#cat ${CODE_SRC}/forms_py_header_auth.py  	>> ${CODE_OUTPUT}/forms.py
	cat ${AUTO_FORMS}/*.py  					>> ${CODE_OUTPUT}/forms.py
	cat ${CODE_SRC}/forms/*.py            		>> ${CODE_OUTPUT}/forms.py
	ls -l ${CODE_OUTPUT}/forms.py
	
	
${CODE_SRC}/forms/*.py:
	./link_functions.sh


${CODE_OUTPUT}/views.py:	${AUTO_VIEWS}/*.py ${CODE_OUTPUT}/models.py
	echo
	echo "***********************************"
	echo "* Creating views.py *"
	echo "***********************************"
	echo
	cat ${CODE_SRC}/views_py_header.py    		>  ${CODE_OUTPUT}/views.py
	cat ${AUTO_INCLUDES}/models_py_imports.py	>> ${CODE_OUTPUT}/views.py
	cat ${CODE_SRC}/views_py_collector.py 		>> ${CODE_OUTPUT}/views.py
	cat ${AUTO_VIEWS}/*.py                		>> ${CODE_OUTPUT}/views.py
	cat ${CODE_SRC}/views/*.py            		>> ${CODE_OUTPUT}/views.py
	ls -l ${CODE_OUTPUT}/views.py

${AUTO_TEMPLATES}/base.html:
	echo
	echo "***********************************"
	echo "* Generating base.html            *"
	echo "***********************************"
	echo
	python gen_collector_menu.py

clean:
	mv models/base.py models/base.py.sav
	rm models/*.py
	mv models/base.py.sav models/base.py
	rm forms/*.py
	rm views/*.py
	
