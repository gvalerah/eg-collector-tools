# Flask required modules
#from flask import render_template, session, redirect, url_for, current_app, flash
from flask                  import render_template, session, redirect, url_for, current_app, flash
from flask_wtf              import Form
from wtforms                import Field
from wtforms                import StringField, IntegerField, DecimalField, DateTimeField
from wtforms.fields.html5   import DateField
from wtforms                import BooleanField, SelectField, SubmitField, RadioField
from wtforms.validators     import Required, AnyOf, DataRequired, Email, EqualTo, HostnameValidation
from wtforms.validators     import IPAddress, InputRequired, Length, MacAddress, NoneOf, NumberRange, Optional
from wtforms.validators     import Regexp, Required

def pi_1000000_0(data):
    print("enter: pi_1000000.py:pi_1000000_0()"
    print("%s: ***************"%__name__)
    print("%s: pi_1000000 0 IN"%__name__)
    print("%s: ***************"%__name__)
    print("Campo 1 =",data[0]['form'].Campo1)
    print("Campo 2 =",data[0]['form'].Campo2)
    #file_name='Billing_Resume_14_2018-11-01_2018-11-30_1.pdf'
    file_name='CR_21_2018-04-01_2018-04-30_1_UF.pdf'
    data[0]['redirect']=url_for('static',filename='tmp/%s'%(file_name))
    flash('file %s exported OK'%(file_name))
    return data

def pi_1000000_1(data):
    print("enter: pi_1000000.py:pi_1000000_1()"
    print("%s: ***************"%__name__)
    print("%s: pi_1000000 1 IN"%__name__)
    print("%s: ***************"%__name__)
    data[0]['redirect']='/plugins'
    return data
    
class frm_pi_1000000(Form):
    Campo1      = StringField('Campo de Prueba 1 - Solo para Demo')
    Campo2      = StringField('Campo de Prueba 2 - Solo para Demo')
    
    submits     = 2
    submit_0    = SubmitField('Export')
    submit_1    = SubmitField('Cancel')
    
    functions   = []
    functions.append(pi_1000000_0)
    functions.append(pi_1000000_1)
       
def pi_1000000(data):
    print("enter: pi_1000000.py:pi_1000000()"
    data.append({'code':1000000,'description':'Reporte de Billing en UF (AR)','form':frm_pi_1000000()})
    print("data=",data)
    return data

