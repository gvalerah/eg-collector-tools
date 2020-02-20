# Flask required modules
from flask_wtf              import Form
from wtforms                import Field
from wtforms                import StringField, IntegerField, DecimalField, DateTimeField
from wtforms.fields.html5   import DateField
from wtforms                import BooleanField, SelectField, SubmitField, RadioField
from wtforms.validators     import Required, AnyOf, DataRequired, Email, EqualTo, HostnameValidation
from wtforms.validators     import IPAddress, InputRequired, Length, MacAddress, NoneOf, NumberRange, Optional
from wtforms.validators     import Regexp, Required

def pi_1000027_0(data):
    print("%s: ***************"%__name__)
    print("%s: pi_1000027 0 IN"%__name__)
    print("%s: ***************"%__name__)
    print("Campo 1 =",data[0]['form'].Campo1)
    print("Campo 2 =",data[0]['form'].Campo2)
    data[0]['redirect']='/plugins'
    return data

def pi_1000027_1(data):
    print("%s: ***************"%__name__)
    print("%s: pi_1000027 1 IN"%__name__)
    print("%s: ***************"%__name__)
    data[0]['redirect']='/plugins'
    return data
    
class frm_pi_1000027(Form):
    Campo1      = StringField('Campo de Prueba 1 - Solo para Demo')
    Campo2      = StringField('Campo de Prueba 2 - Solo para Demo')
    
    submits     = 2
    submit_0    = SubmitField('Save')
    submit_1    = SubmitField('Cancel')
    
    functions   = []
    functions.append(pi_1000027_0)
    functions.append(pi_1000027_1)
    
    
def pi_1000027(data):
    data.append({'code':1000027,'description':'Mi descripcion','form':frm_pi_1000027()})
    print("data=",data)
    return data

