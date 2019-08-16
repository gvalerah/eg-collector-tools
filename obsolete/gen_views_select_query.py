# General variables
from gen.gen_functions      import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja

def Gen_Views_Select_Query(Tab,f):

    table_name = Tab['table']
    class_name = Tab['class']
    
    # ------------------------------------------------------------------------    
    # Create SELECT QUERY VIEWER (PAGINATED)
    # ------------------------------------------------------------------------    
    f.write(    "@main.route('/select/%s_Query', methods=['GET','POST'])\n"                                                 % (table_name) )
    f.write(    "def select_%s_query():\n"                                                                                  % (table_name) )
    f.write(    "    logger.debug('Enter: select_%s()')\n"                                                                  % (table_name) )
    
    f.write(    "    field =  request.args.get('field',None,type=str)\n")
    f.write(    "    value =  request.args.get('value',0,type=str)\n")
    
    f.write(    "    print('%s: query=%s'%(__name__,query))\n")
    
    f.write(    "    page =  request.args.get('page',1,type=int)\n")
    f.write(    "    if field is not None:\n")
    for c in Tab['columns']:    
        f.write("        if field == '%s':\n"%(c['field']))
        f.write("            rows =  %s.query.filter_by(%s=value)" \
            ".paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)\n"                             % (class_name,c['field']) )
    f.write(    "    else:\n")
    f.write(    "       rows =  %s.query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)\n"  % (class_name) )
    f.write(    "    next_url = url_for('.select_%s_query', page=rows.next_num) \\\n"                                       % (table_name) )
    f.write(    "        if rows.has_next else None\n")
    f.write(    "    prev_url = url_for('.select_%s_query', page=rows.prev_num) \\\n"                                       % (table_name) )
    f.write(    "        if rows.has_prev else None\n")
    f.write(    "    return render_template('%s_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)\n" % \
                    (table_name.lower()))
    f.write(Dash)
    
