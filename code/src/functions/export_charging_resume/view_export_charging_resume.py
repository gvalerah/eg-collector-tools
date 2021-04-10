# ======================================================================
# View for Get Billing Resume from DB
# (c) Sertechno 2018/2019/2020
# GLVH @ 2020-04-01
# ======================================================================

import  simplejson              as json
import  pandas
from    pandas.io.json          import json_normalize
from    reportlab.lib.pagesizes import letter
from    reportlab.pdfgen        import canvas
from    reportlab.lib.utils     import ImageReader
from    flask                   import send_file
from    babel.numbers           import format_number
from    babel.numbers           import format_decimal
from    babel.numbers           import format_percent
from    emtec.collector.forms   import frm_export_Charging_Resume
from    emtec.class_report      import *
from    collections             import namedtuple
from    pprint                  import pprint

@main.route('/forms/Export_Charging_Resume', methods=['GET', 'POST'])
@login_required
def forms_Export_Charging_Resume():
    function_name=sys._getframe().f_code.co_name
    logger.debug('%s: Enter'%(function_name))
    collectordata=get_collectordata()

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_export_Charging_Resume()
    
    rows = db.session.query( 
            func.count(charge_resume.Cus_Id).label('RECORDS'),
            charge_resume.Cus_Id,
            charge_resume.CR_Date_From,
            charge_resume.CR_Date_To,
            charge_resume.CIT_Status,
            charge_resume.Cur_Code,
            charge_resume.Cus_Name
            ).group_by( charge_resume.Cus_Id,
                        charge_resume.CR_Date_From,
                        charge_resume.CR_Date_To,
                        charge_resume.CIT_Status,
                        charge_resume.Cur_Code,
                        charge_resume.Cus_Name
            ).order_by( charge_resume.Cus_Name,
                        charge_resume.CR_Date_From,
                        charge_resume.CR_Date_To,
                        charge_resume.CIT_Status,
                        charge_resume.Cur_Code
            )
    
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
        option="%s_%s_%s_%s_%s_%s"%(
                row.Cus_Id,
                row.CR_Date_From,
                row.CR_Date_To,
                row.CIT_Status,
                row.Cur_Code,
                row.Cus_Name
            )
        value ="%s from %s to %s status=%s currency=%s (%s)"%(
                row.Cus_Name,
                row.CR_Date_From,
                row.CR_Date_To,
                dstatuses[row.CIT_Status],
                dcurrencies[row.Cur_Code],
                row.RECORDS
            )
        export_choices.append((option,value))

    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    #query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query an conver in list for further use in choices selection
    #export_choices = [row.Cur_Code for row in query.all()]

    ccs=db.session.query(Cost_Centers).all()
    cc_choices=[(":","")]
    for cc in ccs:
        cc_choices.append(("%s:%s"%(cc.CC_Id,cc.CC_Code),cc.CC_Description))

    platforms=db.session.query(Platforms).all()
    platform_choices=[(0,"")]
    for platform in platforms:
        platform_choices.append((platform.Pla_Id,platform.Pla_Name))

    form.Export.choices   = export_choices
    form.CC.choices       = cc_choices
    form.Platform.choices = platform_choices
    
    if form.validate_on_submit():

        data=form.Export.data.split("_")

        if     form.submit_PDF.data:
            CC_Name=Pla_Name=''
            for cc,name in form.CC.choices:
                if cc == form.CC.data:
                    CC_Name=name
            for pla,name in form.Platform.choices:
                if platform == form.Platform.data:
                    Pla_Name=name
            print("CC =",CC_Name,"Pla =",Pla_Name)
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "pdf",
                                CC_Id           = form.CC.data.split(':')[0],
                                CC_Code         = form.CC.data.split(':')[1],
                                Pla_Id          = form.Platform.data,
                                CC_Name         = CC_Name,
                                Pla_Name        = Pla_Name
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
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            pass
            #print('form validated but not submited ???')
        return redirect(url_for('.index'))


    return render_template(
        'export_charging_resume.html',
        form=form,
        collectordata=collectordata
        )

