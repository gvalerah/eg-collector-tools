# =============================================================================
# View for User Data in Tree structure
# (c) Sertechno 2018,2019
# GLVH @ 2019-01-11
# =============================================================================

# view required imports
import os
import json
from pprint import pprint,pformat

# view required functions

img='xxx'

def load_children(PARENT,DATA,children,parent=0):
        cc_counter=0
        for child in children:
            DATA.append({
                'cc_id':child.CC_Id,
                'cc_code':child.CC_Code,
                'cc_description':child.CC_Description,
                'children':[],
                'ci_list':[],
                'ci_count':0,
                'parent':parent
                })
            # Load CIs
            query = db.session.query(
                        configuration_item.CI_Id,configuration_item.CI_Name
                        ).filter(configuration_item.CC_Id==child.CC_Id)
            CIS = query.all()
            ci_counter = 0
            for ci in CIS:
                DATA[cc_counter]['ci_list'].append({
                    'ci_id'   : ci.CI_Id,
                    'ci_name' : ci.CI_Name,
                    'cu_list' : []
                    })
                # Load CUs
                query = db.session.query(charge_unit
                            ).filter(charge_unit.CI_Id==ci.CI_Id)
                CUS = query.all()
                for cu in CUS:
                    ref=''
                    if cu.CU_UUID is not None:
                        ref=    ( " / %s"%cu.CU_UUID.strip()        if (len( cu.CU_UUID.strip() ) > 0) else '')
                    if cu.CU_Reference_1 is not None:
                        ref=ref+( " / %s"%cu.CU_Reference_1.strip() if (len( cu.CU_Reference_1.strip() ) > 0) else '')
                    if cu.CU_Reference_2 is not None:
                        ref=ref+( " / %s"%cu.CU_Reference_2.strip() if (len( cu.CU_Reference_2.strip() ) > 0) else '')
                    if cu.CU_Reference_3 is not None:
                        ref=ref+( " / %s"%cu.CU_Reference_3.strip() if (len( cu.CU_Reference_3.strip() ) > 0) else '')
                    DATA[cc_counter]['ci_list'][ci_counter]['cu_list'].append({'cu_id':cu.CU_Id,'cu_description':cu.CU_Description,'cu_reference':ref})
                ci_counter+=1
            #DATA[cc_counter]['ci_count']    = len(DATA[cc_counter]['ci_list'])
            #PARENT['children']['ci_count'] += DATA[cc_counter]['ci_count']
            
            # Look for more children
            query = db.session.query(cost_center
                        ).filter(cost_center.CC_Parent_Code == child.CC_Code,
                                 cost_center.CC_Code        != cost_center.CC_Parent_Code
                        )
            list_children_cc = query.all()
            if len(list_children_cc)>0:
                load_children(DATA,DATA[cc_counter]['children'],list_children_cc)
            cc_counter+=1

def render_ci(ci,f,level,
    render_empty_ci=False   # renders CI if empty
    ):
    # setup Edit Icon as per actual static icon
    img='<img src="/static/img/search.png" width="32" height="32" title="" alt="Details">'
    # define accordeon indentation level lof current option
    indent="  "*level
    # Output Force/Write Whitespace indentation data
    M='<font color="white">%s</font>'%("MM"*level)
    cu_list_name="cul_%s"%ci['ci_id']
    # If there is CUs, this is the deepest level, define if "renderizable")
    if len(ci['cu_list']):
        href="/forms/Configuration_Items?CI_Id=%s"%ci['ci_id']
        if ci['ci_id'] == 1:
            href='#'
            img=''
        f.write('%s%s<button type="button" class="btn btn-link" data-toggle="collapse" data-target="#%s">Configuration Item: %s (%s Charge Units)</button><a href="%s"  target="_blank">%s</a><br>\n'%\
                            (indent*3,M*2, cu_list_name, ci['ci_name'], len(ci['cu_list']),href,img))
                            
        f.write('%s<div id="%s" class="collapse">\n'%(indent*4,cu_list_name))
        for cu in ci['cu_list']:
            href="/forms/Charge_Units?CU_Id=%s"%cu['cu_id']
            if cu['cu_id'] == 1:
                f.write('%s%sCharge Unit: %s %s<br>\n'%(indent*5,M*3,cu['cu_description'],cu['cu_reference']))
            else:
                f.write('%s%s<a href="%s" target="_blank">Charge Unit: %s %s</a><br>\n'%(indent*5,M*3,href,cu['cu_description'],cu['cu_reference']))
                            
        f.write("%s</div>"%(indent*4))
    else:
        if render_empty_ci:
            href="/forms/Configuration_Items?CI_Id=%s"%ci['ci_id']
            f.write('%s%s<a href="%s" target="_blank">Configuration Item: %s %s</a><br>\n'% (indent*3,M*2, href, ci['ci_name'],img) )                     

