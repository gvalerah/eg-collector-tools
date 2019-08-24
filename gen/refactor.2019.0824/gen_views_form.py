# General variables
from gen.gen_functions      import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja
from gen.gen_functions      import Gen_Views_Permissions

def Gen_Views_Form(Tab,f,f2):

    # ------------------------------------------------------------------------ 
    # Create VIEW FORM 
    # ------------------------------------------------------------------------
    
    table_name = Tab['table']
    class_name = Tab['class']
    

    # GV 20190816 f2.write(    "from ..models import %s\n"                         % (class_name) )
    f2.write(    "from emtec.collector.db.Flask_models import %s\n"  % (class_name) )
    # GV 20190816 f2.write(    "from ..forms  import frm_%s,frm_%s_delete\n"       % (class_name,class_name) )
    f2.write(    "from emtec.collector.forms  import frm_%s,frm_%s_delete\n"       % (class_name,class_name) )
    
    f.write(    "@main.route('/forms/%s', methods=['GET', 'POST'])\n"    % (table_name) )
    f.write(    "@login_required\n" )
    # 20190109 GV eliminated to allow users to "View" editing forms .... will avoid modifications later ....
    #f.write(    "@permission_required(Permission.DELETE)\n" )
    #f.write(    "@permission_required(Permission.MODIFY)\n" )
    Gen_Views_Permissions(Tab,f)
    f.write(    "def forms_%s():\n"%(table_name))
    f.write(    '    """ Form handling function for table %s """\n\n'% (table_name) )
    f.write(    "    logger.debug('Enter: forms_%s()')\n"           % (table_name) )

    for key in Tab['keys']:
        f.write(    "    %s  =  request.args.get('%s',0,type=int)\n"%(key,key))

    if Tab['has_parent']:
        f.write(    "    parent_key  =  request.args.get('parent_key',None,type=str)\n")
        f.write(    "    parent_value=  request.args.get('parent_value',0,type=int)\n\n")

    f.write(    "    row =  %s.query.filter(%s).first()\n"                  % (class_name,Tab['code']['key_filter']) )    

    f.write(    "    if row is None:\n")
    f.write(    "        row=%s()\n"                                        % (class_name) )    
    f.write(    "        session['is_new_row']=True\n\n"  )    

    f.write(    "    session['data'] =  {%s}\n"                             % (Tab['code']['dict_fields']) )

    if Tab['has_parent']:
        f.write(    "    if parent_key is not None:\n")
        f.write(    "       session['data'][parent_key] = parent_value\n\n")
        f.write(    "       print('parent_key  = ',parent_key)\n")
        f.write(    "       print('parent_value= ',parent_value)\n")    
        f.write(    "       print('session[\"data\"][parent_key] = %s'%(parent_key,session['data'][parent_key]))\n\n")
                       
    f.write(    "    form = frm_%s()\n\n"                                   % (class_name) )

    if Tab['has_fks']:
        f.write(    "    if form.has_FKs:\n")
        f.write(        "%s\n"%(Tab['code']['get_choices']))
    
            
    # Actual Form activation here
    f.write(        "    if form.validate_on_submit():\n")
    # Code for SAVE option
    # 20190109 GV f.write(        "        if     form.submit_Save.data:\n")
    f.write(        "        if     form.submit_Save.data and current_user.role_id>1:\n")
    for c in Tab['columns']:
        if not c['is_id'] and c['is_form_editable']:
            f.write("            row.%s = form.%s.data\n"                   % (c['field'],c['field']))
            
    f.write(        "            try:\n")

    f.write(        "               session['new_row']=str(row)\n")
    f.write(        "               db.session.close()\n")
    f.write(        "               db.session.add(row)\n")
    f.write(        "               db.session.commit()\n")

    f.write(        "               if session['is_new_row']==True:\n")
    f.write(        "                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )\n")
    f.write(        "                   flash('New %s created OK')\n"      % (Tab['entity']))
    f.write(        "               else:\n")
    f.write(        "                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )\n")
    f.write(        "                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )\n")
    
    f.write(        "                   message=Markup('<b>%s %%s saved OK</b>'%%(%s))\n"      % (Tab['entity'],Tab['code']['key_fields']))
    f.write(        "                   flash(message)\n")
    f.write(        "               db.session.close()\n")
    f.write(        "            except Exception as e:\n")
    f.write(        "               db.session.rollback()\n")
    f.write(        "               db.session.close()\n")
    f.write(        "               message=Markup('ERROR saving %s record : %%s'%%(e))\n" % (Tab['entity'])    )
    f.write(        "               flash(message)\n")
    f.write(        "            return redirect(url_for('.select_%s_query'))\n"  % (table_name))    

    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
    f.write(        "        elif   form.submit_New.data and current_user.role_id>1:\n")
    f.write(        "            #print('New Data Here ...')\n")
    f.write(        "            session['is_new_row']=True\n")        
    f.write(        "            db.session.close()\n")
    f.write(        "            row=%s()\n"                                % (class_name))
    if Tab['primary_key_auto_increment'] != '':
        f.write(        "            return redirect(url_for('.forms_%s',%s=row.%s))\n\n"%(table_name,Tab['primary_key_auto_increment'], \
                    Tab['primary_key_auto_increment']))    
    else:
        f.write(        "            return redirect(url_for('.forms_%s'))\n\n"%(table_name,))    
    
    # Code for CANCEL option 
    f.write(        "        elif   form.submit_Cancel.data:\n")
    f.write(        "            #print('Cancel Data Here ... does nothing')\n")
    f.write(        "            message=Markup('%s Record modifications discarded ...')\n"%(Tab['entity']))
    f.write(        "            flash(message)\n")

    # Code for ANY OTHER option should never get here
    f.write(        "        else:\n")
    f.write(        "            #print('form validated but not submited ???')\n")
    f.write(        "            message=Markup('<b>%s data modifications not allowed for user \\'%%s\\'. Please contact Collector\\'s Administrator ...</b>'%%(current_user.username))\n"%(Tab['entity'],))    
    f.write(        "            flash(message)\n")
    if Tab['primary_key_auto_increment'] != '':
        f.write(        "            return redirect(url_for('.forms_%s',%s=row.%s))\n\n"%(table_name,Tab['primary_key_auto_increment'], \
                    Tab['primary_key_auto_increment']))    
    else:
        f.write(        "            return redirect(url_for('.forms_%s'))\n\n"%(table_name))    
    
    for c in Tab['columns']:
        if not c['is_id'] and c['is_form_editable']:
            f.write("    form.%s.data = row.%s\n"%(c['field'],c['field']))            
    f.write(        "    session['prev_row']=str(row)\n")
    f.write(        "    session['is_new_row']=False\n")    
    f.write(        "    return render_template('%s.html', form=form, row=row)\n\n"%(table_name.lower()))    
    f.write(Dash)

