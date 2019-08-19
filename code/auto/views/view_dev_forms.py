# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Dev_Forms', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Dev_Forms():
    """ Form handling function for table Dev_Forms """

    logger.debug('Enter: forms_Dev_Forms()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_form.query.filter(dev_form.Id == Id).first()
    if row is None:
        row=dev_form()
        session['is_new_row']=True

    session['data'] =  { 'Id':row.Id, 'Table':row.Table, 'Field':row.Field, 'Type':row.Type, 'Null':row.Null, 'Key':row.Key, 'Default':row.Default, 'Extra':row.Extra, 'Foreign_Key':row.Foreign_Key, 'Referenced_Table':row.Referenced_Table, 'Foreign_Field':row.Foreign_Field, 'Foreign_Value':row.Foreign_Value, 'Length':row.Length, 'Validation':row.Validation, 'Validation_Type':row.Validation_Type, 'Validation_String':row.Validation_String, 'Caption_String':row.Caption_String, 'Field_Order':row.Field_Order, 'Field_Format':row.Field_Format, 'Form_Editable':row.Form_Editable, 'ORM_Schema':row.ORM_Schema}
    form = frm_dev_form()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Table = form.Table.data
            row.Field = form.Field.data
            row.Type = form.Type.data
            row.Null = form.Null.data
            row.Key = form.Key.data
            row.Default = form.Default.data
            row.Extra = form.Extra.data
            row.Foreign_Key = form.Foreign_Key.data
            row.Referenced_Table = form.Referenced_Table.data
            row.Foreign_Field = form.Foreign_Field.data
            row.Foreign_Value = form.Foreign_Value.data
            row.Length = form.Length.data
            row.Validation = form.Validation.data
            row.Validation_Type = form.Validation_Type.data
            row.Validation_String = form.Validation_String.data
            row.Caption_String = form.Caption_String.data
            row.Field_Order = form.Field_Order.data
            row.Field_Format = form.Field_Format.data
            row.Form_Editable = form.Form_Editable.data
            row.ORM_Schema = form.ORM_Schema.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Form created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Form %s saved OK</b>'%(Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Form record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Dev_Forms_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=dev_form()
            return redirect(url_for('.forms_Dev_Forms',Id=row.Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Form Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Form data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Dev_Forms',Id=row.Id))

    form.Table.data = row.Table
    form.Field.data = row.Field
    form.Type.data = row.Type
    form.Null.data = row.Null
    form.Key.data = row.Key
    form.Default.data = row.Default
    form.Extra.data = row.Extra
    form.Foreign_Key.data = row.Foreign_Key
    form.Referenced_Table.data = row.Referenced_Table
    form.Foreign_Field.data = row.Foreign_Field
    form.Foreign_Value.data = row.Foreign_Value
    form.Length.data = row.Length
    form.Validation.data = row.Validation
    form.Validation_Type.data = row.Validation_Type
    form.Validation_String.data = row.Validation_String
    form.Caption_String.data = row.Caption_String
    form.Field_Order.data = row.Field_Order
    form.Field_Format.data = row.Field_Format
    form.Form_Editable.data = row.Form_Editable
    form.ORM_Schema.data = row.ORM_Schema
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('dev_forms.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Dev_Forms_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Dev_Forms_delete():
    """ Delete record handling function for table Dev_Forms """

    logger.debug('Enter: forms_Dev_Forms_delete()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_form.query.filter(dev_form.Id == Id).first()
    if row is None:
        row=dev_form()
    session['data'] =  { 'Id':row.Id, 'Table':row.Table, 'Field':row.Field, 'Type':row.Type, 'Null':row.Null, 'Key':row.Key, 'Default':row.Default, 'Extra':row.Extra, 'Foreign_Key':row.Foreign_Key, 'Referenced_Table':row.Referenced_Table, 'Foreign_Field':row.Foreign_Field, 'Foreign_Value':row.Foreign_Value, 'Length':row.Length, 'Validation':row.Validation, 'Validation_Type':row.Validation_Type, 'Validation_String':row.Validation_String, 'Caption_String':row.Caption_String, 'Field_Order':row.Field_Order, 'Field_Format':row.Field_Format, 'Form_Editable':row.Form_Editable, 'ORM_Schema':row.ORM_Schema}
    form = frm_dev_form_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Form %s deleted OK'%(Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Dev_Forms_delete',Id=session['data']['Id']))

            return redirect(url_for('.select_Dev_Forms_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Dev_Forms_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Dev_Forms_query'))


    return render_template('dev_forms_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Dev_Forms_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Dev_Forms_query():
    """ Select rows handling function for table Dev_Forms """

    logger.debug('Enter: select_Dev_Forms_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Id':
            rows =  dev_form.query.filter_by(Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Table':
            rows =  dev_form.query.filter_by(Table=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Field':
            rows =  dev_form.query.filter_by(Field=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Type':
            rows =  dev_form.query.filter_by(Type=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Null':
            rows =  dev_form.query.filter_by(Null=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Key':
            rows =  dev_form.query.filter_by(Key=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Default':
            rows =  dev_form.query.filter_by(Default=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Extra':
            rows =  dev_form.query.filter_by(Extra=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Foreign_Key':
            rows =  dev_form.query.filter_by(Foreign_Key=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Referenced_Table':
            rows =  dev_form.query.filter_by(Referenced_Table=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Foreign_Field':
            rows =  dev_form.query.filter_by(Foreign_Field=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Foreign_Value':
            rows =  dev_form.query.filter_by(Foreign_Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Length':
            rows =  dev_form.query.filter_by(Length=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Validation':
            rows =  dev_form.query.filter_by(Validation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Validation_Type':
            rows =  dev_form.query.filter_by(Validation_Type=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Validation_String':
            rows =  dev_form.query.filter_by(Validation_String=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Caption_String':
            rows =  dev_form.query.filter_by(Caption_String=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Field_Order':
            rows =  dev_form.query.filter_by(Field_Order=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Field_Format':
            rows =  dev_form.query.filter_by(Field_Format=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Form_Editable':
            rows =  dev_form.query.filter_by(Form_Editable=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'ORM_Schema':
            rows =  dev_form.query.filter_by(ORM_Schema=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  dev_form.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Dev_Forms_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Dev_Forms_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Dev_Forms_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Dev_Forms_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('dev_forms_All.html',rows=rows)
# =============================================================================