# ======================================================================

def prepare_report_header(r):
    
    # Setup Report Header
    r.Header.box.visible=False
    # Horizontal subwindows
    header_dimensions=[(0,6),(6,2),(8,1)]
    # Horizontal subwindows for first Header SubWindow
    r.pdf_create_subwindows_details   (r.Header, dimensions=header_dimensions,box=True,horizontal=True)
    header_dimensions=[0.25,0.50,0.25]
    r.pdf_create_subwindows_relatives (r.Header.subwindows[0], dimensions=header_dimensions,box=True)
    # ....+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8
    # ....+6....5....+....+....+...9....5....5....5....5....+....1
    # "%3d"    3   4  0-  3 % ( row.CIT_Count          )   )
    # "%s"     45 46  4- 49 % ( row.CU_Description     )   )
    # "%12.2f" 12 13 50- 62 % ( row.Rat_Price          )   )
    # "%12.2f" 12 13 63- 75 % ( row.CR_Quantity        )   )
    # "%12.2f" 12 13 76- 88 % ( row.CR_ST_at_Rate_Cur  )   )
    # "%20.6f" 20 21 89-109 % ( row.CR_Cur_XR          )   )
    # "%12.2f" 12 13 110-122 % ( row.CR_ST_at_Cur       )   )    
    
    # Max witdh should be in range 60 @ 12picas / 90 @ 8picas
    details=[4,20,12,12,12,18,12]
    # widths will be scaled to 8/12 = 2/3 because of font size = 8
    #print("details=",details)
    for i in range(len(details)):
        details[i]*=(2/3) 
    #print("details=",details)
    r.pdf_create_subwindows_widths (r.Header.subwindows[1], widths=details, box=True)
        
    # Poblar cabecera
    H=r.create_record("Cabecera")
    
    H.add_field(window=r.Header.subwindows[0].subwindows[1],name='Count'    ,format='{Company Name}',    align=CENTER,row=1,fontname='Helvetica-Bold',fontsize=18)
    H.add_field(window=r.Header.subwindows[0].subwindows[1],name='Header Title'    ,format='{Report Title}',    align=CENTER,row=2)
    H.add_field(window=r.Header.subwindows[0].subwindows[1],name='Period'    ,
        format='from %s to %s'%(
            r.vars['vars']['From'].strftime("%Y-%m-%d"),
            r.vars['vars']['To'].strftime("%Y-%m-%d")),
        align=CENTER,row=3)
    H.add_field(window=r.Header.subwindows[0].subwindows[1],name='CC'    ,
        format=('%s %s'%(
                r.vars['vars']['ccname'],
                r.vars['vars']['platformname']
                )).strip(),
        align=CENTER,row=4)
  
    H.add_field(window=r.Header.subwindows[1].subwindows[0],name='N'     ,format='Rec',    align=CENTER,fontname='Helvetica-Bold',fontsize=11,color=blue)
    H.add_field(window=r.Header.subwindows[1].subwindows[1],name='CU'    ,format='Component',    align=CENTER,fontname='Helvetica-Bold',fontsize=11,color=blue)
    H.add_field(window=r.Header.subwindows[1].subwindows[2],name='Price' ,format='Price',    align=CENTER,fontname='Helvetica-Bold',fontsize=11,color=blue)
    H.add_field(window=r.Header.subwindows[1].subwindows[3],name='Q'     ,format='Quantity',    align=CENTER,fontname='Helvetica-Bold',fontsize=11,color=blue)
    H.add_field(window=r.Header.subwindows[1].subwindows[4],name='STXR'  ,format='Sub Total XR',    align=CENTER,fontname='Helvetica-Bold',fontsize=11,color=blue)
    H.add_field(window=r.Header.subwindows[1].subwindows[5],name='XR'    ,format='XR',    align=CENTER,fontname='Helvetica-Bold',fontsize=11,color=blue)
    H.add_field(window=r.Header.subwindows[1].subwindows[6],name='SubT'  ,format='Sub Total',    align=CENTER,fontname='Helvetica-Bold',fontsize=11,color=blue)

    # Asociar registro al reporte
    r.add_header_record(H)

