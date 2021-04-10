# =============================================================================
# View for Get Active Sharding Period
# (c) Sertechno 2020
# GLVH @ 2020-03-18
# =============================================================================

from emtec.collector.forms       import frm_set_period

@main.route('/forms/Set_Period', methods=['GET', 'POST'])
@login_required
def forms_Set_Period():
    logger.debug('Enter: forms_Set_Period()'%())
    form = frm_set_period()
    # Aqui debe determinar los periodos disponibles
    # segun BD y coordinado con indicador en Tabla Interface para este
    # usuario

    set_periods_available(
        db.engine,
        Interface,
        current_user.id
        )

    session['data'] =  { 'Period': get_period_data(
                                        User_Id=current_user.id,
                                        engine=db.engine,
                                        Interface=Interface
                                        ) 
                        }

    period_choices=[]
    periods=session['data']['Period']['available'].split(',')

    try:
        for period in periods:
            description="Charge Items table for %s"%(
                datetime.strptime(period,"%Y%m").strftime("%B %Y")
                )
            period_choices.append((period,description))
    except:
        flash('Warning no periods available ...')
        pass
    form.Period.choices   = period_choices
    #form.Period.data      = session['data']['Period']['active']
                            
    if form.validate_on_submit():
        data=session['data']
        print("**********************************************")
        print("data=",data)
        print("**********************************************")
        if     form.submit_Set.data:
            # Aqui ajusta valor en BD para este usuario segun seleccion
            # usa funcion set ....
            
            set_interface_variable(
                engine=db.engine,
                Interface=Interface,
                User_Id=current_user.id,
                Table_name='CONTEXT',
                name='active_period',   # Variable name
                value=form.Period.data              # variable value
            )
            return redirect(url_for('.set_Period', data = data ))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            print('form validated but not submited ???')
        return redirect(url_for('.index'))
    return render_template(
            'set_period.html',
            form=form,
            collectordata=get_collectordata(),
            data=get_period_data(
                    engine=db.engine,
                    Interface=Interface,
                    User_Id=current_user.id
                    )
            )

# =============================================================================

@main.route('/set/Period', methods=['GET','POST'])
@login_required
def set_Period():
    function_name=sys._getframe().f_code.co_name
    logger.debug('%s: Enter'%(function_name))

    return render_template(
            'report_period.html',
            collectordata=get_collectordata(),
            data=get_period_data(
                    engine=db.engine,
                    Interface=Interface,
                    User_Id=current_user.id
                    )
            )
