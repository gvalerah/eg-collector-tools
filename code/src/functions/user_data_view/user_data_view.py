# =============================================================================
# View for User Data in Tree structure
# (c) Sertechno 2018,2019
# GLVH @ 2019-01-11
# =============================================================================

# view required imports
import json
from pprint import pprint

# view required functions

img='xxx'

def load_children(DATA,children):
        cc_counter=0
        for child in children:
            #print("%s: child=%s"%(__name__,child))
            DATA.append({'cc_id':child.CC_Id,'cc_code':child.CC_Code,'cc_description':child.CC_Description,'children':[],'ci_list':[]})
            # Load CIs
            query=db.session.query(configuration_item.CI_Id,configuration_item.CI_Name).filter(configuration_item.CC_Id==child.CC_Id)
            CIS=query.all()
            ci_counter=0
            for ci in CIS:
                DATA[cc_counter]['ci_list'].append({'ci_id':ci.CI_Id,'ci_name':ci.CI_Name,'cu_list':[]})
                # Load CUs
                #query=db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).filter(charge_unit.CI_Id==ci.CI_Id)
                query=db.session.query(charge_unit).filter(charge_unit.CI_Id==ci.CI_Id)
                CUS=query.all()
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
            
            # Look for more children
            query=db.session.query(cost_center).filter(cost_center.CC_Parent_Code==child.CC_Code,cost_center.CC_Code!=cost_center.CC_Parent_Code)
            list_children_cc=query.all()
            #print("%s: list_children_cc=%s"%(__name__,list_children_cc))
            if len(list_children_cc)>0:
                load_children(DATA[cc_counter]['children'],list_children_cc)
            cc_counter+=1

def render_ci(ci,f,level):
    img='<img src="/static/img/edit.png" width="32" height="32" title="" alt="Details">'
    indent="  "*level
    M='<font color="white">%s</font>'%("MM"*level)
    cu_list_name="cul_%s"%ci['ci_id']
    # If there is CUs
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
        href="/forms/Configuration_Items?CI_Id=%s"%ci['ci_id']
        f.write('%s%s<a href="%s" target="_blank">Configuration Item: %s %s</a><br>\n'% (indent*3,M*2, href, ci['ci_name'],img) )                     

def render_children(DATA,f,level=1):
    img='<img src="/static/img/edit.png" width="32" height="32" title="" alt="Details">'
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

    USER=current_user.id

    user_cc=db.session.query(User.CC_Id).filter(User.id==USER).scalar() 
    list_cc=db.session.query(cost_center).filter(cost_center.CC_Id==user_cc).all() 

    DATA={}
    DATA.update({'user':{'user_id':USER},'cc_id':list_cc[0].CC_Id,'cc_code':list_cc[0].CC_Code,'cc_description':list_cc[0].CC_Description,'children':[]})

    #print("Children=",DATA['children'])
    #print("list_cc=",list_cc)

    load_children(DATA['children'],list_cc)
    #print("DATA=",DATA)

    #filename="tmp/%s_%s_user_data_tree.html"%(current_user.id,id(current_user.id))
    filename="tmp/%s_user_data_tree.html"%(current_user.id)
    try:
        f=open("/%s"%filename,'w')
    except Exception as e:
        message=("Couldn't open file: '%s'. Please inform administrator. EXCEPTION: %s"%(filename,e))
        flash(message)
        logger.error(message)
        return render_template("exception.html",filename=filename,data=DATA)

    
#  generate HTML

    render_children(DATA,f)
   
    f.close()
    
    return render_template("user_data_view.html",filename=filename,data=DATA)

# =============================================================================