def prepare_report_footer(r):
    # Poblar pie de pagina
    # Setup Report Footer
    # Horizontal subwindows
    
    footer_dimensions=[(0,1),(1,3)]
    r.pdf_create_subwindows_details   (r.Footer, dimensions=footer_dimensions,box=False,horizontal=True)
    r.Footer.box.visible=False
    # Vertical subwindows for 2 horizontal subwindow
    footer_dimensions=[0.20,0.60,0.20]
    r.pdf_create_subwindows_relatives (r.Footer.subwindows[1], dimensions=footer_dimensions,box=True)
    F=r.create_record("Pie de Pagina")
    F.add_field(window=r.Footer.subwindows[1].subwindows[0],name='Code'    ,format='{Report Name}',    align=CENTER,row=1)
    #print("r.vars ****************************************************")
    #pprint(r.vars)
    #print("r.vars ****************************************************")
    F.add_field(window=r.Footer.subwindows[1].subwindows[1],name='SubTitulo',format='Generado: {DATE} {TIME}',    align=CENTER,row=1)
    F.add_field(window=r.Footer.subwindows[1].subwindows[2],name='Page',format='Pagina: {current_page} ',align=RIGHT,row=1)
    
    r.add_footer_record(F)

def prepare_detail(r):    
    r.Detail.subwindows=[]
    #details=[(0,4),(4,46),(50,13),(63,13),(76,13),(89,21),(110,13)]
    #r.pdf_create_subwindows_details (r.Detail, dimensions=details, box=True)
    #r.pdf_create_subwindows(r.Detail, subwindows=7,box=True)
    # Max witdh should be in range 60 @ 12picas / 90 @ 8picas
    details=[4,20,12,12,12,18,12]
    # widths will be scaled to 8/12 = 2/3 because of font size = 8
    #print("details=",details)
    for i in range(len(details)):
        details[i]*=(2/3) 
    #print("details=",details)
    r.pdf_create_subwindows_widths (r.Detail, widths=details, box=True)

    for w in r.Detail.subwindows:
        w.box.visible=False
        w.box.color  =pink
        
    S=r.create_record("Summary",create_group=False)
    S.add_field(window=r.Detail,name='summary'  ,format='{}', align=LEFT ,fontname='Courier',fontsize=8)
    
    R=r.create_record("Detalle",create_group=True)
    # GV 20200330 R.borders=LINE_BOX
    R.borders=LINE_NONE
    
    # Creates al record's fields, and groups
    # Group field are defined populating parameter group with 1,2,...
    # Its important to declare fields as per data field if auto filling is going to be used
    # See: use of <Record>.get_field_names() & <Record>.set_field_value() functions in main ....
    
    # Grouping order should be considered here to ( ...,group=1,....., group=2, ....)
    # -------------------------------------------------------------------------------
    R.add_field(name='CC'     ,format='{}', group=1, coerce=str,visible=False,color=pink)
    R.add_field(name='CI'     ,format='{}', group=2, coerce=str,visible=False,color=pink)
    
    R.add_field(window=r.Detail.subwindows[ 0],name='N'    ,format='{:,d}'  , align=CENTER ,fontname='Courier',fontsize=8)
    R.add_field(window=r.Detail.subwindows[ 1],name='CU'   ,format='{}'     , align=CENTER ,fontname='Courier',fontsize=8,evaluate=False)
    R.add_field(window=r.Detail.subwindows[ 2],name='Price',format='{:,.6f}', align=RIGHT  ,fontname='Courier',fontsize=8)
    R.add_field(window=r.Detail.subwindows[ 3],name='Q'    ,format='{:,.6f}', align=RIGHT  ,fontname='Courier',fontsize=8)
    R.add_field(window=r.Detail.subwindows[ 4],name='STXR' ,format='{:,.6f}', align=RIGHT  ,fontname='Courier',fontsize=8)
    R.add_field(window=r.Detail.subwindows[ 5],name='XR'   ,format='{:,.6f}', align=RIGHT  ,fontname='Courier',fontsize=8)
    R.add_field(window=r.Detail.subwindows[ 6],name='ST'   ,format='{:,.2f}', align=RIGHT  ,fontname='Courier',fontsize=8,coerce=float)

    # Next record defines a priority field evaluation , not needed now
    #R.add_field(name='Downtime'     ,format='{:5.2f}%', align=RIGHT,fontname='Courier',fontsize=8,coerce=float,priority=0,visible=False)

    # Sets up a custom value:color dictionary for inline evaluation
    #R.fields[3].value_Colors={'CRITICAL':red,'WARNING':yellow,'DOWN':orange,'OK':lightgreen,'UNKNOWN':white}

    # references to Records's Groups
    
    Group0=R.get_group('Detalle_G0')    
    Group0.add_footer("Report-Footer") 
    Group0.footer.add_field    (window=r.Detail.subwindows[4],format='Total Reporte:' , align=RIGHT ,color=blue      ,fontname='Courier-Bold',fontsize=12)
    #Group0.footer.add_field    (window=r.Detail.subwindows[6],format='{:,d}'       , evaluate=True          ,value='{Detalle_G0_ST_S}'     ,align=RIGHT ,color=black      ,fontname='Courier-Bold',fontsize=12)
    Group0.footer.add_field    (window=r.Detail.subwindows[6],format='{:,.2f}'       , evaluate=True          ,value='{Detalle_G0_ST_S}'     ,align=RIGHT ,color=black      ,fontname='Courier-Bold',fontsize=12)

    Group1=R.get_group('Detalle_G1')    
    Group1.add_header("CC-Header")
    Group1.add_header("CC-Header-Filler") # Empty Header used to create "blank line" after hostgroup headers
    Group1.add_footer("CC-Footer") 
    Group1.add_footer("CC-Footer-Filler") # Empty Footer used to create "blank line" after hostgroup details
    # Populates Group's header's and footer's fields and output setups (window, align, color, fontname, fontsize, isgf,...)
    # isgf (is Group Field) flag is mandatory for group records coerced fields.etc.)
    Group1.header.add_field(window=r.Detail.subwindows[0],format='CC:'        ,align=LEFT ,color=blue      ,fontname='Courier-Bold',fontsize=12)
    Group1.header.add_field(window=r.Detail.subwindows[1],format='{}'           ,value='{Detalle_G1_K}'     ,align=LEFT ,color=black      ,fontname='Courier-Bold',fontsize=12)
    Group1.footer.add_field(window=r.Detail.subwindows[4],format="Total CC '{}' :",value='{Detalle_G1_K}' , align=RIGHT ,color=blue      ,fontname='Courier-Bold',fontsize=12)
    Group1.footer.add_field(window=r.Detail.subwindows[6],format='{:,.2f}'       , evaluate=True          ,value='{Detalle_G1_ST_S}'     ,align=RIGHT ,color=black      ,fontname='Courier-Bold',fontsize=12)

    Group2=R.get_group('Detalle_G2')    
    Group2.add_header("CI-Header")
    Group2.add_header("CI-Header_Filler") # Empty Header used to create "blank line" after host headers
    Group2.add_footer("CI-Footer") 
    Group2.add_footer("CI-Footer_Filler") # Empty Footer used to create "blank line" after host details
    # Populates Group's header's and footer's fields and output setups (window, align, color, fontname, fontsize, isgf,...)
    # isgf (is Group Field) flag is mandatory for group records coerced fields.etc.)
    Group2.header.add_field    (window=r.Detail.subwindows[1],format='CI:'    , align=LEFT ,color=blue      ,fontname='Courier-Bold',fontsize=12)
    Group2.header.add_field    (window=r.Detail.subwindows[2],format='{}'       , value='{Detalle_G2_K}'     ,align=LEFT ,color=black      ,fontname='Courier-Bold',fontsize=12)
    Group2.footer.add_field    (window=r.Detail.subwindows[4],format="Total CI '{}' :" , value='{Detalle_G2_K}', align=RIGHT ,color=blue      ,fontname='Courier-Bold',fontsize=12)
    Group2.footer.add_field    (window=r.Detail.subwindows[6],format='{:,.2f}'       , evaluate=True          ,value='{Detalle_G2_ST_S}'     ,align=RIGHT ,color=black      ,fontname='Courier-Bold',fontsize=12)

