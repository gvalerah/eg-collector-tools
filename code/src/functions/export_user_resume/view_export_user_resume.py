# =============================================================================
# View for Get Billing Resume from DB
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# =============================================================================
import  simplejson as json
import  pandas
from    pandas.io.json             import json_normalize
from    flask                      import send_file
from    babel.numbers  import format_number, format_decimal, format_percent
from    emtec.collector.forms       import frm_export_User_Resume

@main.route('/forms/Export_User_Resume', methods=['GET', 'POST'])
@login_required
def forms_Export_User_Resume():
    logger.debug('Enter: forms_Export_User_Resume()'%())
    collectordata=get_collectordata()

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_export_User_Resume()

    # 20210422 GV cambio a rutina estandar USERCAN = db.get_user_cost_centers(current_user.id) 
    USERCAN = db.get_user_cost_centers(current_user.id,) 
    rows = db.session.query(    func.count(user_resumes.CI_CC_Id).label('RECORDS'),
                        user_resumes.CI_CC_Id,
                        user_resumes.CR_Date_From,
                        user_resumes.CR_Date_To,
                        user_resumes.CIT_Status,
                        user_resumes.Cur_Code,
                        user_resumes.CC_Description
                    ).filter(     user_resumes.CI_CC_Id.in_(USERCAN)
                    ).group_by(   user_resumes.CI_CC_Id,
                                user_resumes.CR_Date_From,
                                user_resumes.CR_Date_To,
                                user_resumes.CIT_Status,
                                user_resumes.Cur_Code,
                                user_resumes.CC_Description
                    ).order_by(   user_resumes.CI_CC_Id,
                                user_resumes.CR_Date_From,
                                user_resumes.CR_Date_To,
                                user_resumes.CIT_Status,
                                user_resumes.Cur_Code
                    ).all()

    # Load Statuses
    statuses=cit_status.query.all()
    dstatuses={}
    for s in statuses:
        dstatuses[s.CIT_Status]=s.Value
        
    currencies=currency.query.all()
    dcurrencies={}
    for c in currencies:
        dcurrencies[c.Cur_Code]=c.Cur_Name
    
    # Load Currency Names

    export_choices = []
    for row in rows:
        option="%s_%s_%s_%s_%s_%s"%(row.CI_CC_Id,row.CR_Date_From,row.CR_Date_To,row.CIT_Status,row.Cur_Code,row.CC_Description)
        value ="%s from %s to %s status=%s currency=%s"%(row.CC_Description,row.CR_Date_From,row.CR_Date_To,dstatuses[row.CIT_Status],dcurrencies[row.Cur_Code])
        export_choices.append((option,value))
    
    form.Export.choices   = export_choices

    if form.validate_on_submit():

        data=form.Export.data.split("_")
        print("data=",data)
        
        CC_Code=db.session.query(cost_center.CC_Code).filter(cost_center.CC_Id==data[0]).one()
        
        if     form.submit_PDF.data:
            return redirect(url_for('.export_User_Resume',
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "pdf"
                                ))
        elif     form.submit_XLS.data:
            return redirect(url_for('.export_User_Resume',
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "xlsx"
                                ))
        elif     form.submit_CSV.data:
            return redirect(url_for('.export_User_Resume',
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "csv"
                                ))
        elif     form.submit_JSON.data:
            return redirect(url_for('.export_User_Resume',
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "json"
                                ))
        elif     form.submit_FIX.data:
            return redirect(url_for('.export_User_Resume',
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "fix"
                                ))
        elif     form.submit_Delete.data:
            return redirect(url_for('.export_User_Resume',
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "del"
                                ))
        elif   form.submit_Cancel.data:
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support')
        return redirect(url_for('.index'))
        
    return render_template(
        'export_user_resume.html',
        form=form
        )

# =============================================================================

# **********************************************************************


def export_user_resume_to_pdf(  output_file,rows,Customer,From,To,Status,Currency,
                    CC_Id=0,Pla_Id=0,CC_Name='',Pla_Name='',CC_Code=''):
    # this structure is to conditionaly import report functions
    report_name = 'rpt-ur-001'
    if report_name == 'rpt-ur-001':
        from emtec.collector.custom.rpt_ur_001 import export_to_pdf
    pdf_file = export_to_pdf(
                current_app,
                output_file,
                rows,
                Customer,
                From,
                To,
                Status,
                Currency,
                CC_Id,
                Pla_Id,
                CC_Name,
                Pla_Name,
                CC_Code
                )
    return pdf_file
    
# **********************************************************************

