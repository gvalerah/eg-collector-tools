MYPWD=$(pwd)
ROOT=/home/gvalera/collector
TOOLS=/home/gvalera/GIT/EG-Collector-Tools
CODE=$TOOLS/code
SRC=$CODE/src
FUNCTIONS=$SRC/functions
FORMS=$SRC/forms
VIEWS=$SRC/views
TEMPLATES=$SRC/templates

echo Starting in $MYPWD ...
echo Changing to $FUNCTIONS ...

cd $FUNCTIONS
for dir in ls *
do
    if [ -d "$dir" ]; then
        echo function: $dir

        cd $dir
        for file in *.html
        do
            echo "  template :" $file
            #unlink $TEMPLATES/$file
            ln -f -s $FUNCTIONS/$dir/$file $TEMPLATES/$file
        done

        for file in *.py
        do
	    #echo procesando $file
            if [[ $file == 'frm_'* ]]; then
                echo "  form     :" $file
                #echo ln -f -s $FUNCTIONS/$dir/$file $FORMS/$file
                #unlink $FORMS/$file
                ln -f -s $FUNCTIONS/$dir/$file $FORMS/$file
            else
                if [[ $file == 'view_'* ]]; then
                    echo "  view     :" $file                
                    #echo ln -f -s $FUNCTIONS/$dir/$file $VIEWS/$file                
                    #unlink $VIEWS/$file
                    ln -f -s $FUNCTIONS/$dir/$file $VIEWS/$file                
                fi
            fi
        done

        cd ..
        
    fi
done
echo returning to $MYPWD ...
cd $MYPWD