def prepare_report( vars ):
    # PREPARACION DEL REPORTE
    varsTuple = namedtuple('varsTuple', sorted(vars))
    rvars = varsTuple(**vars)
    r=Report(   name=rvars.name,
                company=rvars.company,
                title=rvars.title,
                filename=rvars.pdf_file,
                orientation=rvars.orientation,
                debug=rvars.debug,
                debug_function=rvars.debug_function)
    r.vars.update({'vars':vars})
    # Setup header & footer
    prepare_report_header(r)
    prepare_report_footer(r)
    # Setuo Detail format(s)
    prepare_detail(r)
    # Adjust Page Geometry if needed
    r.calculate_windows()
    # Setup windows visibility
    r.Header.box.visible                = False
    r.Header.subwindows[2].box.visible  = False
    r.Footer.box.visible                = False
    r.add_image(rvars.logo_cust,window=r.Header.subwindows[0],subwindow=0)
    r.add_image(rvars.logo_file,window=r.Header.subwindows[0],subwindow=2)
    
    return(r)

def export_to_pdf(  output_file,rows,Customer,From,To,Status,Currency,
                    CC_Id=0,Pla_Id=0,CC_Name='',Pla_Name='',CC_Code=''):
    vars={
    
        'basename':output_file,
        'name':'RPT-CR-001',
        'company':Customer,
        'title':'Charging Resume',
        'orientation':LANDSCAPE,
        'debug':False,
        'debug_function':None,
        'pdf_file' :"%s%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file))),
        'logo_file':"%s%s"%(current_app.root_path,url_for('static',filename='img/logo_emtec.png')),
        'logo_cust':"%s%s"%(current_app.root_path,url_for('static',filename='img/logo_customer.png')),
        'From':datetime.strptime(From,"%Y-%m-%d"),
        'To':datetime.strptime(To,"%Y-%m-%d"),
        'cc':CC_Id,
        'cccode':CC_Code,
        'ccname':CC_Name,
        'platform':Pla_Id,
        'platformname':Pla_Name
    }
    r = prepare_report(vars)
    r.vars.update({
        'logo_file':vars['logo_file'],
        'logo_cust':vars['logo_cust'],
        'vars':vars
        })
    R = r.get_record('Detalle')

    field_names=['CC','CI','N','CU','Price','Q','STXR','XR','ST']
    for row in rows:
        # load row values to record here
        # special attention to group keys
        # these should correspond to data ordering
        field_values=[   
            "%s: %s"%(row.CC_Code,row.CC_Description),  # Group 1 Key
            "%s"%(row.CI_Name),                         # Group 2 Key
            row.CIT_Count,
            row.CU_Description,
            row.Rat_Price,
            row.CR_Quantity,
            row.CR_ST_at_Rate_Cur,
            row.CR_Cur_XR,
            row.CR_ST_at_Cur
        ]

        R.set_field_values(field_names,field_values)
        # print row here
        R.print(WRAP)
    # complete report here
    # prints last footers if any
    R.print_final_record_footers()
    # Print report's last footer
    r.pdf_print_final_footer()
    # Closes report
    r.close()
    return vars['pdf_file']