def render_children(DATA,f,level=1,
    render_empty_cc=False
    ):
    img='<img src="/static/img/search.png" width="32" height="32" title="" alt="Details">'
    child_counter=0
    indent="  "*level
    M='<font color="white">%s</font>'%("MM"*level)
    cc_list_name="ccl_%s"%id(DATA['children'])
    for child in DATA['children']:
        # If there's CIs
        if len(child['ci_list'])>0:
            href="/forms/Cost_Centers?CC_Id=%s"%child['cc_id']
            ci_list_name="cil_%s"%child['cc_id']
            if child['cc_id'] == 1:
                f.write('%s%s'
                    '<button type="button" class="btn btn-link" data-toggle="collapse" data-target="#%s">Cost Center: %s %s (%s Configuration Items)</button>'
                    '<a href="%s" target="_blank">%s</a><br>\n'%\
                     (indent,M, 
                      ci_list_name, child['cc_code'], child['cc_description'], len(child['ci_list']),
                      "#",""))
            else:
                f.write('%s%s'
                    '<button type="button" class="btn btn-link" data-toggle="collapse" data-target="#%s">Cost Center: %s %s (%s Configuration Items)</button>'
                    '<a href="%s" target="_blank">%s</a><br>\n'%\
                     (indent,M, 
                      ci_list_name, child['cc_code'], child['cc_description'], len(child['ci_list']),
                      href,img))
            f.write('%s<div id="%s" class="collapse">\n'%(indent*2,ci_list_name))
                
            for ci in child['ci_list']:
                render_ci(ci,f,level)
            f.write("%s</div>"%(indent*2))
        else:
            if render_empty_cc:
                href="/forms/Cost_Centers?CC_Id=%s"%child['cc_id']
                f.write('<font color="white">%s%s__</font><a href="%s" target="_blank">Cost Center: %s %s</a><br>\n'%(indent,M, href, child['cc_code'], child['cc_description'])  )      
        if len(child['children'])>0:
            render_children(child,f,level+1)
        child_counter+=1        

    
@main.route('/forms/User_Data_View', methods=['GET'])
@login_required
@permission_required(Permission.CUSTOMER)
def forms_User_Data_View():
    logger.debug('Enter: forms_User_Data_View()'%())
    collectordata=get_collectordata()
        
    config_ini = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    if current_app.config.get('COLLECTOR_CONFIG_FILE'):
        config_ini.read( current_app.config.get('COLLECTOR_CONFIG_FILE') )        
        limit_user_cost_centers = config_ini.getboolean('Interface','limit_user_cost_centers',fallback=False)
    else:
        limit_user_cost_centers = False
        
    query = db.session.query(
            Configuration_Items.Cus_Id,
            Configuration_Items.CC_Id,
            Configuration_Items.CI_Id,
            Charge_Units.CU_Id,
            Charge_Units.Typ_Code,
            Cost_Centers.CC_Description,
            Configuration_Items.CI_Name,
            Charge_Units.CU_Description,
            Charge_Units.CU_Reference_1,
            Charge_Units.CU_Reference_2,
            Charge_Units.CU_Reference_3
            ).select_from(Charge_Units
            ).join( Configuration_Items,
                    Configuration_Items.CI_Id   == Charge_Units.CI_Id
            ).join( Cost_Centers,
                    Cost_Centers.CC_Id          == Configuration_Items.CC_Id
            ).filter(Charge_Units.Typ_Code.in_(('CPU','RAM','DSK','IMG')) # Este deberia ser la lista de permitidos OJO
            ).filter(Configuration_Items.CI_Name.notlike('NBUBVG%')
            ).filter(Configuration_Items.Cus_Id == current_user.cost_center.Cus_Id)

    # Limits CCs to user visible only, else all above users's cc id
    if limit_user_cost_centers:
        logger.info("limiting user cost centers ....")
        USER_COST_CENTERS = db.get_user_cost_centers(current_user.id)
        query = query.filter(Configuration_Items.CC_Id.in_(USER_COST_CENTERS))
    else:
        query = query.filter(Configuration_Items.CC_Id  >= current_user.cost_center.CC_Id) # Este deberia ser la lista de permitidos OJO
    rows = query.order_by( Cost_Centers.CC_Description,
                        Configuration_Items.CI_Name,
                        Charge_Units.CU_Description
            ).all()

    return render_template("user_data_view_new.html",rows=rows)



