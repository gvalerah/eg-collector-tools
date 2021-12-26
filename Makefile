# Application folders
        APP_NAME=Collector
        APP_name=collector
COLLECTOR_FOLDER=/home/gvalera/GIT/EG-Collector
      APP_FOLDER=${COLLECTOR_FOLDER}/app
  SERVICE_FOLDER=${COLLECTOR_FOLDER}/service
    TOOLS_FOLDER=${COLLECTOR_FOLDER}/tools
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

# Emtec Library updates for Collector App
           LIB_EMTEC=/home/gvalera/GIT/eg-libraries/emtec/src/emtec
    LIB_EMTEC_COMMON=${LIB_EMTEC}/common
       LIB_COLLECTOR=${LIB_EMTEC}/collector
    LIB_COLLECTOR_DB=${LIB_COLLECTOR}/db
LIB_COLLECTOR_COMMON=${LIB_COLLECTOR}/common

all:	base.html classes collector 

collector:	${COLLECTOR_CODE_OUTPUT}/models.py ${COLLECTOR_CODE_OUTPUT}/orm_model.py ${COLLECTOR_CODE_OUTPUT}/forms.py ${COLLECTOR_CODE_OUTPUT}/views.py ${COLLECTOR_CODE_SRC}/*.py ${SUITE_AUTO_TEMPLATES}/base.html
	@echo
	@echo "***********************************"
	@echo "* Updating Collector's  Auto Files *"
	@echo "***********************************"
	@echo
	@echo
	@echo "APP_NAME                      =" ${APP_NAME}
	@echo "APP_name                      =" ${APP_name}
	@echo "COLLECTOR_FOLDER              =" ${COLLECTOR_FOLDER}
	@echo "APP_FOLDER                    =" ${APP_FOLDER}
	@echo "MAIN_FOLDER                   =" ${MAIN_FOLDER}
	@echo "TEMPLATES_FOLDER              =" ${TEMPLATES_FOLDER}
	@echo "SUITE_TOOLS_FOLDER            =" ${SUITE_TOOLS_FOLDER}
	@echo "SUITE_APP_FOLDER              =" ${SUITE_APP_FOLDER}
	@echo "SUITE_CODE_FOLDER             =" ${SUITE_CODE_FOLDER}
	@echo "SUITE_AUTO_FOLDER             =" ${SUITE_AUTO_FOLDER}
	@echo "SUITE_AUTO_MODELS             =" ${SUITE_AUTO_MODELS}
	@echo "SUITE_AUTO_FORMS              =" ${SUITE_AUTO_FORMS}
	@echo "SUITE_AUTO_VIEWS              =" ${SUITE_AUTO_VIEWS}
	@echo "SUITE_AUTO_TEMPLATES          =" ${SUITE_AUTO_TEMPLATES}
	@echo "SUITE_AUTO_INCLUDES           =" ${SUITE_AUTO_INCLUDES}
	@echo "COLLECTOR_TOOLS_FOLDER        =" ${COLLECTOR_TOOLS_FOLDER}
	@echo "COLLECTOR_CODE_FOLDER         =" ${COLLECTOR_CODE_FOLDER}
	@echo "COLLECTOR_CODE_SRC            =" ${COLLECTOR_CODE_SRC}
	@echo "COLLECTOR_CODE_COMMON         =" ${COLLECTOR_CODE_COMMON}
	@echo "COLLECTOR_CODE_OUTPUT         =" ${COLLECTOR_CODE_OUTPUT}
	@echo "COLLECTOR_CODE_AUTO           =" ${COLLECTOR_CODE_AUTO}
	@echo "LIB_EMTEC                     =" ${LIB_EMTEC}
	@echo "LIB_EMTEC_COMMON              =" ${LIB_EMTEC_COMMON}
	@echo "LIB_COLLECTOR                 =" ${LIB_COLLECTOR}
	@echo "LIB_COLLECTOR_DB              =" ${LIB_COLLECTOR_DB}
	@echo "LIB_COLLECTOR_COMMON          =" ${LIB_COLLECTOR_COMMON}
	@echo
	@echo updating functions source files ...
	@echo
	./link_functions.sh
	@echo
	@echo updating ${LIB_COLLECTOR_DB}/flask_models.py ...
	@cp ${COLLECTOR_CODE_OUTPUT}/models.py       		${LIB_COLLECTOR_DB}/flask_models.py
	@echo
	@echo updating ${LIB_COLLECTOR_DB}/orm_model.py ...
	@cp ${COLLECTOR_CODE_OUTPUT}/orm_model.py       		${LIB_COLLECTOR_DB}/orm_model.py
	@echo
	@echo updating ${LIB_COLLECTOR}/forms.py ...
	@cp ${COLLECTOR_CODE_OUTPUT}/forms.py       		${LIB_COLLECTOR}/forms.py
	@echo
	@echo "updating ${MAIN_FOLDER}/views.py ..."
	@md5sum ${COLLECTOR_CODE_OUTPUT}/views.py
	@md5sum ${MAIN_FOLDER}/views.py
	cp ${COLLECTOR_CODE_OUTPUT}/views.py       		${MAIN_FOLDER}/views.py
	@md5sum ${COLLECTOR_CODE_OUTPUT}/views.py
	@md5sum ${MAIN_FOLDER}/views.py
	@echo
	@echo "updating ${TEMPLATES_FOLDER}/base.html ..."
	@echo
	@echo cp  ${SUITE_AUTO_TEMPLATES}/base.html        		${TEMPLATES_FOLDER}/base.html
	@cp  ${SUITE_AUTO_TEMPLATES}/base.html        		${TEMPLATES_FOLDER}/base.html
	@echo
	@ls -l ${SUITE_AUTO_TEMPLATES}/base.html
	@echo
	@ls -l ${TEMPLATES_FOLDER}/base.html
	@echo
	@echo "updating ${TEMPLATES_FOLDER} templates ..."
	@echo
	cp  ${SUITE_AUTO_TEMPLATES}/*.html     		${TEMPLATES_FOLDER}/.
	ls -l ~/collector/app/templates/navbar_template.html
	cp  ${COLLECTOR_CODE_SRC}/templates/*.html     		${TEMPLATES_FOLDER}/.
	ls -l ~/collector/app/templates/navbar_template.html
	@echo
	@echo "updating COMMON files to" ${LIB_COLLECTOR_COMMON}
	@echo
	@cp  ${COLLECTOR_CODE_COMMON}/collector/*.py     			${LIB_COLLECTOR_COMMON}/.
	@ls -l ${LIB_COLLECTOR_COMMON}/.
	@echo
	@echo
	@echo "updating error handlers ..."
	@echo
	cp  ${COLLECTOR_CODE_SRC}/errors.py			${MAIN_FOLDER}/errors.py
	@ls -l ${MAIN_FOLDER}/errors.py
	@echo
	@echo "updating application static programs ..."
	@echo
	cp  ${COLLECTOR_CODE_SRC}/collector.py						${COLLECTOR_FOLDER}/collector.py
	cp  ${COLLECTOR_CODE_SRC}/collector_drv_nutanix.py			${COLLECTOR_FOLDER}/.
	cp  ${COLLECTOR_CODE_SRC}/collector_services.py				${COLLECTOR_FOLDER}/.
	cp  ${COLLECTOR_CODE_SRC}/*.md								${COLLECTOR_FOLDER}/.
	cp  ${COLLECTOR_CODE_SRC}/app/*.py							${COLLECTOR_FOLDER}/app/.
	cp  ${COLLECTOR_CODE_SRC}/app/auth/*.py						${COLLECTOR_FOLDER}/app/auth/.
	cp  ${COLLECTOR_CODE_SRC}/app/main/*.py						${COLLECTOR_FOLDER}/app/main/.
	cp  ${COLLECTOR_CODE_SRC}/app/main/plugins_code/*.py		${COLLECTOR_FOLDER}/app/main/plugins_code/.
	cp  ${COLLECTOR_CODE_SRC}/app/static/css/*.css				${COLLECTOR_FOLDER}/app/static/css/.
	cp  ${COLLECTOR_CODE_SRC}/app/static/css/*.map				${COLLECTOR_FOLDER}/app/static/css/.
	cp  ${COLLECTOR_CODE_SRC}/app/static/img/*.*				${COLLECTOR_FOLDER}/app/static/img/.
	cp  ${COLLECTOR_CODE_SRC}/app/static/js/*.js				${COLLECTOR_FOLDER}/app/static/js/.
	cp  ${COLLECTOR_CODE_SRC}/app/static/js/*.map				${COLLECTOR_FOLDER}/app/static/js/.
	cp  ${COLLECTOR_CODE_SRC}/app/templates/*.html				${COLLECTOR_FOLDER}/app/templates/.
	cp  ${COLLECTOR_CODE_SRC}/app/templates/auth/*.html			${COLLECTOR_FOLDER}/app/templates/auth/.
	cp  ${COLLECTOR_CODE_SRC}/app/templates/bootstrap/*.html	${COLLECTOR_FOLDER}/app/templates/bootstrap/.
	cp  ${COLLECTOR_CODE_SRC}/app/templates/plugins/*.html		${COLLECTOR_FOLDER}/app/templates/plugins/.
	cp  ${COLLECTOR_CODE_SRC}/service/*.py						${COLLECTOR_FOLDER}/service/.
	cp  ${COLLECTOR_CODE_SRC}/service/*.service					${COLLECTOR_FOLDER}/service/.
	cp  ${COLLECTOR_CODE_SRC}/service/README.*					${COLLECTOR_FOLDER}/service/.
	cp  ${COLLECTOR_CODE_SRC}/service/collectors/*.py			${COLLECTOR_FOLDER}/service/collectors/.
	cp  ${COLLECTOR_CODE_SRC}/service/platforms/*.py			${COLLECTOR_FOLDER}/service/platforms/.
	cp  ${COLLECTOR_CODE_SRC}/service/plugins/*.ini				${COLLECTOR_FOLDER}/service/plugins/.
	cp  ${COLLECTOR_CODE_SRC}/tools/*.py						${COLLECTOR_FOLDER}/tools/.
	cp  ${COLLECTOR_CODE_SRC}/scripts/*.sh						${COLLECTOR_FOLDER}/scripts/.
	@echo
	@echo "updating sql tools menu ..."
	@echo
	cp  ${COLLECTOR_CODE_SRC}/sql/*					${COLLECTOR_FOLDER}/sql/.
	@echo
	@echo collector completed !!!
	@echo

classes: base.html
	@echo
	@echo "***********************************"
	@echo "* Generating DB Clasess AUTOCODE  *"
	@echo "***********************************"
	@echo
	@echo "***********************************"
# 	GV Doble ejecucion eliminada por redundancia, esta en pre-requisito 
#	echo python ${SUITE_TOOLS_FOLDER}/gen_menu.py ${APP_NAME} ${SUITE_TOOLS_FOLDER} 
#	python ${SUITE_TOOLS_FOLDER}/gen_menu.py ${APP_NAME} ${SUITE_TOOLS_FOLDER}
	@echo "***********************************"
	@touch ${COLLECTOR_CODE_SRC}/*.py 
	@touch ${COLLECTOR_CODE_SRC}/models/*.py
	@cd ${SUITE_TOOLS_FOLDER}
	python ${SUITE_TOOLS_FOLDER}/populate_dev_tables.py ${SUITE_TOOLS_FOLDER}/gen_collector.ini
	python ${SUITE_TOOLS_FOLDER}/gen_models_code.py ${SUITE_TOOLS_FOLDER}/gen_collector.ini
	@cd ${COLLECTOR_TOOLS_FOLDER}
	@echo
	@ls -l ${TEMPLATES_FOLDER}/base.html
	@echo

${COLLECTOR_CODE_OUTPUT}/models.py:	${COLLECTOR_CODE_SRC}/*.py ${COLLECTOR_CODE_SRC}/models/*.py
	@echo
	@echo "***********************************"
	@echo "* Creating models.py *"
	@echo "***********************************"
	@echo
	@cat ${COLLECTOR_CODE_SRC}/models_py_header.py  		>  ${COLLECTOR_CODE_OUTPUT}/models.py
	@cat ${COLLECTOR_CODE_SRC}/models_py_header_auth.py  	>> ${COLLECTOR_CODE_OUTPUT}/models.py
	@cat ${SUITE_AUTO_MODELS}/flask_*.py  					>> ${COLLECTOR_CODE_OUTPUT}/models.py
	@cat ${COLLECTOR_CODE_SRC}/models/*.py            		>> ${COLLECTOR_CODE_OUTPUT}/models.py
	@cat ${COLLECTOR_CODE_SRC}/models_py_User_footer.py  	>> ${COLLECTOR_CODE_OUTPUT}/models.py
	@ls -l ${COLLECTOR_CODE_OUTPUT}/models.py

${COLLECTOR_CODE_OUTPUT}/orm_model.py:	${COLLECTOR_CODE_SRC}/*.py 
	@echo
	@echo "***********************************"
	@echo "* Creating orm_model.py *"
	@echo "***********************************"
	@echo
	@cat ${COLLECTOR_CODE_SRC}/orm_models_py_header.py		>  	${COLLECTOR_CODE_OUTPUT}/orm_model.py
	@cat ${SUITE_AUTO_MODELS}/ORM_model.py  			>> 	${COLLECTOR_CODE_OUTPUT}/orm_model.py
	@cp  ${SUITE_AUTO_MODELS}/ORM_model_schema.py  		${COLLECTOR_CODE_OUTPUT}/orm_model_schema.py
	@ls -l ${COLLECTOR_CODE_OUTPUT}/orm_model.py

${COLLECTOR_CODE_OUTPUT}/forms.py:	${COLLECTOR_CODE_SRC}/*.py ${COLLECTOR_CODE_SRC}/forms/*.py
	@echo
	@echo "***********************************"
	@echo "* Creating forms.py *"
	@echo "***********************************"
	@echo
	@cat ${COLLECTOR_CODE_SRC}/forms_py_header.py  		>  ${COLLECTOR_CODE_OUTPUT}/forms.py
	@cat ${SUITE_AUTO_FORMS}/*.py  					>> ${COLLECTOR_CODE_OUTPUT}/forms.py
	@cat ${COLLECTOR_CODE_SRC}/forms/*.py            		>> ${COLLECTOR_CODE_OUTPUT}/forms.py
	@ls -l ${COLLECTOR_CODE_OUTPUT}/forms.py

${COLLECTOR_CODE_SRC}/forms/*.py:
	@echo
	@echo "***********************************"
	@echo "* Creating symbolic links for ${COLLECTOR_CODE_SRC}/forms/*.py *"
	@echo "***********************************"
	@echo
	./link_functions.sh

${COLLECTOR_CODE_OUTPUT}/views.py:	${COLLECTOR_CODE_OUTPUT}/models.py
	@echo
	@echo "***********************************"
	@echo "* Creating views.py *"
	@echo "***********************************"
	@echo
	@cat ${COLLECTOR_CODE_SRC}/views_py_header.py    		>  ${COLLECTOR_CODE_OUTPUT}/views.py
	@cat ${SUITE_AUTO_INCLUDES}/models_py_imports.py	>> ${COLLECTOR_CODE_OUTPUT}/views.py
	@cat ${SUITE_AUTO_VIEWS}/*.py                		>> ${COLLECTOR_CODE_OUTPUT}/views.py
	@cat ${COLLECTOR_CODE_SRC}/views/*.py            		>> ${COLLECTOR_CODE_OUTPUT}/views.py
	@ls -l ${COLLECTOR_CODE_OUTPUT}/views.py

base:
	@echo
	@echo "***********************************"
	@echo "* Generating base ...             *"
	@echo "***********************************"

base.html:
	@echo
	@echo "***********************************"
	@echo "* Generating ${SUITE_AUTO_TEMPLATES}/base.html"
	@echo "***********************************"
	@echo
	@echo "***********************************"
	@echo python ${SUITE_TOOLS_FOLDER}/gen_menu_j2.py ${APP_NAME} ${SUITE_TOOLS_FOLDER} 
	@python ${SUITE_TOOLS_FOLDER}/gen_menu_j2.py ${APP_NAME} ${SUITE_TOOLS_FOLDER}
	@echo "***********************************"
	@echo
	ls -l ${SUITE_AUTO_TEMPLATES}/base.html
	@echo
	ls -l ${TEMPLATES_FOLDER}/base.html
	@echo

clean:
	mv models/base.py models/base.py.sav
	rm models/*.py
	mv models/base.py.sav models/base.py
	rm forms/*.py
	rm views/*.py
	
