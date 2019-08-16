# =============================================================================
# View for Change_CIT_State
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_change_cit_state,frm_change_cit_state_confirm
from babel.numbers  import format_number, format_decimal, format_percent
from sqlalchemy     import and_

@main.route('/forms/Change_CIT_State', methods=['GET', 'POST'])
@login_required
def forms_Change_CIT_State():
    logger.debug('Enter: forms_Change_CIT_State()'%())

    session['data'] =  {    'CU_Id': None, 
                            'CIT_Date_From':None, 
                            'CIT_Time_From':'00:00:00', 
                            'CIT_Date_To':None, 
                            'CIT_Time_To':'23:00:00', 
                            'CIT_Status':1,
                            'CIT_Status_To':1
                       }

    form = frm_change_cit_state()

    hours=[]
    for h in range(0,24):
        hh="%02d:00:00"%h
        hours.append((hh,hh))

    form.CU_Id.choices = db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).order_by(charge_unit.CU_Description).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.CIT_Status_To.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.CIT_Time_From.choices = hours
    form.CIT_Time_To.choices = hours
 
    if form.validate_on_submit():
        session['data']['CU_Id'         ] = form.CU_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Time_From' ] = form.CIT_Time_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT_Time_To'   ] = form.CIT_Time_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['CIT-Status_To' ] = form.CIT_Status_To.data
        if     form.submit_Search.data:
            # Get the Selected options index for string lists
            for i in range(len(form.CU_Id.choices)):
                if form.CU_Id.choices[i][0]==form.CU_Id.data:
                    cu_index=i
            return redirect(url_for('.report_Change_CIT_State_Confirm',
                                CU_Id           = form.CU_Id.data,
                                CU_Description        = form.CU_Id.choices[cu_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Time_From   = form.CIT_Time_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Time_To     = form.CIT_Time_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                CIT_Status_To      = form.CIT_Status_To.data,
                                CIT_Status_To_Value= form.CIT_Status.choices[form.CIT_Status_To.data-1][1],
                                ))
        elif   form.submit_Cancel.data:
            flash('Search discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Change_CIT_State'))

    form.CU_Id.data        = session['data']['CU_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Time_From.data = session['data']['CIT_Time_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Time_To.data   = session['data']['CIT_Time_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.CIT_Status_To.data    = session['data']['CIT_Status_To']

    return render_template('change_cit_state.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json
import datetime

@main.route('/report/Change_CIT_State_Confirm', methods=['GET','POST'])
@login_required
def report_Change_CIT_State_Confirm():
    logger.debug('Enter: report_Charging_Resume()')
    CU_Id          =  request.args.get('CU_Id',None,type=int)
    CU_Description        =  request.args.get('CU_Description',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Time_From   =  request.args.get('CIT_Time_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Time_To     =  request.args.get('CIT_Time_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    CIT_Status_To      =  request.args.get('CIT_Status_To',None,type=int)
    CIT_Status_To_Value=  request.args.get('CIT_Status_To_Value',None,type=str)    

    # DateTime fields are required for correct searches & updates
    CIT_DateTime_From   =  '%s %s'%(CIT_Date_From,CIT_Time_From)
    CIT_DateTime_To     =  '%s %s'%(CIT_Date_To,CIT_Time_To)
    
    query = db.session.query(charge_item)\
                    .join(charge_unit).add_column(charge_unit.CU_UUID)\
                    .join(configuration_item)\
                    .filter(charge_item.CU_Id == CU_Id)\
                    .filter(charge_item.CIT_Status == CIT_Status)\
                    .filter(and_(   charge_item.CIT_DateTime >= CIT_DateTime_From,
                                    charge_item.CIT_DateTime <= CIT_DateTime_To
                                )
                            )
        
    rows=query.all()

    form = frm_change_cit_state_confirm()

    if form.validate_on_submit():
        if     form.submit_Change.data:
            # Aqui cambia efectivamente los datos
            query = db.session.query(charge_item)\
                    .filter(charge_item.CU_Id == CU_Id)\
                    .filter(charge_item.CIT_Status == CIT_Status)\
                    .filter(and_(   charge_item.CIT_DateTime >= CIT_DateTime_From,
                                    charge_item.CIT_DateTime <= CIT_DateTime_To
                                )
                            )
            rows=query.all()
                        
            try:
                count=0
                audit_records=[]
                for row in rows:
                    previous=str(row)
                    row.CIT_Status = CIT_Status_To
                    updated=str(row)
                    audit_records.append([previous,updated])
                    count += 1
                db.session.commit()
                flash("Charge Items status modified OK from '%s' to '%s' for %d records"%(CIT_Status_Value,CIT_Status_To_Value,count))
                for record in audit_records:
                    logger.audit("%s:OLD:%s"%(current_user.username,record[0]))
                    logger.audit("%s:UPD:%s"%(current_user.username,record[1]))
            except Exception as e:
                flash("Exception updating Charge Items: %s"%e)            
            return redirect(url_for('.forms_Change_CIT_State'))
        elif   form.submit_Cancel.data:
            flash('Change discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Change_CIT_State'))
    
    return render_template('change_cit_state_confirm.html',rows=rows,form=form,
                CU_Id=CU_Id,
                CU_Description=CU_Description,
                CIT_Date_From=CIT_Date_From,
                CIT_Time_From=CIT_Time_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Time_To=CIT_Time_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                CIT_Status_To=CIT_Status_To,
                CIT_Status_To_Value=CIT_Status_To_Value 
                )


