# General variables
from gen.gen_functions      import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja
from gen.gen_functions      import Gen_Views_Permissions

def Gen_Views_Select_Query(Tab,f):

    table_name = Tab['table']
    class_name = Tab['class']
    
    # ------------------------------------------------------------------------    
    # Create SELECT QUERY VIEWER (PAGINATED)
    # ------------------------------------------------------------------------    
    f.write(    "@main.route('/select/%s_Query', methods=['GET','POST'])\n"                 % (table_name))
    f.write(    "@login_required\n")
    Gen_Views_Permissions(Tab,f)
    f.write(    "def select_%s_query():\n"                                                  % (table_name))
    f.write(    '    """ Select rows handling function for table %s """\n\n'                % (table_name) )
    f.write(    "    logger.debug('Enter: select_%s_query()')\n"                            % (table_name) )
    # Get parameters from URL call
    f.write(    "    field =  request.args.get('field',None,type=str)\n")
    f.write(    "    value =  request.args.get('value',0,type=str)\n")
    f.write(    "    page  =  request.args.get('page',1,type=int)\n\n")
    
    has_filter=False
    # if some filter is required
    f.write(    "    if field is not None:\n")
    xif='if'
    for c in Tab['columns']:    
        f.write("        %-4s field == '%s':\n"%(xif,c['field']))
        f.write("            rows =  %s.query.filter_by(%s=value)\\\n"                      % (class_name,c['field']))
        # include required JOINS to get referenced values as added columns to query result
        if Tab['has_relations'] and Tab['gen_foreign_fields']: # GV 20181130
            f.write(            "%s"                                                        % (Tab['code']['my_joins']))
        f.write("               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)\n")
        xif='elif'
            
    # else select all will be required
    f.write(    "    else:\n")
    f.write(    "       rows =  %s.query\\\n"                                               % (class_name))
    if Tab['has_relations']:
        f.write(               "%s"                                                         % (Tab['code']['my_joins']))
    f.write(    "               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)\n")
    
    f.write(    "\n")
    # Pagination required variables
    f.write(    "    if field is not None:\n")
    f.write(    "       next_url = url_for('.select_%s_query', field=field, value=value, page=rows.next_num) \\\n"       % (table_name))
    f.write(    "           if rows.has_next else None\n")
    f.write(    "       prev_url = url_for('.select_%s_query', field=field, value=value, page=rows.prev_num) \\\n"       % (table_name))
    f.write(    "           if rows.has_prev else None\n\n")
    f.write(    "    else:\n")
    f.write(    "       next_url = url_for('.select_%s_query', page=rows.next_num) \\\n"       % (table_name))
    f.write(    "           if rows.has_next else None\n")
    f.write(    "       prev_url = url_for('.select_%s_query', page=rows.prev_num) \\\n"       % (table_name))
    f.write(    "           if rows.has_prev else None\n\n")
        
    #f.write(    "    return render_template('%s_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)\n" % \
    #                (table_name.lower()))
    #f.write(    "    return render_template('%s_All.html',rows=rows.items,next_url=next_url,prev_url=prev_url)\n" % \
    #                (table_name.lower()))
    f.write(    "    return render_template('%s_All.html',rows=rows)\n" % \
                    (table_name.lower()))
    f.write(Dash)
    
