# Application folders
        APP_NAME=Collector
COLLECTOR_FOLDER=/home/gvalera/collector
      APP_FOLDER=${COLLECTOR_FOLDER}/app
  SERVICE_FOLDER=${COLLECTOR_FOLDER}/service
     MAIN_FOLDER=${APP_FOLDER}/main
TEMPLATES_FOLDER=${APP_FOLDER}/templates

# Suite Tools structure folders
SUITE_TOOLS_FOLDER=/home/gvalera/GIT/EG-Suite-Tools
  SUITE_APP_FOLDER=${SUITE_TOOLS_FOLDER}/${APP_NAME}
 SUITE_CODE_FOLDER=${SUITE_APP_FOLDER}/code

# Suite Auto Code Folders structure
   SUITE_AUTO_FOLDER=${SUITE_CODE_FOLDER}/auto
   SUITE_AUTO_MODELS=${SUITE_AUTO_FOLDER}/models
    SUITE_AUTO_FORMS=${SUITE_AUTO_FOLDER}/forms
    SUITE_AUTO_VIEWS=${SUITE_AUTO_FOLDER}/views
SUITE_AUTO_TEMPLATES=${SUITE_AUTO_FOLDER}/templates
 SUITE_AUTO_INCLUDES=${SUITE_AUTO_FOLDER}/includes

       COLLECTOR_TOOLS_FOLDER=/home/gvalera/GIT/EG-Collector-Tools
        COLLECTOR_CODE_FOLDER=${COLLECTOR_TOOLS_FOLDER}/code
           COLLECTOR_CODE_SRC=${COLLECTOR_CODE_FOLDER}/src
        COLLECTOR_CODE_COMMON=${COLLECTOR_CODE_SRC}/common
        COLLECTOR_CODE_OUTPUT=${COLLECTOR_CODE_FOLDER}/output
          COLLECTOR_CODE_AUTO=${COLLECTOR_CODE_FOLDER}/auto
COLLECTOR_CODE_AUTO_TEMPLATES=${COLLECTOR_CODE_AUTO}/templates

# Emtec Library updates for Collector App
           LIB_EMTEC=/home/gvalera/GIT/eg-libraries/emtec/src/emtec
    LIB_EMTEC_COMMON=${LIB_EMTEC}/common
       LIB_COLLECTOR=${LIB_EMTEC}/collector
    LIB_COLLECTOR_DB=${LIB_COLLECTOR}/db
LIB_COLLECTOR_COMMON=${LIB_COLLECTOR}/common

all:	${SUITE_AUTO_TEMPLATES}/base.html classes collector 

