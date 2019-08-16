# Flask required modules
from flask_wtf              import FlaskForm as Form
from wtforms                import Field
from wtforms                import StringField, IntegerField, DecimalField, DateTimeField
from wtforms                import StringField, IntegerField, DecimalField, DateTimeField
from wtforms_components     import TimeField
from wtforms.fields.html5   import DateField
from wtforms                import BooleanField, SelectField, SubmitField, RadioField
from wtforms.validators     import Required, AnyOf, DataRequired, Email, EqualTo, HostnameValidation
from wtforms.validators     import IPAddress, InputRequired, Length, MacAddress, NoneOf, NumberRange, Optional
from wtforms.validators     import Regexp, Required

