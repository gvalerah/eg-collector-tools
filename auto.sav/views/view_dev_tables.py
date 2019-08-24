# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

@main.route('/forms/Dev_Tables', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Dev_Tables():
    """ Form handling function for table Dev_Tables """

    logger.debug('Enter: forms_Dev_Tables()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_table.query.filter(dev_table.Id == Id).first()
    if row is None:
        row=dev_table()
        session['is_new_row']=True

    session['data'] =  { 'Id':row.Id, 'Name':row.Name, 'Caption':row.Caption, 'Entity':row.Entity, 'Class_Name':row.Class_Name, 'Child_Table':row.Child_Table, 'Parent_Table':row.Parent_Table, 'Use_Pagination':row.Use_Pagination, 'Use_Children_Pagination':row.Use_Children_Pagination, 'Generate_Form_One':row.Generate_Form_One, 'Generate_Form_All':row.Generate_Form_All, 'Generate_Form_Filter':row.Generate_Form_Filter, 'Generate_Children':row.Generate_Children, 'Generate_Foreign_Fields':row.Generate_Foreign_Fields, 'Permission_View':row.Permission_View, 'Permission_Delete':row.Permission_Delete, 'Permission_Modify':row.Permission_Modify, 'Permission_Report':row.Permission_Report, 'Permission_Export':row.Permission_Export, 'Permission_View_Private':row.Permission_View_Private, 'Permission_Modify_Private':row.Permission_Modify_Private, 'Permission_Administer':row.Permission_Administer}
    form = frm_dev_table()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Name = form.Name.data
            row.Caption = form.Caption.data
            row.Entity = form.Entity.data
            row.Class_Name = form.Class_Name.data
            row.Child_Table = form.Child_Table.data
            row.Parent_Table = form.Parent_Table.data
            row.Use_Pagination = form.Use_Pagination.data
            row.Use_Children_Pagination = form.Use_Children_Pagination.data
            row.Generate_Form_One = form.Generate_Form_One.data
            row.Generate_Form_All = form.Generate_Form_All.data
            row.Generate_Form_Filter = form.Generate_Form_Filter.data
            row.Generate_Children = form.Generate_Children.data
            row.Generate_Foreign_Fields = form.Generate_Foreign_Fields.data
            row.Permission_View = form.Permission_View.data
            row.Permission_Delete = form.Permission_Delete.data
            row.Permission_Modify = form.Permission_Modify.data
            row.Permission_Report = form.Permission_Report.data
            row.Permission_Export = form.Permission_Export.data
            row.Permission_View_Private = form.Permission_View_Private.data
            row.Permission_Modify_Private = form.Permission_Modify_Private.data
            row.Permission_Administer = form.Permission_Administer.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Table created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Table %s saved OK</b>'%(Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Table record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Dev_Tables_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=dev_table()
            return redirect(url_for('.forms_Dev_Tables',Id=row.Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Table Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Table data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Dev_Tables',Id=row.Id))

    form.Name.data = row.Name
    form.Caption.data = row.Caption
    form.Entity.data = row.Entity
    form.Class_Name.data = row.Class_Name
    form.Child_Table.data = row.Child_Table
    form.Parent_Table.data = row.Parent_Table
    form.Use_Pagination.data = row.Use_Pagination
    form.Use_Children_Pagination.data = row.Use_Children_Pagination
    form.Generate_Form_One.data = row.Generate_Form_One
    form.Generate_Form_All.data = row.Generate_Form_All
    form.Generate_Form_Filter.data = row.Generate_Form_Filter
    form.Generate_Children.data = row.Generate_Children
    form.Generate_Foreign_Fields.data = row.Generate_Foreign_Fields
    form.Permission_View.data = row.Permission_View
    form.Permission_Delete.data = row.Permission_Delete
    form.Permission_Modify.data = row.Permission_Modify
    form.Permission_Report.data = row.Permission_Report
    form.Permission_Export.data = row.Permission_Export
    form.Permission_View_Private.data = row.Permission_View_Private
    form.Permission_Modify_Private.data = row.Permission_Modify_Private
    form.Permission_Administer.data = row.Permission_Administer
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('dev_tables.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Dev_Tables_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Dev_Tables_delete():
    """ Delete record handling function for table Dev_Tables """

    logger.debug('Enter: forms_Dev_Tables_delete()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_table.query.filter(dev_table.Id == Id).first()
    if row is None:
        row=dev_table()
    session['data'] =  { 'Id':row.Id, 'Name':row.Name, 'Caption':row.Caption, 'Entity':row.Entity, 'Class_Name':row.Class_Name, 'Child_Table':row.Child_Table, 'Parent_Table':row.Parent_Table, 'Use_Pagination':row.Use_Pagination, 'Use_Children_Pagination':row.Use_Children_Pagination, 'Generate_Form_One':row.Generate_Form_One, 'Generate_Form_All':row.Generate_Form_All, 'Generate_Form_Filter':row.Generate_Form_Filter, 'Generate_Children':row.Generate_Children, 'Generate_Foreign_Fields':row.Generate_Foreign_Fields, 'Permission_View':row.Permission_View, 'Permission_Delete':row.Permission_Delete, 'Permission_Modify':row.Permission_Modify, 'Permission_Report':row.Permission_Report, 'Permission_Export':row.Permission_Export, 'Permission_View_Private':row.Permission_View_Private, 'Permission_Modify_Private':row.Permission_Modify_Private, 'Permission_Administer':row.Permission_Administer}
    form = frm_dev_table_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Table %s deleted OK'%(Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Dev_Tables_delete',Id=session['data']['Id']))

            return redirect(url_for('.select_Dev_Tables_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Dev_Tables_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Dev_Tables_query'))


    return render_template('dev_tables_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Dev_Tables_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Dev_Tables_query():
    """ Select rows handling function for table Dev_Tables """

    logger.debug('Enter: select_Dev_Tables_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Id':
            rows =  dev_table.query.filter_by(Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Name':
            rows =  dev_table.query.filter_by(Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Caption':
            rows =  dev_table.query.filter_by(Caption=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Entity':
            rows =  dev_table.query.filter_by(Entity=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Class_Name':
            rows =  dev_table.query.filter_by(Class_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Child_Table':
            rows =  dev_table.query.filter_by(Child_Table=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Parent_Table':
            rows =  dev_table.query.filter_by(Parent_Table=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Use_Pagination':
            rows =  dev_table.query.filter_by(Use_Pagination=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Use_Children_Pagination':
            rows =  dev_table.query.filter_by(Use_Children_Pagination=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Form_One':
            rows =  dev_table.query.filter_by(Generate_Form_One=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Form_All':
            rows =  dev_table.query.filter_by(Generate_Form_All=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Form_Filter':
            rows =  dev_table.query.filter_by(Generate_Form_Filter=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Children':
            rows =  dev_table.query.filter_by(Generate_Children=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Foreign_Fields':
            rows =  dev_table.query.filter_by(Generate_Foreign_Fields=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_View':
            rows =  dev_table.query.filter_by(Permission_View=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Delete':
            rows =  dev_table.query.filter_by(Permission_Delete=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Modify':
            rows =  dev_table.query.filter_by(Permission_Modify=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Report':
            rows =  dev_table.query.filter_by(Permission_Report=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Export':
            rows =  dev_table.query.filter_by(Permission_Export=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_View_Private':
            rows =  dev_table.query.filter_by(Permission_View_Private=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Modify_Private':
            rows =  dev_table.query.filter_by(Permission_Modify_Private=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Administer':
            rows =  dev_table.query.filter_by(Permission_Administer=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  dev_table.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Dev_Tables_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Dev_Tables_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Dev_Tables_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Dev_Tables_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('dev_tables_All.html',rows=rows)
# =============================================================================
