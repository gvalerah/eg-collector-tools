# ------------------------------------------------ 
# Models File
# Static File. 
# GLVH 2018-11-23
# ------------------------------------------------
from .                      import db
from datetime               import datetime

from sqlalchemy             import Column, String, Integer, Numeric, Date, Time, Boolean
from sqlalchemy             import ForeignKey

from flask_sqlalchemy       import SQLAlchemy
from copy                   import copy, deepcopy
# Flask required modules
from flask_wtf              import Form
from wtforms                import Field
from wtforms                import StringField, IntegerField, DecimalField, DateTimeField
from wtforms.fields.html5   import DateField
from wtforms                import BooleanField, SelectField, SubmitField, RadioField
from wtforms.validators     import Required, AnyOf, DataRequired, Email, EqualTo, HostnameValidation
from wtforms.validators     import IPAddress, InputRequired, Length, MacAddress, NoneOf, NumberRange, Optional
from wtforms.validators     import Regexp, Required
# Required form Authorization subsystem
from werkzeug.security      import generate_password_hash, check_password_hash
from itsdangerous           import TimedJSONWebSignatureSerializer as Serializer
from flask                  import current_app
from flask_login            import UserMixin, AnonymousUserMixin
from .                      import login_manager
# ------------------------------------------------


