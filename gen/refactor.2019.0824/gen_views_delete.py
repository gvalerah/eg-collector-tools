# General variables
from gen.gen_functions      import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja
from gen.gen_functions      import Gen_Views_Permissions

def Gen_Views_Delete(Tab,f):

    table_name = Tab['table']
    class_name = Tab['class']
    

    # ------------------------------------------------------------------------ 
    # Create DELETE FORM 
    # ------------------------------------------------------------------------ 
        
    f.write(    "@main.route('/forms/%s_delete', methods=['GET', 'POST'])\n"    % (table_name) )
    f.write(    "@login_required\n" )
    f.write(    "@permission_required(Permission.DELETE)\n" )
    Gen_Views_Permissions(Tab,f)    
    f.write(    "def forms_%s_delete():\n"%(table_name))
    f.write(    '    """ Delete record handling function for table %s """\n\n'                % (table_name) )
    f.write(    "    logger.debug('Enter: forms_%s_delete()')\n"           % (table_name) )

    for key in Tab['keys']:
        f.write(    "    %s  =  request.args.get('%s',0,type=int)\n"%(key,key))

    f.write(    "    row =  %s.query.filter(%s).first()\n"                  % (class_name,Tab['code']['key_filter']) )    

    f.write(    "    if row is None:\n")
    f.write(    "        row=%s()\n"                                        % (class_name) )    
    f.write(    "    session['data'] =  {%s}\n"                             % (Tab['code']['dict_fields']) )
                       
    f.write(    "    form = frm_%s_delete()\n\n"                                   % (class_name) )

    if Tab['has_fks']:
        pass
            
    # Actual Form activation here
    f.write(        "    if form.validate_on_submit():\n")
    for c in Tab['columns']:
        if c['is_id'] is not True:
            pass
    # Code for SAVE option
    f.write(        "        if  form.submit_Delete.data:\n")
    f.write(        "            print('Delete Data Here...')\n")

    for c in Tab['columns']:
        if not c['is_id']:
            pass

    #f.write(        "            print('Delete Data Here...')\n")
    f.write(        "            try:\n")
    f.write(        "                session['deleted_row']=str(row)\n")
    f.write(        "                db.session.close()\n")
    f.write(        "                db.session.delete(row)\n")
    f.write(        "                db.session.commit()\n")
    f.write(        "                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )\n")
    f.write(        "                flash('%s %%s deleted OK'%%(%s))\n"      % (Tab['entity'],Tab['code']['key_fields']))
    f.write(        "            except exc.IntegrityError as e:\n")
    f.write(        "                db.session.rollback()\n")    
    f.write(        "                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')\n")
    #f.write(        "                flash('INTEGRITY ERROR: %s'%(e))\n")
    #f.write(        "                flash('DIR E: %s'%(dir(e)))\n")
    #f.write(        "                flash('E Code : %s'%(e.code))\n")
    #f.write(        "                flash('E Detail : %s'%(e.detail))\n")
    #f.write(        "                flash('E Statement : %s'%(e.statement))\n")
    f.write(        "                return redirect(url_for('.forms_%s_delete',%s))\n\n"%(table_name,Tab['code']['key_redirs']))    
    #f.write(        "            return redirect(url_for('.select_%s'))\n"  % (table_name))    

    for c in Tab['columns']:
        if not c['is_id']:
            #f.write("            form.%s.data = session['data']['%s']\n"%(c['field'],c['field']))            
            pass
    f.write(        "            return redirect(url_for('.select_%s_query'))\n"  % (table_name))    

    # Code for CANCEL option 
    f.write(        "        elif   form.submit_Cancel.data:\n")
    f.write(        "            print('Cancel Data Here ... does nothing')\n")
    f.write(        "            flash('Record modifications discarded ...')\n")
    f.write(        "            return redirect(url_for('.select_%s_query'))\n"  % (table_name))    

    # Code for ANY OTHER option should never get here
    f.write(        "        else:\n")
    f.write(        "            print('form validated but not submited ???')\n")
    # GV 20181113 f.write(        "        return redirect(url_for('.forms_%s_delete',%s))\n\n"%(table_name,Tab['code']['key_redirs']))    
    # GV 20181113 f.write(        "            return render_template('%s.html',C=C, form=form, data=session.get('data'),row=row)\n\n"%(table_name.lower()))    
    f.write(        "            return redirect(url_for('.select_%s_query'))\n"  % (table_name))    

    for c in Tab['columns']:
        if not c['is_id']:
            #f.write("    form.%s.data = session['data']['%s']\n"%(c['field'],c['field']))
            pass           

    f.write(        "\n")    

    f.write(        "\n")    

    #f.write(        "    return render_template('%s_delete.html',C=C, form=form, data=session.get('data'),row=row)\n\n"%(table_name.lower()))    
    f.write(        "    return render_template('%s_delete.html', form=form, data=session.get('data'),row=row)\n\n"%(table_name.lower()))    
    f.write(Dash)