"""
    # Data will be a map with structured Cost Centers details
    DATA={}
    DATA.update({
        'user'          : {'user_id':USER},
        'cc_id'         : list_cc[0].CC_Id,
        'cc_code'       : list_cc[0].CC_Code,
        'cc_description': list_cc[0].CC_Description,
        'children'      : [],
        'ci_count'      : 0,
        })

    # will populate DATA with detaisl from childrens list
    # starts with top CC only
    load_children(DATA,DATA['children'],list_cc)
    '''
    print("***********************************************************")
    print("***********************************************************")
    #pprint(DATA)
    with open("/home/gvalera/COMPARTIDO/loco.json","w") as fp:
        fp.write(json.dumps(DATA))
    print("***********************************************************")
    print("***********************************************************")
    for x in DATA['children']:
        if x['ci_count']>0 or x['parent']>0:
            print(x)
    '''
    # Temporary tree file name, will be unique for user
    filename="tmp/%s_user_data_tree.html"%(current_user.id)
    try:
        # if previos version exists, then its removed
        if os.path.exists(f"/{filename}"):
            os.remove(f"/{filename}")
        f=open(f"/{filename}",'w')
    except Exception as e:
        message=("Couldn't open file: '%s'. Please inform administrator. EXCEPTION: %s"%(filename,e))
        flash(message)
        logger.error(message)
        # renders exception if required
        return render_template("exception.html",filename=filename,data=DATA)
        
#  generate HTML

    render_children(DATA,f)
   
    f.close()
    
    print("forms_User_Data_View(): filename=",filename)
    
    # Actual output rendering
    return render_template("user_data_view.html",filename=filename,data=DATA)
"""
# =============================================================================

@main.route('/forms/User_Data_View_OLD', methods=['GET'])
@login_required
@permission_required(Permission.CUSTOMER)
def forms_User_Data_View_OLD():
    logger.debug('Enter: forms_User_Data_View()'%())
    collectordata=get_collectordata()

    USER              = current_user.id
    

    # Get CC of current User (Top Level CC for all query effects)
    user_cc = db.session.query(User.CC_Id).filter(User.id==USER).scalar()
    # Populates list with actual User's Top Cost Center attributes (must be one only) 
    list_cc = db.session.query(cost_center).filter(cost_center.CC_Id==user_cc).all() 



    # Data will be a map with structured Cost Centers details
    DATA={}
    DATA.update({
        'user'          : {'user_id':USER},
        'cc_id'         : list_cc[0].CC_Id,
        'cc_code'       : list_cc[0].CC_Code,
        'cc_description': list_cc[0].CC_Description,
        'children'      : [],
        'ci_count'      : 0,
        })

    # will populate DATA with detaisl from childrens list
    # starts with top CC only
    load_children(DATA,DATA['children'],list_cc)
    '''
    print("***********************************************************")
    print("***********************************************************")
    #pprint(DATA)
    with open("/home/gvalera/COMPARTIDO/loco.json","w") as fp:
        fp.write(json.dumps(DATA))
    print("***********************************************************")
    print("***********************************************************")
    for x in DATA['children']:
        if x['ci_count']>0 or x['parent']>0:
            print(x)
    '''
    # Temporary tree file name, will be unique for user
    filename="tmp/%s_user_data_tree.html"%(current_user.id)
    try:
        # if previos version exists, then its removed
        if os.path.exists(f"/{filename}"):
            os.remove(f"/{filename}")
        f=open(f"/{filename}",'w')
    except Exception as e:
        message=("Couldn't open file: '%s'. Please inform administrator. EXCEPTION: %s"%(filename,e))
        flash(message)
        logger.error(message)
        # renders exception if required
        return render_template("exception.html",filename=filename,data=DATA)
        
#  generate HTML

    render_children(DATA,f)
   
    f.close()
    
    print("forms_User_Data_View(): filename=",filename)
    
    # Actual output rendering
    return render_template("user_data_view.html",filename=filename,data=DATA)

# =============================================================================

