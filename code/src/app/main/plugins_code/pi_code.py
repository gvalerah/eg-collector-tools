# Flask required modules
from flask_wtf              import Form
from wtforms                import Field
from wtforms                import StringField, IntegerField, DecimalField, DateTimeField
from wtforms.fields.html5   import DateField
from wtforms                import BooleanField, SelectField, SubmitField, RadioField
from wtforms.validators     import Required, AnyOf, DataRequired, Email, EqualTo, HostnameValidation
from wtforms.validators     import IPAddress, DataRequired, Length, MacAddress, NoneOf, NumberRange, Optional
from wtforms.validators     import Regexp, Required


def pi_main(data):
    data.append({'code':1000000,'description':'Mi descripcion desde pi_1000000.py en __init__.py','form':None})
    print("%s: data = %s",(__name__,data))
    return data
    
    
class frm_pi_1000000(Form):
    Campo1 = StringField('Campo de Prueba 1')
    Campo2 = StringField('Campo de Prueba 2')
    Boton1 = SubmitField('Save')
    Boton2 = SubmitField('Cancel')


def pi_1000000(data):
    data.append({'code':1000000,'description':'Mi descripcion','form':frm_pi_1000000()})
    print("data=",data)
    return data

def pi_1000013(data):
    data.append({'code':1000013,'description':'Mi descripcion','form':None})
    return data

def pi_1000027(data):
    data.append({'code':1000027,'description':'Mi descripcion','form':None})
    return data

