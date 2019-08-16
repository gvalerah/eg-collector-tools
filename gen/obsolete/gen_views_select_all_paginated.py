# General variables
from gen.gen_functions      import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja

def Gen_Views_Select_All_Paginated(Tab,f):

    table_name = Tab['table']
    class_name = Tab['class']

    # ------------------------------------------------------------------------    
    # Create SELECT ALL VIEWER (PAGINATED)
    # ------------------------------------------------------------------------    
    f.write(    "@main.route('/select/%s', methods=['GET','POST'])\n"                                                                       % (table_name)  )
    f.write(    "@login_required\n"  )
    f.write(    "def select_%s():\n"                                                                                                        % (table_name)  )
    f.write(    "    logger.debug('Enter: select_%s()')\n"                                                                                  % (table_name)  )
    
    f.write(    "    field =  request.args.get('field',None,type=str)\n")
    f.write(    "    value =  request.args.get('value',0,type=str)\n")
    
    f.write(    "    page =  request.args.get('page',1,type=int)\n")
    f.write(    "    print('%s: page=%d'%(__name__,page))\n")
    f.write(    "    if field is not None:\n")
    f.write(    "       rows =  %s.query\\\n"                                                                                               % (class_name))
    if Tab['has_relations']:
        f.write(                   "%s"                                                                                                   % (Tab['code']['my_joins']))
    f.write(    "               .filter_by(query).paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)\n"                    )
    f.write(    "    else:\n")
    f.write(    "       rows =  %s.query\\\n"                                                                                               % (class_name)  )
    if Tab['has_relations']:
        f.write(                   "%s"                                                                                                   % (Tab['code']['my_joins']))
    f.write(    "               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)\n"                    )
    f.write(    "    next_url = url_for('.select_%s', page=rows.next_num) \\\n"                                                             % (table_name)  )
    f.write(    "        if rows.has_next else None\n")
    f.write(    "    prev_url = url_for('.select_%s', page=rows.prev_num) \\\n"                                                             % (table_name)  )
    f.write(    "        if rows.has_prev else None\n")
    f.write(    "    return render_template('%s_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)\n"                       % \
                     (table_name.lower()))
    f.write(Dash)

"""
           
        for r in range(len(RELATIONS)):
            rel=RELATIONS[r]
            if rel[1] == table_name and rel[2] == c['field']:
                xrel=str(", db.ForeignKey('%s.%s')"%(rel[4],rel[2]))   # rel[4] = Referenced Table rel[2] = FK field
                Tab['code']['my_relations'].append((rel[4],rel[2]))
                Tab['code']['my_joins'] = Tab['code']['my_joins'] + ".join(%s)"%rel[4]
                Tab['has_relations'] = True
                break
                
  rates = rate.query\
            .join(cu_type       ,rate.Typ_Code   == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
            .join(customer      ,rate.Cus_Id     == customer.Cus_Id).add_columns(customer.Cus_Name)\
            .join(platform      ,rate.Pla_Id     == platform.Pla_Id).add_columns(platform.Pla_Name)\
            .join(cost_center   ,rate.CC_Id      == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
            .join(charge_unit   ,rate.CU_Id      == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
            .join(currency      ,rate.Cur_Code   == currency.Cur_Code).add_columns(currency.Cur_Name)\
            .join(measure_unit  ,rate.MU_Code    == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
            .join(rat_period    ,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\

for r in rates:
    print((r))
    #print("r 0  ---------->",(r[0]))
    print("r 0 Rat_Id ---->",(r[0].Rat_Id))
    print("r 1  ---------->",(r[1]))
    print("r 2  ---------->",(r[2]))
    print("r 3  ---------->",(r[3]))
    print("r 4  ---------->",(r[4]))
    print("r 5  ---------->",(r[5]))
    print("r 0 Rat_Price ->",(r[0].Rat_Price))
    print("r 6  ---------->",(r[6]))
    print("r 7  ---------->",(r[7]))
    print("r 8  ---------->",(r[8]))
"""
              
                