def export_user_resume_to_xls(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s.json"%(output_file)
    export_user_resume_to_json(json_file,rows,Customer,From,To,Status,Currency)
    
    json_file   ="%s%s"%(current_app.root_path, url_for('static',filename='tmp/%s.json'%(output_file)))
    
    with open(json_file) as data_file:    
        d= json.load(data_file)  

    df1 = json_normalize(d, 'detail').assign(**d['header'])
        
    xlsx_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    
    df1.to_excel(xlsx_file,'Sheet 1')
    
    print("%s: output_file = %s"%('export_to_xlsx',output_file))
    print("%s: json_file   = %s"%('export_to_xlsx',json_file))
    print("%s: xlsx_file   = %s"%('export_to_xlsx',xlsx_file))
       
    return xlsx_file    

def export_user_resume_to_csv(output_file,rows,Customer,From,To,Status,Currency,precision=8):
    cvs_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(cvs_file,"w")

    f.write("H,Customer,From,To,Status,Currency\n")
    f.write("H,%s,%s,%s,%s,%s\n"%(Customer,From,To,Status,Currency))
    f.write("D,Records,CU,Rate,Q,Subtotal,XR,Total\n")
    count = 0
    for row in rows:
        f.write ("D,%s,%s,%s,%s,%s,%s,%s\n"%
                    (   row.CIT_Count, 
                        row.CU_Description, 
                        round(row.Rat_Price,precision), 
                        round(row.CR_Quantity_at_Rate,precision), 
                        round(row.CR_ST_at_Rate_Cur,precision), 
                        round(row.CR_Cur_XR,precision),
                        round(row.CR_ST_at_Cur,precision)
                    )
                )
        count += 1
    f.write("T,%d\n"%(count))
    f.close()
    return cvs_file

RAT_PERIOD_DESCRIPTIONS={1:"HOUR",2:"DAY",3:"MONTH"}

# field,cast,precision,map,error
record_structure = {
    'header': {
        'customer': ('Customer',str,None,None,None),
        'from'    : ('From'    ,str,None,None,None),
        'to'      : ('To'      ,str,None,None,None),
        'status'  : ('Status'  ,str,None,None,None),
        'currency': ('Currency',str,None,None,None),
    },
    'detail': {
        'ccCode'                : ('CI_CC_Id'           ,int  ,None,None                   ,0),
        'ccDescription'         : ('CC_Description'     ,str  ,None,None                   ,'ERROR'),
        'ciName'                : ('CI_Name'            ,str  ,None,None                   ,'ERROR'),
        'cuDescription'         : ('CU_Description'     ,str  ,None,None                   ,'ERROR'), 
        'items'                 : ('CIT_Count'          ,int  ,None,None                   ,0), 
        'rate'                  : ('Rat_Price'          ,float,8   ,None                   ,0), 
        'mu'                    : ('Rat_MU_Code'        ,str  ,None,None                   ,'ERROR'), 
        'rateCurrency'          : ('Rat_Cur_Code'       ,str  ,None,None                   ,'ERROR'), 
        'ratePeriodDescription' : ('Rat_Period'         ,int  ,None,RAT_PERIOD_DESCRIPTIONS,'ERROR'), 
        'resumeQuantityAtRate'  : ('CR_Quantity_at_Rate',float,8   ,None                   ,0.0),
        'totalAtCurrency'       : ('CR_ST_at_Rate_Cur'  ,float,8   ,None                   ,0.0)
    }
}

def row_to_dict(row,structure):
    d = {}
    for name in structure:
        Field,Type,Precision,Map,Error = structure[name]
        value = getattr(row,Field)
        
        if Type == int:
            if Map is None:
                try:
                    value = int(value)
                except:
                    value = Error
            else:
                try:
                    value = Map.get(int(value),Error)
                except:
                    value = Error
        elif Type == float:
            try:
                if Precision is not None:
                    value = float(value)
                else:
                    value = round(float(value,Precision))
            except:
                value = Error
        elif Type == str:
            value=str(value)
        else:
            value = Error
        d.update({name:value})
    return d

def export_user_resume_to_json(output_file,rows,Customer,From,To,Status,Currency,precision=8):
    json_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(json_file,"w")
    
    mydict = {}
    mydict.update({'header':{}})
    mydict['header'].update({'customer':Customer})
    mydict['header'].update({'from':From})
    mydict['header'].update({'to':To})
    mydict['header'].update({'status':Status})
    mydict['header'].update({'currency':Currency})
    mydict.update({'detail':[]})
    count = 0
    for row in rows:
        mydict['detail'].append(row_to_dict(row,record_structure['detail']))
        '''
        mydict['detail'].append({})

        mydict['detail'][count].update( {
            'ccCode'                : row.CI_CC_Id,
            'ccDescription'         : row.CC_Description,
            'ciName'                : row.CI_Name,
            'cuDescription'         : row.CU_Description, 
            'items'                 : row.CIT_Count, 
            'mu'                    : row.Rat_MU_Code, 
            'rateCurrency'          : row.Rat_Cur_Code, 
            'ratePeriodDescription' : RAT_PERIOD_DESCRIPTIONS.get(row.Rat_Period,"ERROR"), 
            'resumeQuantityAtRate'  : round(row.CR_Quantity_at_Rate,precision),
            'totalAtCurrency'       : round(row.CR_ST_at_Rate_Cur,precision)
            })
        
        count += 1
        '''
    jsonarray = json.dumps(mydict)
    
    f.write(jsonarray)

    f.close()
    return json_file

def export_user_resume_to_fix(output_file,rows,Customer,From,To,Status,Currency):
    fix_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))

    f=open(fix_file,"w")

    f.write("H%06d%-60s%-10s%-10s%-45s%-45s*\n"%(0,Customer,From,To,Status,Currency))
    count = 0
    for row in rows:
        f.write ("D%06d%-60s%020.8f%020.8f%020.8f%020.8f%020.8f%010d*\n"%\
                    (row.CIT_Count, row.CU_Description, row.Rat_Price, row.CR_Quantity,row.CR_ST_at_Rate_Cur,row.CR_Cur_XR,row.CR_ST_at_Cur,0)\
                )
        count += 1
    f.write("T%06d%0170d*\n"%(count,0))
    f.close()
    return fix_file

