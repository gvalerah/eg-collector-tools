# =============================================================================
# View for Graphic os Use per Type
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_graph_use_per_type_filter
from babel.numbers  import format_number, format_decimal, format_percent
from emtec.collector.common.stats_functions    import RunningStats

@main.route('/forms/Get_Graph_Stats_Per_Type_Filter', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Get_Graph_Stats_Per_Type_Filter():
    logger.debug('Enter: forms_Get_Graph_Stats_Per_Type_Filter()'%())

    form = frm_graph_use_per_type_filter()
    
    form.Graph.choices      = [ (1,"Lineal"), (2,"Bars"), (3,"Min Max") ]
    form.Type.choices       = db.session.query(cu_type.Typ_Code,cu_type.Typ_Description).order_by(cu_type.Typ_Description).all()
    form.Field.choices      = [ (1,"Count"), (2,"Mean"), (3,"Use") ]

    form.Customer.choices   = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()
    form.Platform.choices   = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
    form.CC.choices         = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
    form.CI.choices         = db.session.query(configuration_item.CI_Id,configuration_item.CI_Name).order_by(configuration_item.CI_Name).all()

    form.Estimation.choices = [ (0,"None"),
                                (1,"Lineal"),
                                (2,"Season"),
                                (3,"Lineal Adjusted by Season"),
                                (4,"Lineal Adjusted by Season w/RLs")
                              ]
   
       
    if form.validate_on_submit():
        if     form.submit_Report.data:
            #print("CU Type=",form.Type.data,"len",len(form.Type.data))
            session['data'] = { 'graph':form.Graph.data,
                        'year':form.Year.data,
                        'from':form.From.data,
                        'to':form.To.data,
                        'type':form.Type.data,
                        'field':form.Field.data,
                        'customer':form.Customer.data,
                        'platform':form.Platform.data,
                        'cc':form.CC.data,
                        'ci':form.CI.data,
                        'estimation':form.Estimation.data }
            return redirect(url_for('.report_Graph_Use_Per_Type_Filter'
                                ))

        elif   form.submit_Cancel.data:
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Get_User_Resume'))


    return render_template('graph_use_per_type_filter.html',form=form)

# =============================================================================

import simplejson as json
import matplotlib.pyplot as plt
import numpy as np
import calendar
import tempfile
from   ..common.stats_functions import Regression_Line

@main.route('/report/Graph_Use_Per_Type_Filter', methods=['GET','POST'])
@login_required
@admin_required
def report_Graph_Use_Per_Type_Filter():
    logger.debug('Enter: report_Stats_Use_Per_Type_Filter()')
    
    tmp_name="tmp_name"
    tmp_path="tmp_path"
    actual=[]
    estimate=[]
    months=0

    query = db.session.query(st_use_per_type).filter(\
                st_use_per_type.Year    ==session['data']['year'],
                st_use_per_type.Month   >=session['data']['from'],
                st_use_per_type.Month   <=session['data']['to'],
                st_use_per_type.Typ_Code==session['data']['type'],
                st_use_per_type.Cus_Id  ==session['data']['customer'],
                st_use_per_type.Pla_Id  ==session['data']['platform'],
                st_use_per_type.CC_Id   ==session['data']['cc'],
                st_use_per_type.CI_Id   ==session['data']['ci']                
                )\
                .order_by(st_use_per_type.Year,st_use_per_type.Month)

    try:
        rows=query.all()
    except Exception as e:
        flash(e)
        rows=None
         
    # Initialize data vectors
    actual=[]
    estimate=[]
    for i in range(12):
        actual.append(0)
        
    # Load Actual Data vector with selected field
    session['data']['afield']='Count'
    session['data']['rs']=RunningStats()   # This will be use to captyre running statistics 
    for row in rows:
        if session['data']['field'] == 1:
            actual[row.Month-1] = row.Count
            session['data']['afield']='Count' 
        elif session['data']['field'] == 2:
            actual[row.Month-1] = float(row.Mean)
            session['data']['afield']='Mean' 
        elif session['data']['field'] == 3:
            actual[row.Month-1] = float(row.Count*row.Mean) 
            session['data']['afield']='Use' 
        else:
            actual[row.Month-1]=row.Count
            session['data']['afield']='Count' 
        session['data']['rs'].push(actual[row.Month-1])
    
    # Appropiate try/except blocks should be include here, any error should be reported and defaults considered
            
    session['data']['cutype']  = db.session.query(cu_type.Typ_Description).filter(cu_type.Typ_Code==session['data']['type']).scalar()
    session['data']['cusname'] = db.session.query(customer.Cus_Name).filter(customer.Cus_Id==session['data']['customer']).scalar()
    session['data']['planame'] = db.session.query(platform.Pla_Name).filter(platform.Pla_Id==session['data']['platform']).scalar()
    session['data']['ccname']  = db.session.query(cost_center.CC_Description).filter(cost_center.CC_Id==session['data']['cc']).scalar()
    session['data']['ciname']  = db.session.query(configuration_item.CI_Name).filter(configuration_item.CI_Id==session['data']['ci']).scalar()
 
    # MU defaults to Unit, should be repleced with variable MU depending on DB
    # MU will be allways UNT for field Count
    # MU will depend on DB for fields Mean & Use
    session['data']['mu']='UNT'
    # special cases follows
    if (session['data']['type'] in ('DSK','RAM')) and (session['data']['afield'] in ('Mean','Use')):
            session['data']['mu']='GB'
    
    # Prepare some presentation parameters
    dias = [np.array(calendar.mdays)[0:i].sum() + 1 for i in np.arange(12)+1]  # Para generar el lugar del primer días de cada mes en un año
    months = calendar.month_abbr[1:13]  # Creamos una lista con los nombres abreviados de los meses
    months12=months
    months24=months+months
    """
    for i in range(0,len(months12)):
        months12[i]=months12[i][0:3]
    for i in range(0,len(months24)):
        months24[i]=months24[i][0:3]
    """    
       
    # Ge Data here from parameters
    
    # Force Demo Data

    suptitle = "%s of %s (%s/%s-%s/%s)"%(session['data']['afield'],session['data']['cutype'],
                                months12[session['data']['from']-1],
                                session['data']['year'],
                                months12[session['data']['to']-1],
                                session['data']['year'],
                                )

    title=''
    
    estimate=[]
    session['data']['coeficients_yx']=None
    session['data']['coeficients_yx2']=None
    # As Data is Know, diferent graphic and forecasts can be generated, defaults to Lineal Regression Proyection

    if session['data']['estimation']==1:
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        session['data']['coeficients_yx']=RL.get_yx_coeficients()
        title='Lineal proyection for %s'%(session['data']['year']+1)
    elif session['data']['estimation']==2:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            if actual[i-1] != 0:
                v=(actual[i]-actual[i-1])/actual[i-1]
            else:
                v=0
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        previous=actual[11]
        for i in range(0,len(actual)):
            estimate.append(previous*(1+var[i]))
            previous=estimate[i]
            
        title='Season proyection for %s'%(session['data']['year']+1)
    elif session['data']['estimation']==3:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            if actual[i-1] != 0:
                v=(actual[i]-actual[i-1])/actual[i-1]
            else:
                v=0
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        session['data']['coeficients_yx']=RL.get_yx_coeficients()

        for i in range(0,len(actual)):
            estimate[i]=estimate[i]*(1+var[i])
            
        title='Lineal proyection adjusted by season for %s'%(session['data']['year']+1)
    elif session['data']['estimation']==4:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            if actual[i-1] != 0:
                v=(actual[i]-actual[i-1])/actual[i-1]
            else:
                v=0
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        session['data']['coeficients_yx']=RL.get_yx_coeficients()

        for i in range(0,len(actual)):
            estimate[i]=estimate[i]*(1+var[i])
            
        title='Lineal proyection adjusted by season w/RLs for %s'%(session['data']['year']+1)
        Data=actual+estimate
        RLLine1=RL.estimate_y(0,23)
        RL2         =   Regression_Line(Data)
        RLLine2=RL2.estimate_y(0,23)
        session['data']['coeficients_yx2']=RL2.get_yx_coeficients()
        
         
    else:
        pass
        #estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        #title='MV durante 2018'
    
    #print("Data 2018",actual)
    #print("Data 2019",estimate)

    
    # Variation to use auto-deletable temporary file names
    
    fp = tempfile.mkstemp(   suffix='.png',
                            dir='%s%s'%(    current_app.root_path,
                                            url_for('static',filename='tmp')
                                        )
                        )
                        
    tmp_path    =   fp[1]
    tmp_name    =   fp[1].split('/app/static/tmp/')[1]
        
    
    # Plot Data here to temporary file
    # Generate Graphic here    

    # Data is designed to report estimation for next year as a continuation of actual 2018's data
    Data=actual+estimate
    for i in range(0,len(actual)-1):
        Data[i]=None

    # Creates Figura: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html
    fig = plt.figure(figsize=[12,9])
    
    # Get current size
    #fig_size = plt.rcParams["figure.figsize"]
    # Prints: [8.0, 6.0]
    #print ("Current size:", fig_size)
 
    # Set figure width to 12 and height to 9
    #fig_size=[12,9]
    #fig_size[0] = 12
    #fig_size[1] = 9
    #plt.rcParams["figure.figsize"] = fig_size

    # Get current size
    fig_size = plt.rcParams["figure.figsize"]
    # Prints: [8.0, 6.0]
    #print ("Current size:", fig_size)
    
    ax=fig.gca()
    ax.clear()
    
    if session['data']['graph']==1:
        ax.plot(actual,'b',label='Actual')
    elif session['data']['graph']==2:
        #index = np.arange(n_groups)
        index = np.arange(len(actual))
        bar_width = 0.70
        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        #std_actual = (0,1,2,3,4,5,6,7,8,9,10,11)
        ax.bar( index,actual,bar_width,
                alpha=opacity, color='b',
                #yerr=std_actual, error_kw=error_config,
                label='Actual')

    else:
        ax.plot(actual,'b')
    
    
    if session['data']['estimation'] > 0: 
        ax.plot(Data,'r:',label="Estimation")
    
    if session['data']['estimation']==4:
        ax.plot(RLLine1,'b-',linewidth='0.5') 
        ax.plot(RLLine2,'r--',linewidth='0.5')
    
    # Customize the grid

    # Turn on the minor TICKS, which are required for the minor GRID
    ax.minorticks_on()

    # Customize the major grid
    ax.grid(which='major', linestyle='--', linewidth='0.5', color='gray')
    # Customize the minor grid
    ax.grid(which='minor', linestyle=':', linewidth='0.25', color='gray')    

    ax.legend()
    #fig.tight_layout()

    plt.suptitle(suptitle)
    plt.title(title)
    plt.xlabel('Period')
    plt.ylabel('%s of %s (%s)'%(session['data']['afield'],session['data']['cutype'],session['data']['mu']))
    
        
    if session['data']['estimation'] > 0: 
        xticks=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        plt.xticks(xticks, months24, size = 'small', color = 'b', rotation = 45)  # Etiquetas, meses, en las posiciones, dias, con color azul y rotadas 45º
    else:
        xticks=[0,1,2,3,4,5,6,7,8,9,10,11]
        plt.xticks(xticks, months12, size = 'small', color = 'b', rotation = 45)  # Etiquetas, meses, en las posiciones, dias, con color azul y rotadas 45º

    #plt.show()
    
    plt.savefig(tmp_path)
    plt.close
    return render_template('show_graph_use_per_type_filter.html',
                        filename=tmp_name,
                        actual=actual,
                        estimate=estimate,
                        #Year=Year,
                        months=months,
                        Data=session['data']
                )