# ======================================================================

def export_to_xls(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s.json"%(output_file)
    export_to_json(json_file,rows,Customer,From,To,Status,Currency)
    
    json_file   ="%s%s"%(current_app.root_path, url_for('static',filename='tmp/%s.json'%(output_file)))
    
    with open(json_file) as data_file:    
        d= json.load(data_file)  

    df1 = json_normalize(d, 'detail').assign(**d['header'])
        
    xlsx_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    
    df1.to_excel(xlsx_file,'Sheet 1')
           
    return xlsx_file    

def export_to_csv(output_file,rows,Customer,From,To,Status,Currency,full=False):
    cvs_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(cvs_file,"w")

    f.write('H,Customer,From,To,Status,Currency\n')
    f.write('H,"%s","%s","%s","%s","%s"\n'%(Customer,From,To,Status,Currency))
 
    if full:
        count = 0
        for row in rows:
            if count==0:
                _=[x.upper().replace("_","") for x in row.get_column_headers()]
                f.write('D,%s\n'%','.join(_))
            _=[str(x) for x in row.get_json_array()]
            f.write ("D,%s\n"%','.join(_))
            count += 1
    else:
        f.write('D,Records,CU,Rate,Q,Subtotal,XR,Total\n')
        count = 0
        for row in rows:
            f.write ("D,%s,%s,%s,%s,%s,%s,%s\n"%(
                        row.CIT_Count,
                        row.CU_Description,
                        row.Rat_Price,
                        row.CR_Quantity,
                        row.CR_ST_at_Rate_Cur,
                        row.CR_Cur_XR,
                        row.CR_ST_at_Cur
                        )
                    )
            count += 1
    f.write("T,%d\n"%(count))
    f.close()
    return cvs_file
    
def export_to_json(output_file,rows,Customer,From,To,Status,Currency,codes=False):
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
        if codes:
            dict['detail'].append(
                {   
                    'customer':               row.Cus_Id,
                    'dateFrom':               row.CR_Date_From.strftime('%Y-%m-%d'),
                    'dateTo':                 row.CR_Date_To.strftime('%Y-%m-%d'),
                    'status':                 row.CIT_Status,
                    'currency':               row.Cur_Code,
                    'items':                  row.CIT_Count, 
                    'quantity':               row.CIT_Quantity, 
                    'generation':             row.CIT_Generation, 
                    'cu':                     row.CU_Id,
                    'cc':                     row.CI_CC_Id,
                    'operation':              row.CU_Operation,
                    'type':                   row.Typ_Code,
                    'ccCurrency':             row.CC_Cur_Code,           
                    'ci':                     row.CI_Id,     
                    'rate':                   row.Rat_Id,      
                    'price':                  row.Rat_Price,
                    'mu':                     row.Rat_MU_Code,
                    'rateCurrency':           row.Rat_Cur_Code,
                    'rateHourly':             row.Rat_Hourly,
                    'rateDaily':              row.Rat_Daily,
                    'rateMonthly':            row.Rat_Monthly,
                    'resumeQuantity':         row.CR_Quantity,          # CIT Quantity after conversion, if any
                    'resumeQuantityAtRate':   row.CR_Quantity_at_Rate, 
                    'ccXR':                   row.CC_XR,
                    'resumeCurrencyXR':       row.CR_Cur_XR,
                    'subtotalAtRateCurrency': row.CR_ST_at_Rate_Cur,
                    'subtotalAtCcCurrency':   row.CR_ST_at_CC_Cur,
                    'totalAtCurrency':        row.CR_ST_at_Cur,
                    'cusName':                row.Cus_Name,
                    'ciName':                 row.CI_Name,
                    'cuDescription':          row.CU_Description,
                    'ccDescription':          row.CC_Description, 
                    'ratePeriodDescription':  row.Rat_Period_Description, 
                    'ccCode':                 row.CC_Code, 
                    'platform':               row.Pla_Id, 
                    'platformName':           row.Pla_Name, 
                }
            )
        else:
            dict['detail'].append(
                {   
                    'items':                  row.CIT_Count, 
                    'quantity':               row.CIT_Quantity, 
                    'type':                   row.Typ_Code,
                    'price':                  row.Rat_Price,
                    'mu':                     row.Rat_MU_Code,
                    'rateCurrency':           row.Rat_Cur_Code,
                    'rateHourly':             row.Rat_Hourly,
                    'rateDaily':              row.Rat_Daily,
                    'rateMounhtly':           row.Rat_Monthly,
                    'resumeQuantity':         row.CR_Quantity,
                    'resumeQuantityAtRate':   row.CR_Quantity_at_Rate, 
                    'ccXR':                   row.CC_XR,
                    'resumeCurrencyXR':       row.CR_Cur_XR,
                    'subtotalAtRateCurrency': row.CR_ST_at_Rate_Cur,
                    'subtotalAtCcCurrency':   row.CR_ST_at_CC_Cur,
                    'totalAtCurrency':        row.CR_ST_at_Cur,
                    'ciName':                 row.CI_Name,
                    'cuDescription':          row.CU_Description,
                    'ccDescription':          row.CC_Description, 
                    'ratePeriodDescription':  row.Rat_Period_Description, 
                    'ccCode':                 row.CC_Code, 
                    'platformName':           row.Pla_Name, 
                }
            )
            
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
        f.write ("D%06d%-45s%020.6f%020.6f%020.6f%020.6f%020.6f%010d*\n"%(
                    row.CIT_Count,
                    row.CU_Description,
                    row.Rat_Price,
                    row.CR_Quantity,
                    row.CR_ST_at_Rate_Cur,
                    row.CR_Cur_XR,
                    row.CR_ST_at_Cur,
                    0)
                )
        count += 1
    f.write("T%06d%0155d*\n"%(count,0))
    f.close()
    return fix_file

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
    CC_Id           =  request.args.get('CC_Id',0,type=int)
    CC_Code         =  request.args.get('CC_Code',"",type=str)
    CC_Name         =  request.args.get('CC_Name',"",type=str)
    Pla_Id          =  request.args.get('Pla_Id',0,type=int)
    Pla_Name        =  request.args.get('Pla_Name',"",type=str)
    # Get Actual Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    rows = db.Get_Charge_Resume(
            Cus_Id,
            CIT_Date_From,
            CIT_Date_To,
            CIT_Status,
            Cur_Code,
            CC_Id=CC_Id,
            Pla_Id=Pla_Id
            )
    # Aqui hace la conversion
    if   CC_Id >  0 and Pla_Id > 0:     tail="_%s_%s"%(CC_Id,Pla_Id)
    elif CC_Id == 0 and Pla_Id > 0:     tail="_%s"%(Pla_Id)
    elif CC_Id >  0 and Pla_Id == 0:    tail="_%s"%(CC_Id)
    else:                               tail=""
    output_file = "CR_%d_%s_%s_%s_%s%s.%s"%(
        Cus_Id,
        CIT_Date_From,
        CIT_Date_To,
        CIT_Status,
        Cur_Code,
        tail,
        Format
        )
    if      Format == 'pdf':
        #return_file=export_to_pdf(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
        return_file=export_to_pdf(  output_file,
                                    rows,
                                    Cus_Name,
                                    CIT_Date_From,
                                    CIT_Date_To,
                                    CIT_Status_Value,
                                    Cur_Name,
                                    CC_Id,
                                    Pla_Id,
                                    CC_Name,
                                    Pla_Name,
                                    CC_Code
                                )
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
    logger.debug("%s: return_file   = %s"%('export_Charging_Resume',return_file))
    logger.debug("%s: att name      = %s"%('export_Charging_Resume',output_file))
    return send_file(return_file,as_attachment=True,attachment_filename=output_file)

