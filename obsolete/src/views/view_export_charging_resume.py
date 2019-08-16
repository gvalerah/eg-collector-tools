# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================

from ..models       import frm_export_Charging_Resume
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Export_Charging_Resume', methods=['GET', 'POST'])
@login_required
def forms_Export_Charging_Resume():
    logger.debug('Enter: forms_Export_Charging_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_export_Charging_Resume()

    query = "SELECT COUNT(*) AS RECORDS,Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,Cus_Name FROM Charge_Resumes "\
                "GROUP BY Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,Cus_Name "\
                "ORDER BY Cus_Name,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code"
                
    rows=db.engine.execute(query).fetchall()

    # Load Statuses
    statuses=cit_status.query.all()
    dstatuses={}
    for s in statuses:
        dstatuses[s.CIT_Status]=s.Value
        
    currencies=currency.query.all()
    dcurrencies={}
    for c in currencies:
        dcurrencies[c.Cur_Code]=c.Cur_Name
    
    #print("statuses",statuses)
    #print("currencies",currencies)
    #print("dstatuses",dstatuses)
    #print("dcurrencies",dcurrencies)
    
    
    # Load Currency Names


    export_choices = []
    for row in rows:
        option="%s_%s_%s_%s_%s_%s"%(row.Cus_Id,row.CR_Date_From,row.CR_Date_To,row.CIT_Status,row.Cur_Code,row.Cus_Name)
        print("option split=",option.split("_"))
        value ="%s from %s to %s status=%s currency=%s"%(row.Cus_Name,row.CR_Date_From,row.CR_Date_To,dstatuses[row.CIT_Status],dcurrencies[row.Cur_Code])
        export_choices.append((option,value))
     
     
       

    #print("export_choices=",export_choices)



    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    #query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query an conver in list for further use in choices selection
    #export_choices = [row.Cur_Code for row in query.all()]

    form.Export.choices   = export_choices

    if form.validate_on_submit():

        data=form.Export.data.split("_")
        print("data=",data)
        if     form.submit_PDF.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "pdf"
                                ))
        if     form.submit_XLS.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "xlsx"
                                ))
        if     form.submit_CSV.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "csv"
                                ))
        if     form.submit_JSON.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "json"
                                ))
        if     form.submit_FIX.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "fix"
                                ))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            print('form validated but not submited ???')
        return redirect(url_for('.index'))


    return render_template('export_charging_resume.html',form=form)

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

        if row.CI_Id != previo_CI:
            if is_first == False:
                canvas.drawRightString   (570,h, "%12.2f"    % ( sum_CI  )   )
                h -= 15
            canvas.drawString   ( 30,h, "CI : %s"  % ( row.CI_Name           )   )
            previo_CI=row.CI_Id
            sum_CI = 0
            h -= 15

        if h < 70:
            print_header = True
            canvas.line         ( 20,30,580,30)
            canvas.showPage()
            
        canvas.drawCentredString ( 30,h, "%3d"       % ( row.CIT_Count          )   )
        canvas.drawString        ( 80,h, "%s"        % ( row.CU_Description     )   )
        canvas.drawRightString   (280,h, "%12.2f"    % ( row.Rat_Price          )   )
        canvas.drawRightString   (350,h, "%12.2f"    % ( row.CR_Quantity        )   )
        canvas.drawRightString   (410,h, "%12.2f"    % ( row.CR_ST_at_Rate_Cur  )   )
        canvas.drawRightString   (490,h, "%20.6f"    % ( row.CR_Cur_XR          )   )
        canvas.drawRightString   (570,h, "%12.2f"    % ( row.CR_ST_at_Cur       )   )
        sum_CI      += row.CR_ST_at_Cur
        sum_total   += row.CR_ST_at_Cur
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
    return pdf_file


def export_to_xls(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s.json"%(output_file)
    export_to_json(json_file,rows,Customer,From,To,Status,Currency)
    
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

def export_to_csv(output_file,rows,Customer,From,To,Status,Currency):
    cvs_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(cvs_file,"w")

    f.write("H,Customer,From,To,Status,Currency\n")
    f.write("H,%s,%s,%s,%s,%s\n"%(Customer,From,To,Status,Currency))
    f.write("D,Records,CU,Rate,Q,Subtotal,XR,Total\n")
    count = 0
    for row in rows:
        f.write ("D,%s,%s,%s,%s,%s,%s,%s\n"%\
                    (row.CIT_Count, row.CU_Description, row.Rat_Price, row.CR_Quantity, row.CR_ST_at_Rate_Cur, row.CR_Cur_XR,row.CR_ST_at_Cur)\
                )
        count += 1
    f.write("T,%d\n"%(count))
    f.close()
    return cvs_file
    
"""
        canvas.drawCentredString ( 30,h, "%3d"       % ( row.CIT_Count          )   )
        canvas.drawString        ( 80,h, "%s"        % ( row.CU_Description     )   )
        canvas.drawRightString   (280,h, "%12.2f"    % ( row.Rat_Price          )   )
        canvas.drawRightString   (350,h, "%12.2f"    % ( row.CR_Quantity        )   )
        canvas.drawRightString   (410,h, "%12.2f"    % ( row.CR_ST_at_Rate_Cur  )   )
        canvas.drawRightString   (490,h, "%20.6f"    % ( row.CR_Cur_XR          )   )
        canvas.drawRightString   (570,h, "%12.2f"    % ( row.CR_ST_at_Cur       )   )    
"""    
    

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
        dict['detail'][count].update( {    'items':row.CIT_Count, 'cu':row.CU_Description, 'price':row.Rat_Price, \
                                        'q':row.CR_Quantity, 'subtotal':row.CR_ST_at_Rate_Cur,\
                                        'xr':row.CR_Cur_XR, 'total':row.CR_ST_at_Cur \
                                })
        count += 1
    dict['header'].update({'count':count})
    jsonarray = json.dumps(dict)
    
    f.write(jsonarray)

    f.close()
    return json_file

def export_to_fix(output_file,rows,Customer,From,To,Status,Currency):
    fix_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))

    f=open(fix_file,"w")

    f.write("H%06d%-45s%-10s%-10s%-45s%-45s*\n"%(0,Customer,From,To,Status,Currency))
    count = 0
    for row in rows:
        f.write ("D%06d%-45s%020.6f%020.6f%020.6f%020.6f%020.6f%010d*\n"%\
                    (row.CIT_Count, row.CU_Description, row.Rat_Price, row.CR_Quantity,row.CR_ST_at_Rate_Cur,row.CR_Cur_XR,row.CR_ST_at_Cur,0)\
                )
        count += 1
    f.write("T%06d%0155d*\n"%(count,0))
    f.close()
    return fix_file

import simplejson as json
from flask import send_file

@main.route('/export/Charging_Resume', methods=['GET','POST'])
@login_required
def export_Charging_Resume():
    logger.debug('Enter: Export_Charging_Resume()')
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
    query="CALL Get_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    rows =  db.engine.execute(query).fetchall()

    # Aqui hace la conversion 
    output_file = "CR_%d_%s_%s_%s_%s.%s"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,Format)
    if      Format == 'pdf':
        return_file=export_to_pdf(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'xlsx':
        return_file=export_to_xls(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'csv':
        return_file=export_to_csv(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'json':
        return_file=export_to_json(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'fix':
        return_file=export_to_fix(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    else:
        pass    
    
    # Aqui debe enviar el archivo a la PC
    print("%s: return_file   = %s"%('export_Charging_Resume',return_file))
    print("%s: att name      = %s"%('export_Charging_Resume',output_file))
    return send_file(return_file,as_attachment=True,attachment_filename=output_file)

