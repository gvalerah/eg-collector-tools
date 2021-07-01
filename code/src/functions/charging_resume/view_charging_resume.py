# ======================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# GLVH @ 2019-08-18 Refactoring to ORM DB Only
# GLVH @ 2020-10-25 Proper sharding and initialization handling
# ======================================================================

from pprint                         import pformat
from emtec.collector.forms          import frm_charging_resume
from babel.numbers                  import format_number
from babel.numbers                  import format_decimal
from babel.numbers                  import format_percent
from emtec.collector.db.orm_model   import Configuration_Items

# ======================================================================

@main.route('/forms/Get_Charging_Resume', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume():
    logger.debug(f'{this()}: Enter')
    collectordata=get_collectordata()

    session['data'] =  {    'Cus_Id': None,
                            'CIT_Date_From':collectordata['COLLECTOR_PERIOD']['start'], 
                            'CIT_Date_To':collectordata['COLLECTOR_PERIOD']['end'], 
                            'CIT_Status':1,
                            'Cur_Code':'USD'}

    form = frm_charging_resume()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Commit all pending DB states in order to refresh data
    db.session.commit()
    db.session.flush()
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
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
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Update          = 0
                                ))
        if     form.submit_Update.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Update          = 1
                                ))
        elif   form.submit_Cancel.data:
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Get_Charging_Resume'))

    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('charging_resume.html',
                form=form, 
                data=session.get('data'), 
                collectordata=get_collectordata()
                )

# ======================================================================

import simplejson as json

@main.route('/report/Charging_Resume', methods=['GET','POST'])
@login_required
def report_Charging_Resume():
    logger.debug(f'{this()}: Enter')    
    collectordata=get_collectordata()
    
    db.session.flush()
    db.session.commit()
    
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
        
    # Updated cached data for this specific query if requested 
    if Update == 1:
        query = db.session.query(
                Configuration_Items.CI_Id
                ).filter(Configuration_Items.Cus_Id==Cus_Id
                ).order_by( Configuration_Items.CC_Id,
                            Configuration_Items.CI_Id
                )
        logger.debug (f"{this()}: Cus_Id= {Cus_Id} query: {query}")
        CI = query.all()
        logger.debug (f"{this()}: {len(CI)} CI's found for customer {Cus_Id}")
        logger.debug (f"{this()}: {pformat(CI)}")
        resume_records=0

        for ci in CI:
            logger.debug ("%s: db.Update_Charge_Resume_CI(%s,%s,%s,%s,%s,%s,%s,%s)"%(
                this(),
                Cus_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                ci.CI_Id,
                charge_item.__table__.name,
                charge_item.__tablename__
                )
            )
            records = db.Update_Charge_Resume_CI(
                Cus_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                ci.CI_Id,
                charge_item)
            resume_records += records

        logger.debug (f"{this()}: resume_records updated = {resume_records}")
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    rows = db.Get_Charge_Resume(
                Cus_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code
                )

    return render_template('report_charging_resume.html',
                rows=rows,
                Cus_Id=Cus_Id,
                Cus_Name=Cus_Name,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name,
                collectordata=get_collectordata()
                )

@main.route('/download/Charging_Resume', methods=['GET','POST'])
@login_required
def download_Charging_Resume():
    logger.debug(f'{this()}: Enter')    
    collectordata=get_collectordata()
    
    db.session.flush()
    db.session.commit()
    
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    # Gets Charge Resume from DB
    rows = db.Get_Charge_Resume(
                Cus_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code
                )
                
    temp_name   = next(tempfile._get_candidate_names())
    output_file = f"{temp_name}.xlsx"
    
    d = {
        'detail':[],
        'Cus-Id':Cus_Id,
        'CIT_Date_From':CIT_Date_From,
        'CIT_Date_To':CIT_Date_To,
        'CIT_Status':CIT_Status,
        'Cur_Code':Cur_Code,
        'file':output_file,
        'rows':len(rows)
    }
    # Build list of records to export from query
    for row in rows:
        d['detail'].append({
                'ccCode':row.CC_Code,
                'ccDescription':row.CC_Description,
                'ciName':row.CI_Name,
                'cuDescription':row.CU_Description,
                'items':row.CIT_Count,
                'mu':row.Rat_MU_Code,
                'price':float(row.Rat_Price),
                'rateCurrency':row.Cur_Code,
                'ratePeriodDescription':row.Rat_Period_Description,
                'resumeQuantityAtRate':float(row.CR_Quantity_at_Rate),
                'totalAtCurrency':float(row.CR_ST_at_Rate_Cur),
                'from':row.CR_Date_From,
                'to':row.CR_Date_To,
        })
    # List of fields in desired order 
    headers=[
                'ccCode',
                'ccDescription',
                'ciName',
                'cuDescription',
                'items',
                'mu',
                'price',
                'rateCurrency',
                'ratePeriodDescription',
                'resumeQuantityAtRate',
                'totalAtCurrency',
                'from',
                'to',
    ]
    # Normalize data into a Pandas Dataframe
    df1 = json_normalize(d, 'detail')
    # Reorder columns
    df1 = df1.reindex(columns=headers)
    # create temporary filename       
    xlsx_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    df1.to_excel(xlsx_file,'Sheet 1')
    return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file)