def delete_user_resume(output_files,Customer,From,To,Status,Currency):
    result = False
    try:
        # deletes all matching output files
        for output_file in output_files:
            delete_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
            logger.debug(f"deleting file system file: {delete_file}")
            if os.path.exists(delete_file):
                os.remove(delete_file)
        logger.debug(f"delete_user_resume: will delete = {Customer},{From},{To},{Status},{Currency}")
        result = db.Delete_User_Resume(Customer,From,To,Status,Currency)
        logger.debug(f"delete_user_resume: result = {result}")
    except Exception as e:
        logger.error(f"delete_user_resume: Exception: {str(e)}")
        flash(f"delete_user_resume: Exception: {str(e)}")
        result = False
    return result

@main.route('/export/User_Resume', methods=['GET','POST'])
@login_required
def export_User_Resume():
    logger.debug('Enter: Export_User_Resume()')
    CC_Id           =  request.args.get('CC_Id',None,type=int)
    CC_Code         =  request.args.get('CC_Code',None,type=str)
    CC_Description  =  request.args.get('CC_Description',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Format          =  request.args.get('Format',None,type=str)

    # Aqui hace la conversion 
    output_file = "CR_%s_%s_%s_%s_%s.%s"%(CC_Code,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,Format)
    if Format == 'del':
        output_files=[]
        for Format in ['pdf','xlsx','csv','json','fix']:
            output_files.append("CR_%s_%s_%s_%s_%s.%s"%(CC_Code,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,Format))
        if delete_user_resume(output_files,current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code):
            flash(f"User Resume deleted.")
    else:
        # Get Actual Data from Database
        # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
        return_file = None
        rows = []
        rows = db.Get_User_Resume(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
        if len(rows):
            #flash(f"current_user={current_user}")
            #flash(f"current_user.cost_center={current_user.cost_center}")
            Customer = current_user.cost_center.CC_Description
            if      Format == 'pdf':
                return_file=export_user_resume_to_pdf(output_file,rows,Customer,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
            elif    Format == 'xlsx':
                return_file=export_user_resume_to_xls(output_file,rows,Customer,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
            elif    Format == 'csv':
                return_file=export_user_resume_to_csv(output_file,rows,Customer,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
            elif    Format == 'json':
                return_file=export_user_resume_to_json(output_file,rows,Customer,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
            elif    Format == 'fix':
                return_file=export_user_resume_to_fix(output_file,rows,Customer,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
            else:
                pass    

        if return_file is not None:
            if os.path.exists(return_file):
                # Aqui debe enviar el archivo a la PC
                return send_file(return_file,as_attachment=True,attachment_filename=output_file)
            else:
                flash(f"Warning: '{return_file}' does not exist.")
        else:
            flash(f"Warning: No exported data file available.")
    
    return redirect(url_for('.index'))

