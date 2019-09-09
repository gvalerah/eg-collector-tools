# =============================================================================
# View for Get Billing Resume from DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================

from ..models       import frm_billing_resume
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Billing_Resume', methods=['GET', 'POST'])
@login_required
def forms_Get_Billing_Resume():
    logger.debug('Enter: forms_Get_Billing_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_billing_resume()

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
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            
            return redirect(url_for('.report_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1]
                                ))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_Billing_Resume'))

    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('get_billing_resume.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/Billing_Resume', methods=['GET','POST'])
@login_required
def report_Billing_Resume():
    logger.debug('Enter: report_Billing_Resume()')
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    # Get Actual Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="C*ALL Get_Billing_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    rows =  db.engine.execute(query).fetchall()
    
    # ----------------------------------------------------------------------------------------------
    # NOTA AQUI HAY QUE MANEJAR LOS EXTRACTOS ESTATICOS, SON BUENA OPCION, PONERLA COMO ADICIONAL
    # ----------------------------------------------------------------------------------------------
    json_route = "/tmp"
    json_file_name =  "%s/CR001_%s_%s_%s_%s_%s.json"%(json_route,Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    dict = {}
    dict.update({'header':{}})
    dict['header'].update({'customer':Cus_Id})
    dict['header'].update({'from':CIT_Date_From})
    dict['header'].update({'to':CIT_Date_To})
    dict['header'].update({'status':CIT_Status})
    dict['header'].update({'currency':Cur_Code})
    dict.update({'detail':[]})
    count = 0
    for row in rows:
        dict['detail'].append({})
        dict['detail'][count].update( {    'items':row.ITEMS, 'cu':row.CU, 'price':row.RATE_PRICE, 'q':row.Q, 'subtotal':row.ST_AT_RATE,\
                                    'xr':row.BILLXR, 'total':row.TOTAL_BILL_CUR \
                                })
        count += 1
    dict['header'].update({'count':count})
    
    with open(json_file_name,'w') as fp:
        json.dump(dict,fp)
    
    return render_template('report_billing_resume.html',rows=rows,
                Cus_Id=Cus_Id,
                Cus_Name=Cus_Name,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name
                )

