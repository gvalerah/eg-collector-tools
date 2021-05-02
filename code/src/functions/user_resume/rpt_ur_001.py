# ----------------------------------------------------------------------
# rpt-ur-001 
# ----------------------------------------------------------------------
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
    # "%12.6f" 12 13 50- 62 % ( row.Rat_Price          )   )
    # "%12.6f" 12 13 63- 75 % ( row.CR_Quantity        )   )
    # "%12.6f" 12 13 76- 88 % ( row.CR_ST_at_Rate_Cur  )   )
    # "%20.6f" 20 21 89-109 % ( row.CR_Cur_XR          )   )
    # "%12.6f" 12 13 110-122 % ( row.CR_ST_at_Cur       )   )    
    
    # Max witdh should be in range 60 @ 12picas / 90 @ 8picas
    details=[4,20,12,12,12,12]
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
    #.add_field(window=r.Detail.subwindows[ 5],name='XR'   ,format='{:,.6f}', align=RIGHT  ,fontname='Courier',fontsize=8)
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
    r=Report(   name           = rvars.name,
                company        = rvars.company,
                title          = rvars.title,
                filename       = rvars.pdf_file,
                orientation    = rvars.orientation,
                debug          = rvars.debug,
                debug_function = rvars.debug_function)
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
    
        'basename'      : output_file,
        'name'          : 'RPT-UR-001',
        'company'       : Customer,
        'title'         : 'User Charging Resume',
        'orientation'   : LANDSCAPE,
        'debug'         : False,
        'debug_function': None,
        'pdf_file'      : "%s%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file))),
        'logo_file'     : "%s%s"%(current_app.root_path,url_for('static',filename='img/logo_emtec.png')),
        'logo_cust'     : "%s%s"%(current_app.root_path,url_for('static',filename='img/logo_customer.png')),
        'From'          : datetime.strptime(From,"%Y-%m-%d"),
        'To'            : datetime.strptime(To,"%Y-%m-%d"),
        'cc'            : CC_Id,
        'cccode'        : CC_Code,
        'ccname'        : CC_Name,
        'platform'      : Pla_Id,
        'platformname'  : Pla_Name
    }
    r = prepare_report(vars)
    r.vars.update({
        'logo_file':vars['logo_file'],
        'logo_cust':vars['logo_cust'],
        'vars':vars
        })
    R = r.get_record('Detalle')

    field_names=['CC','CI','N','CU','Price','Q','STXR','ST']
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
            row.CR_Quantity_at_Rate,
            row.CR_ST_at_Rate_Cur,
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
