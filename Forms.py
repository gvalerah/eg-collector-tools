# =============================================================================
# Static Model for Code Generation
# (c) Sertechno 2018
# GLVH @ 2018-12-15
# =============================================================================

from sqlalchemy            import Column, String, Integer, Numeric, Date, Time, Boolean
from sqlalchemy            import ForeignKey
from sqlalchemy.orm        import exc
from sqlalchemy.orm        import sessionmaker
from copy                  import copy, deepcopy
# Flask required modules
from flask_wtf             import Form
from wtforms               import Field
from wtforms               import StringField, IntegerField, DecimalField, DateField, DateTimeField
from wtforms               import BooleanField, SelectField, SubmitField, RadioField
from wtforms.validators    import Required, AnyOf, DataRequired, Email, EqualTo, HostnameValidation
from wtforms.validators    import IPAddress, InputRequired, Length, MacAddress, NoneOf, NumberRange, Optional
from wtforms.validators    import Regexp, Required

from Base import Base

class Forms(Base):
    __tablename__ = 'Dev_Forms'
    engine        = None

    Id                = Column( Integer, primary_key=True, autoincrement=True )
    Table             = Column( String(45) )
    Field             = Column( String(45) )
    Type              = Column( String(45) )
    Null              = Column( String(45) )
    Key               = Column( String(45) )
    Default           = Column( String(45) )
    Extra             = Column( String(45) )
    Foreign_Key       = Column( String(45) )
    Referenced_Table  = Column( String(45) )
    Foreign_Field     = Column( String(45) )
    Foreign_Value     = Column( String(45) )
    Length            = Column( Integer )
    Validation        = Column( Boolean )
    Validation_Type   = Column( String(45) )
    Validation_String = Column( String(128) )
    Caption_String    = Column( String(45) )
    Field_Order       = Column( Integer )
    Field_Format      = Column( String(45) )
    Form_Editable     = Column( Boolean )

