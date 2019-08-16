# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2018-08-16
# =============================================================================

from emtec.collector.forms       import frm_stats_use_per_type
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Stats_Per_Type', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Get_Stats_Per_type():
    logger.debug('Enter: forms_Get_Stats_Per_Type()'%())

    form = frm_stats_use_per_type()

    if form.validate_on_submit():
        if     form.submit_Report.data:

            print("form=",form)
            print("form.Year=",form.Year)
            Year=form.Year
            print("Year=",Year)
            print("Year.data=",Year.data)

            return redirect(url_for('.report_Stats_Use_Per_Type',
                                Year            = form.Year.data
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_User_Resume'))


    return render_template('stats_use_per_type.html',form=form)

# =============================================================================

import simplejson as json

@main.route('/report/Stats_Use_Per_Type', methods=['GET','POST'])
@login_required
@admin_required
def report_Stats_Use_Per_Type():
    logger.debug('Enter: report_Stats_Use_Per_Type()')
    
    Year            =  request.args.get('Year',None,type=int)
    
    print("Year=",Year)
    
    rows= db.session.query(st_use_per_type)\
                    .filter(st_use_per_type.Year==Year)\
                    .order_by(st_use_per_type.Typ_Code)\
                    .all()
    
    return render_template('report_stats_use_per_type.html',
                        rows=rows,
                        Year=Year
                )

