#/bin/bash

CODE_FOLDER=/home/gvalera/collector/tools/code
SRC_FOLDER=$CODE_FOLDER/src
FUNCTIONS_FOLDER=$SRC_FOLDER/functions
SRC_VIEWS=$SRC_FOLDER/views
SRC_FORMS=$SRC_FOLDER/forms
SRC_TEMPLATES=$SRC_FOLDER/templates

cd $FUNCTIONS_FOLDER

for d in $(ls -d *)
do
    echo inspecting $d
    cd $FUNCTIONS_FOLDER/$d
    for f in $(ls view_*.py > /dev/null)
        do
            echo "   got view file" $f
            ln -s -f $FUNCTIONS_FOLDER/$d/$f $SRC_VIEWS/$f
        done    
    for f in $(ls frm_*.py > /dev/null)
        do
            echo "   got form file" $f
            ln -s -f $FUNCTIONS_FOLDER/$d/$f $SRC_FORMS/$f
        done    
    for f in $(ls *.html > /dev/null)
        do
            echo "   got template file" $f
            ln -s -f $FUNCTIONS_FOLDER/$d/$f $SRC_TEMPLATES/$f
        done    
done

