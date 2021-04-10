# =============================================================================
# View for Import Cost Centers
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# =============================================================================

import os
from emtec.collector.forms       import frm_import_cost_centers
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField

#UPLOAD_FOLDER = '/path/to/the/uploads'
UPLOAD_FOLDER = '/tmp'
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS=set(['xls'])

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#--------------------------------------------------------------------------
#from openpyxl import load_workbook
import os
import json
# Libreria para leer formato XLS
from xlrd import open_workbook
from time import strptime,strftime
# Import create_engine function
from sqlalchemy import create_engine
from sqlalchemy import text

def load_columns(sheet):
    columns={}
    for col in range(sheet.ncols):
        columns.update({sheet.cell(0,col).value:col})
    return columns
    
def load_Cost_Centers_from_XLS(file):
    logger.debug('%s: Enter: load_Cost_Centers_from_XLS(%s)'%(__name__,file))

    updates=0
    additions=0
    errors=0

    DATA={}
    DATA.update({'metadata':{},'entities':[]})
    
    name = file.split('.')
    
    wb = open_workbook(file)
    nsheets=0

    DATA['metadata'] = {'name':name}
    for s in wb.sheets():
        COLUMNS={}
        COLUMNS=load_columns(s)

        if 'Cost_Centers' in s.name:
            for row in range(1,s.nrows):
                DATA['entities'].append({ 
                            'CC_Id':            int(s.cell(row,COLUMNS['CC_Id']).value),
                            'CC_Code':          s.cell(row,COLUMNS['CC_Code']).value,
                            'CC_Description':   s.cell(row,COLUMNS['CC_Description']).value,
                            'Cur_Code':         s.cell(row,COLUMNS['Cur_Code']).value,
                            'CC_Parent_Code':   s.cell(row,COLUMNS['CC_Parent_Code']).value,
                            })
    logger.debug("%s: CCs = %d"%(__name__,len(DATA['entities'])))
    
    DATA['metadata'].update({'count':len(DATA['entities'])})

    for cc in DATA['entities']:    
        logger.debug("Importing CC: %s %s"%(cc['CC_Code'],cc['CC_Description']))
        try:
            id = db.session.query(cost_center.CC_Id).filter(cost_center.CC_Code==cc['CC_Code']).scalar()
            if id:
                logger.debug("Existent CC",id,"will be updated");
                c=cost_center(id,cc['CC_Code'],cc['CC_Description'],cc['Cur_Code'],cc['CC_Parent_Code'])
                try:
                    db.session.merge(c)
                    db.session.commit()
                    updates+=1
                except Exception as e:
                    errors+=1              
                    flash("fail updating CC:",e)
                logger.debug("c=",c)                
            else:
                logger.debug("Add new CC")
                c=cost_center(0,cc['CC_Code'],cc['CC_Description'],cc['Cur_Code'],cc['CC_Parent_Code'])
                
                logger.debug("c=",c)                
                try:
                    db.session.add(c)
                    db.session.commit()
                    additions+=1
                except Exception as e:                
                    errors+=1              
                    flash("fail updating CC:",e)
        except Exception as e:
            errors+=1              
            flash("fail querying for CC:",e)
        
    return (len(DATA['entities']),additions,updates,errors)

#--------------------------------------------------------------------------
@main.route('/forms/Import_Cost_Centers', methods=['GET', 'POST'])
@login_required
def forms_Import_Cost_Centers():
    logger.debug('%s: Enter: forms_Import_Cost_Centers()'%(__name__))
    logger.debug('%s: UPLOAD_FOLDER=%s'%(__name__,UPLOAD_FOLDER))

    session['data'] =  { }

    form = frm_import_cost_centers()
    logger.debug('%s: form = %s'%(__name__,form))        
    
    if form.validate_on_submit():
        f=form.Import.data
        filename=secure_filename(f.filename)
        logger.debug('%s: filename is %s'%(__name__,filename))        
        f.save(os.path.join(
            UPLOAD_FOLDER,  filename
        ))        
        logger.debug('%s: will call load_Cost_Centers_from_XLS with UPLOAD FOLDER=%s'%(__name__,UPLOAD_FOLDER))        
        result=load_Cost_Centers_from_XLS("%s/%s"%(UPLOAD_FOLDER,filename))
        logger.debug('%s: result type is %s'%(__name__,type(result)))        
        logger.debug('%s: will render template import_cost_centers_execution.html'%(__name__,type(result)))        
        return render_template('import_cost_centers_execution.html',filename=filename,result=result)
        """
        if     form.submit_Import.data:
            print("************")
            print("form.submit_Import.data",form.submit_import.data);
            flash("form.submit_Import.data="%form.submit_import.data);
            print("************")
            return redirect(url_for('.import_Cost_Centers'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.index'))
        """
    logger.debug('%s: will render template import_cost_centers.html'%(__name__))        
    return render_template('import_cost_centers.html',form=form)
    
    
"""    
@main.route('/import/Cost_Centers', methods=['GET','POST'])
@login_required
def import_Cost_Centers():
    #return send_file(return_file,as_attachment=True,attachment_filename=output_file)
    return '<H1>export_User_Resume</H1>'
"""    
"""    
@main.route('/import/Cost_Centers', methods=['GET','POST'])
#def upload_file():
def import_Cost_Centers():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return
" ""
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''    
"""    
"""
from flask import send_from_directory

#@app.route('/uploads/<filename>')
@main.route('/uploads/<filename>')
def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return send_from_directory(UPLOAD_FOLDER, filename)
"""    
