# =============================================================================
# View for Graphic os Use per Type
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_graph_use_per_type
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Graph_Stats_Per_Type', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Get_Graph_Stats_Per_type():
    logger.debug('Enter: forms_Get_Graph_Stats_Per_Type()'%())

    form = frm_graph_use_per_type()
    
    form.Graph.choices   = [(1,"# de Máquinas Virtuales Anual y Proyección Lineal"),
                            (2,"# de Máquinas Virtuales Anual y Proyección estacional"),
                            (3,"# de Máquinas Virtuales Anual y Proyección lineal ajustada estacionalmente"),
                            (4,"# de Máquinas Virtuales Anual y Proyección lineal ajustada estacionalmente (c/LR)")
                           ]

    if form.validate_on_submit():
        if     form.submit_Report.data:

            return redirect(url_for('.report_Graph_Use_Per_Type',
                                Year            = form.Year.data,
                                Graph           = form.Graph.data
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_User_Resume'))


    return render_template('stats_use_per_type.html',form=form)

# =============================================================================

import simplejson as json
import matplotlib.pyplot as plt
import numpy as np
import calendar
from   ..common.stats_functions import Regression_Line

@main.route('/report/Graph_Use_Per_Type', methods=['GET','POST'])
@login_required
@admin_required
def report_Graph_Use_Per_Type():
    logger.debug('Enter: report_Stats_Use_Per_Type()')
    
    Year            =  request.args.get('Year',None,type=int)
    Graph           =  request.args.get('Graph',None,type=int)
        
    # Ge Data here from parameters
    
    # Force Demo Data
    actual      =   [170,210,223,285,301,285,310,260,280,240,320,260]
    estimate=[]


    # As Data is Know, diferent graphic and forecasts can be generated, defaults to Lineal Regression Proyection
    if Graph==1:
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        print("Coeficientes y/x =",RL.get_yx_coeficients())
        title='MV durante 2018 y proyección lineal para 2019'
    elif Graph==2:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            v=(actual[i]-actual[i-1])/actual[i-1]
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        previous=actual[11]
        print("var=",var,"len(var)=",len(var))
        for i in range(0,len(actual)):
            estimate.append(previous*(1+var[i]))
            previous=estimate[i]
            
        title='MV durante 2018 y proyección estacional para 2019'
    elif Graph==3:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            v=(actual[i]-actual[i-1])/actual[i-1]
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)

        for i in range(0,len(actual)):
            estimate[i]=estimate[i]*(1+var[i])
            
        title='MV durante 2018 y proyección lineal ajustada estacionalmente para 2019'
    elif Graph==4:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            v=(actual[i]-actual[i-1])/actual[i-1]
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)

        for i in range(0,len(actual)):
            estimate[i]=estimate[i]*(1+var[i])
            
        title='MV durante 2018 y proyección lineal ajustada estacionalmente para 2019'
        Data=actual+estimate
        RLLine1=RL.estimate_y(0,23)
        RL2         =   Regression_Line(Data)
        RLLine2=RL2.estimate_y(0,23)
        
         
    else:
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        title='MV durante 2018 y proyección lineal para 2019'
    
    print("Data 2018",actual)
    print("Data 2019",estimate)

    filename       =   "%s_stats_per_use_type_%s.png"%(current_user.id,id(actual))
    tmp_filename    =   "%s%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(filename)))
    
    print("filename=",filename)
    print("tmp_name=",tmp_filename)
    
    
    # Plot Data here to temporary file
    # Generate Graphic here    

    # Data is designed to report estimation for next year as a continuation of actual 2018's data
    Data=actual+estimate
    for i in range(0,len(actual)-1):
        Data[i]=None

    
    fig = plt.figure()
    ax=fig.gca()
    ax.clear()
    ax.plot(actual,'b') 
    ax.plot(Data,'r:')
    if Graph==4:
        ax.plot(RLLine1,'b-',linewidth='0.5') 
        ax.plot(RLLine2,'r--',linewidth='0.5')
    
    # Customize the grid

    # Turn on the minor TICKS, which are required for the minor GRID
    ax.minorticks_on()

    # Customize the major grid
    ax.grid(which='major', linestyle='--', linewidth='0.5', color='gray')
    # Customize the minor grid
    ax.grid(which='minor', linestyle=':', linewidth='0.25', color='gray')    

    plt.suptitle('Collector')
    plt.title(title)
    plt.xlabel('Periodo')
    plt.ylabel('# de Máquinas Virtuales')

    dias = [np.array(calendar.mdays)[0:i].sum() + 1 for i in np.arange(12)+1]  # Para generar el lugar del primer días de cada mes en un año
    months = calendar.month_name[1:13]  # Creamos una lista con los nombres de los meses
    months24=months+months
    for i in range(0,len(months24)):
        months24[i]=months24[i][0:3]
    xticks=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    plt.xticks(xticks, months24, size = 'small', color = 'b', rotation = 45)  # Colocamos las etiquetas, meses, en las posiciones, dias, con color azul y   rotadas 45º

    #plt.show()
    plt.savefig(tmp_filename)
    plt.close
    return render_template('show_graph_use_per_type.html',
                        filename=filename,
                        actual=actual,
                        estimate=estimate,
                        Year=Year,
                        months=months
                )

