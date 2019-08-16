# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================

from ..models       import frm_export_billing_resume
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Export_Billing_Resume', methods=['GET', 'POST'])
@login_required
def forms_Export_Billing_Resume():
    logger.debug('Enter: forms_Get_Billing_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_export_billing_resume()

    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query an conver in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Cus_Id.choices     = db.session.query(customer.Cus_Id,customer.Cus_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['Cus_Id'        ] = form.Cus_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        # Get the Selected options index for string lists
        for i in range(len(form.Cus_Id.choices)):
            if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                cus_index=i
        for i in range(len(form.Cur_Code.choices)):
            if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                cur_index=i

        if     form.submit_PDF.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "pdf"
                                ))
        if     form.submit_XLS.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "xlsx"
                                ))
        if     form.submit_CSV.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "csv"
                                ))
        if     form.submit_JSON.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "json"
                                ))
        if     form.submit_FIX.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "fix"
                                ))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            print('form validated but not submited ???')
        #return redirect(url_for('.export_Billing_Resume'))
        return redirect(url_for('.index'))

    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('export_billing_resume.html',form=form, data=session.get('data'))

# =============================================================================
from pandas.io.json             import json_normalize
import simplejson as json
import pandas
from reportlab.lib.pagesizes    import letter
from reportlab.pdfgen           import canvas
from reportlab.lib.utils        import ImageReader

def export_to_pdf(output_file,rows,Customer,From,To,Status,Currency):

    from reportlab.lib.pagesizes    import letter
    from reportlab.pdfgen           import canvas
    
    pdf_file    ="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    logo_file   ="%s/%s"%(current_app.root_path,url_for('static',filename='img/logo_emtec.png'))

    canvas = canvas.Canvas(pdf_file, pagesize=letter)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)
  
    h               = 630
    print_header    = True
    page            = 0
    count           = 0
    sum_CI          = 0
    sum_total       = 0
    previo_CI       = ''
    is_first        = True
    
    logo = ImageReader(logo_file)

    for row in rows:
        if print_header:
            page = page +1
            canvas.drawString   ( 30,750,'BILLING RESUME')
            canvas.drawString   (250,750,'SERTECHNO.COM' )
            canvas.drawString   (520,750,'PAGE:'        )
            canvas.drawString   (560,750,'%3d'%(page)   )

            canvas.rect         ( 20, 30,560,710)

            canvas.drawString   ( 30,720,'CUSTOMER:'    )
            canvas.drawString   (120,720,Customer       )
            
            canvas.drawImage(logo, 350, 660, mask='auto')
            
            canvas.drawString   ( 30,705,'FROM    :'    )
            canvas.drawString   (120,705,From)
            canvas.drawString   ( 30,690,'TO      :'    )
            canvas.drawString   (120,690,To)
            canvas.drawString   ( 30,675,'STATUS  :'    )
            canvas.drawString   (120,675,Status)
            canvas.drawString   ( 30,660,'CURRENCY:'    )
            canvas.drawString   (120,660,Currency       )

            canvas.line         ( 20,645,580,645)
            h       = 630
            canvas.drawString        ( 30,h, "ITEMS"         )
            canvas.drawString        ( 80,h, "CU"            )
            canvas.drawRightString   (280,h, "PRICE"         )
            canvas.drawRightString   (350,h, "Q"             )
            canvas.drawRightString   (410,h, "SUBTOT"        )
            canvas.drawRightString   (490,h, "XR"            )
            canvas.drawRightString   (570,h, "TOTAL"         )
            canvas.line         ( 20,615,580,615        )

            h       = 600

            print_header = False

        if row.CI_ID != previo_CI:
            if is_first == False:
                canvas.drawRightString   (570,h, "%12.2f"    % ( sum_CI  )   )
                h -= 15
            canvas.drawString   ( 30,h, "CI : %s"  % ( row.CI           )   )
            previo_CI=row.CI_ID
            sum_CI = 0
            h -= 15

        if h < 70:
            print_header = True
            canvas.line         ( 20,30,580,30)
            canvas.showPage()
            
        canvas.drawCentredString ( 30,h, "%3d"       % ( row.ITEMS           )   )
        canvas.drawString        ( 80,h, "%s"        % ( row.CU              )   )
        canvas.drawRightString   (280,h, "%12.2f"    % ( row.RATE_PRICE      )   )
        canvas.drawRightString   (350,h, "%12.2f"    % ( row.Q               )   )
        canvas.drawRightString   (410,h, "%12.2f"    % ( row.ST_AT_RATE      )   )
        canvas.drawRightString   (490,h, "%20.6f"    % ( row.BILLXR          )   )
        canvas.drawRightString   (570,h, "%12.2f"    % ( row.TOTAL_BILL_CUR  )   )
        sum_CI      += row.TOTAL_BILL_CUR
        sum_total   += row.TOTAL_BILL_CUR
        is_first = False
        
        count   +=  1
        h       -=  15
        if h < 70:
            print_header = True
            canvas.showPage()
            
    h -= 15

    canvas.drawRightString   (570,h, "%12.2f"    % ( sum_CI  )   )
    canvas.drawRightString   (570,h-15, "%12.2f"    % ( sum_total  )   )

    canvas.drawString   ( 30 ,h,'RECORDS :')
    canvas.drawRightString   (120 ,h,"%04d"%( count ) )
 
    canvas.save()