collector:	${COLLECTOR_CODE_OUTPUT}/models.py ${COLLECTOR_CODE_OUTPUT}/orm_model.py ${COLLECTOR_CODE_OUTPUT}/forms.py ${COLLECTOR_CODE_OUTPUT}/views.py ${COLLECTOR_CODE_SRC}/*.py ${SUITE_AUTO_TEMPLATES}/base.html
	echo
	echo "***********************************"
	echo "* Updating Collector's  Auto Files *"
	echo "***********************************"
	echo
	echo
	echo "APP_NAME                     =" ${APP_NAME}
	echo "COLLECTOR_FOLDER             =" ${COLLECTOR_FOLDER}
	echo "APP_FOLDER                   =" ${APP_FOLDER}
	echo "MAIN_FOLDER                  =" ${MAIN_FOLDER}
	echo "TEMPLATES_FOLDER             =" ${TEMPLATES_FOLDER}
	echo "SUITE_TOOLS_FOLDER           =" ${SUITE_TOOLS_FOLDER}
	echo "SUITE_APP_FOLDER             =" ${SUITE_APP_FOLDER}
	echo "SUITE_CODE_FOLDER            =" ${SUITE_CODE_FOLDER}
	echo "SUITE_AUTO_FOLDER            =" ${SUITE_AUTO_FOLDER}
	echo "SUITE_AUTO_MODELS            =" ${SUITE_AUTO_MODELS}
	echo "SUITE_AUTO_FORMS             =" ${SUITE_AUTO_FORMS}
	echo "SUITE_AUTO_VIEWS             =" ${SUITE_AUTO_VIEWS}
	echo "SUITE_AUTO_TEMPLATES         =" ${SUITE_AUTO_TEMPLATES}
	echo "SUITE_AUTO_INCLUDES          =" ${SUITE_AUTO_INCLUDES}
	echo "COLLECTOR_TOOLS_FOLDER       =" ${COLLECTOR_TOOLS_FOLDER}
	echo "COLLECTOR_CODE_FOLDER        =" ${COLLECTOR_CODE_FOLDER}
	echo "COLLECTOR_CODE_SRC           =" ${COLLECTOR_CODE_SRC}
	echo "COLLECTOR_CODE_COMMON        =" ${COLLECTOR_CODE_COMMON}
	echo "COLLECTOR_CODE_OUTPUT        =" ${COLLECTOR_CODE_OUTPUT}
	echo "COLLECTOR_CODE_AUTO          =" ${COLLECTOR_CODE_AUTO}
	echo "COLLECTOR_CODE_AUTO_TEMPLATES=" ${COLLECTOR_CODE_AUTO_TEMPLATES}
	echo "LIB_EMTEC                    =" ${LIB_EMTEC}
	echo "LIB_EMTEC_COMMON             =" ${LIB_EMTEC_COMMON}
	echo "LIB_COLLECTOR                =" ${LIB_COLLECTOR}
	echo "LIB_COLLECTOR_DB             =" ${LIB_COLLECTOR_DB}
	echo "LIB_COLLECTOR_COMMON         =" ${LIB_COLLECTOR_COMMON}
	echo
	echo updating functions source files ...
	./link_functions.sh
	
	echo updating ${LIB_COLLECTOR_DB}/flask_models.py ...
	cp ${COLLECTOR_CODE_OUTPUT}/models.py       		${LIB_COLLECTOR_DB}/flask_models.py
	
	echo updating ${LIB_COLLECTOR_DB}/orm_model.py ...
	cp ${COLLECTOR_CODE_OUTPUT}/orm_model.py       		${LIB_COLLECTOR_DB}/orm_model.py
	
	echo updating ${LIB_COLLECTOR}/forms.py ...
	cp ${COLLECTOR_CODE_OUTPUT}/forms.py       		${LIB_COLLECTOR}/forms.py
	
	echo "updating ${MAIN_FOLDER}/views.py ..."
	cp ${COLLECTOR_CODE_OUTPUT}/views.py       		${MAIN_FOLDER}/views.py
	
	echo "updating ${TEMPLATES_FOLDER}/base.html ..."
	echo
	echo cp  ${SUITE_AUTO_TEMPLATES}/base.html        		${TEMPLATES_FOLDER}/base.html
	cp  ${SUITE_AUTO_TEMPLATES}/base.html        		${TEMPLATES_FOLDER}/base.html
	echo
	ls -l ${SUITE_AUTO_TEMPLATES}/base.html
	echo
	ls -l ${TEMPLATES_FOLDER}/base.html
	echo
	echo "updating ${APP_FOLDER}/templates ..."
	echo
	cp  ${SUITE_AUTO_TEMPLATES}/*.html     		${TEMPLATES_FOLDER}/.
	cp  ${COLLECTOR_CODE_SRC}/templates/*.html     		${TEMPLATES_FOLDER}/.
	echo
	echo "updating COMMON files ..."
	echo
	cp  ${COLLECTOR_CODE_COMMON}/collector/*.py     			${LIB_COLLECTOR_COMMON}/.
	ls -l ${LIB_COLLECTOR_COMMON}/.
	
	echo
	echo "updating error handlers ..."
	echo
	cp  ${COLLECTOR_CODE_SRC}/errors.py			${MAIN_FOLDER}/errors.py
	ls -l ${MAIN_FOLDER}/errors.py
	ls -l ${COLLECTOR_FOLDER}/collector.py
	ls -l ${LIB_COLLECTOR_DB}/orm_model.py
	ls -l ${LIB_COLLECTOR_DB}/flask_models.py
	ls -l ${LIB_COLLECTOR}/forms.py
	ls -l ${MAIN_FOLDER}/errors.py
	ls -l ${MAIN_FOLDER}/views.py
	echo
	ls -l ${TEMPLATES_FOLDER}/base.html
	echo
	ls -l ${TEMPLATES_FOLDER}/*_charging_*.html
	echo
 
classes:	gen_collector_menu.py
	echo
	echo "***********************************"
	echo "* Generating DB Clasess AUTOCODE  *"
	echo "***********************************"
	echo
	touch  gen_collector_menu.py
	python gen_collector_menu.py
	touch ${COLLECTOR_CODE_SRC}/*.py 
	touch ${COLLECTOR_CODE_SRC}/models/*.py
	cd ${SUITE_TOOLS_FOLDER}
	python ${SUITE_TOOLS_FOLDER}/populate_dev_tables.py ${SUITE_TOOLS_FOLDER}/gen_collector.ini
	python ${SUITE_TOOLS_FOLDER}/gen_models_code.py ${SUITE_TOOLS_FOLDER}/gen_collector.ini
	cd ${COLLECTOR_TOOLS_FOLDER}
	echo
	ls -l ${TEMPLATES_FOLDER}/base.html
	echo
	
${COLLECTOR_CODE_OUTPUT}/models.py:	${COLLECTOR_CODE_SRC}/*.py ${COLLECTOR_CODE_SRC}/models/*.py
	echo
	echo "***********************************"
	echo "* Creating models.py *"
	echo "***********************************"
	echo
	cat ${COLLECTOR_CODE_SRC}/models_py_header.py  		>  ${COLLECTOR_CODE_OUTPUT}/models.py
	cat ${COLLECTOR_CODE_SRC}/models_py_header_auth.py  	>> ${COLLECTOR_CODE_OUTPUT}/models.py
	cat ${SUITE_AUTO_MODELS}/flask_*.py  				>> ${COLLECTOR_CODE_OUTPUT}/models.py
	cat ${COLLECTOR_CODE_SRC}/models/*.py            		>> ${COLLECTOR_CODE_OUTPUT}/models.py
	cat ${COLLECTOR_CODE_SRC}/models_py_User_footer.py  	>> ${COLLECTOR_CODE_OUTPUT}/models.py
	ls -l ${COLLECTOR_CODE_OUTPUT}/models.py

${COLLECTOR_CODE_OUTPUT}/orm_model.py:	${COLLECTOR_CODE_SRC}/*.py 
	echo
	echo "***********************************"
	echo "* Creating orm_model.py *"
	echo "***********************************"
	echo
	cat ${COLLECTOR_CODE_SRC}/orm_models_py_header.py		>  	${COLLECTOR_CODE_OUTPUT}/orm_model.py
	cat ${SUITE_AUTO_MODELS}/ORM_model.py  			>> 	${COLLECTOR_CODE_OUTPUT}/orm_model.py
	cp  ${SUITE_AUTO_MODELS}/ORM_model_schema.py  		${COLLECTOR_CODE_OUTPUT}/orm_model_schema.py
	ls -l ${COLLECTOR_CODE_OUTPUT}/orm_model.py

${COLLECTOR_CODE_OUTPUT}/forms.py:	${COLLECTOR_CODE_SRC}/*.py ${COLLECTOR_CODE_SRC}/forms/*.py
	echo
	echo "***********************************"
	echo "* Creating forms.py *"
	echo "***********************************"
	echo
	cat ${COLLECTOR_CODE_SRC}/forms_py_header.py  		>  ${COLLECTOR_CODE_OUTPUT}/forms.py
	cat ${SUITE_AUTO_FORMS}/*.py  					>> ${COLLECTOR_CODE_OUTPUT}/forms.py
	cat ${COLLECTOR_CODE_SRC}/forms/*.py            		>> ${COLLECTOR_CODE_OUTPUT}/forms.py
	ls -l ${COLLECTOR_CODE_OUTPUT}/forms.py
	
${COLLECTOR_CODE_SRC}/forms/*.py:
	echo
	echo "***********************************"
	echo "* Creating symbolic links for ${COLLECTOR_CODE_SRC}/forms/*.py *"
	echo "***********************************"
	echo
	./link_functions.sh

${COLLECTOR_CODE_OUTPUT}/views.py:	${COLLECTOR_CODE_OUTPUT}/models.py
	echo
	echo "***********************************"
	echo "* Creating views.py *"
	echo "***********************************"
	echo
	cat ${COLLECTOR_CODE_SRC}/views_py_header.py    		>  ${COLLECTOR_CODE_OUTPUT}/views.py
	cat ${SUITE_AUTO_INCLUDES}/models_py_imports.py	>> ${COLLECTOR_CODE_OUTPUT}/views.py
	cat ${SUITE_AUTO_VIEWS}/*.py                		>> ${COLLECTOR_CODE_OUTPUT}/views.py
	cat ${COLLECTOR_CODE_SRC}/views/*.py            		>> ${COLLECTOR_CODE_OUTPUT}/views.py
	ls -l ${COLLECTOR_CODE_OUTPUT}/views.py

${SUITE_AUTO_TEMPLATES}/base.html:	gen_collector_menu.py
	echo
	echo "***********************************"
	echo "* Generating ${SUITE_AUTO_TEMPLATES}/base.html"
	echo "***********************************"
	echo
	python gen_collector_menu.py
	echo
	ls -l ${SUITE_AUTO_TEMPLATES}/base.html
	echo
	ls -l ${TEMPLATES_FOLDER}/base.html
	echo
	
clean:
	mv models/base.py models/base.py.sav
	rm models/*.py
	mv models/base.py.sav models/base.py
	rm forms/*.py
	rm views/*.py
	