def export_to_xls(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s.json"%(output_file)
    export_to_json(json_file,rows,Customer,From,To,Status,Currency)
    
    json_file   ="%s/%s"%(current_app.root_path, url_for('static',filename='tmp/%s.json'%(output_file)))
    
    with open(json_file) as data_file:    
        d= json.load(data_file)  

    df1 = json_normalize(d, 'detail').assign(**d['header'])
        
    xlsx_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    
    df1.to_excel(xlsx_file,'Sheet 1')    

def export_to_csv(output_file,rows,Customer,From,To,Status,Currency):
    cvs_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(cvs_file,"w")

    f.write("H,Customer,From,To,Status,Currency\n")
    f.write("H,%s,%s,%s,%s,%s\n"%(Customer,From,To,Status,Currency))
    f.write("D,Records,CU,Rate,Q,Subtotal,XR,Total\n")
    count = 0
    for row in rows:
        f.write("D,%s,%s,%s,%s,%s,%s,%s\n"%(row.ITEMS,row.CU,row.RATE_PRICE,row.Q,row.ST_AT_RATE,row.BILLXR,row.TOTAL_BILL_CUR))
        count += 1
    f.write("T,%d\n"%(count))
    f.close()


def export_to_json(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(json_file,"w")
    
    dict = {}
    dict.update({'header':{}})
    dict['header'].update({'customer':Customer})
    dict['header'].update({'from':From})
    dict['header'].update({'to':To})
    dict['header'].update({'status':Status})
    dict['header'].update({'currency':Currency})
    dict.update({'detail':[]})
    count = 0
    for row in rows:
        dict['detail'].append({})
        dict['detail'][count].update( {    'items':row.ITEMS, 'cu':row.CU, 'price':row.RATE_PRICE, 'q':row.Q, 'subtotal':row.ST_AT_RATE,\
                                    'xr':row.BILLXR, 'total':row.TOTAL_BILL_CUR \
                                })
        count += 1
    dict['header'].update({'count':count})
    jsonarray = json.dumps(dict)
    
    f.write(jsonarray)

    f.close()

def export_to_fix(output_file,rows,Customer,From,To,Status,Currency):
    fix_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))

    f=open(fix_file,"w")

    f.write("H%06d%-45s%-10s%-10s%-45s%-45s*\n"%(0,Customer,From,To,Status,Currency))
    count = 0
    for row in rows:
        f.write("D%06d%-45s%020.6f%020.6f%020.6f%020.6f%020.6f%010d*\n"%(row.ITEMS,row.CU,row.RATE_PRICE,row.Q,row.ST_AT_RATE,row.BILLXR,row.TOTAL_BILL_CUR,0))
        count += 1
    f.write("T%06d%0155d*\n"%(count,0))
    f.close()

import simplejson as json

@main.route('/export/Billing_Resume', methods=['GET','POST'])
@login_required
def export_Billing_Resume():
    logger.debug('Enter: Export_Billing_Resume()')
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Format          =  request.args.get('Format',None,type=str)
    # Get Actual Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Billing_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    rows =  db.engine.execute(query).fetchall()

    # Aqui hace la conversion 
    output_file = "Billing_Resume_%d_%s_%s_%s.%s"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Format)
    if      Format == 'pdf':
        export_to_pdf(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'xlsx':
        export_to_xls(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'csv':
        export_to_csv(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'json':
        export_to_json(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'fix':
        export_to_fix(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    else:
        pass    
    
    # Aqui debe enviar el archivo a la PC
    #return ("<H1>Envio archivo %s a la PC</H1>"%(output_file_name))
    
    href = url_for('static',filename="tmp/%s"%output_file)
    
    return render_template('report_export_billing_resume.html',output_file=output_file,href=href)

