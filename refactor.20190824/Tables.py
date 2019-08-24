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

class Tables(Base):
    __tablename__ = 'Dev_Tables'
    engine        = None

    Id                        = Column( Integer, primary_key=True, autoincrement=True )
    Name                      = Column( String(45) )
    Caption                   = Column( String(45) )
    Entity                    = Column( String(45) )
    Class_Name                = Column( String(45) )
    Child_Table               = Column( String(45) )
    Parent_Table              = Column( String(45) )
    Use_Pagination            = Column( Boolean )
    Use_Children_Pagination   = Column( Boolean )
    Generate_Form_One         = Column( Boolean )
    Generate_Form_All         = Column( Boolean )
    Generate_Form_Filter      = Column( Boolean )
    Generate_Children         = Column( Boolean )
    Generate_Foreign_Fields   = Column( Boolean )
    Permission_View           = Column( Boolean )
    Permission_Delete         = Column( Boolean )
    Permission_Modify         = Column( Boolean )
    Permission_Report         = Column( Boolean )
    Permission_Export         = Column( Boolean )
    Permission_View_Private   = Column( Boolean )
    Permission_Modify_Private = Column( Boolean )
    Permission_Administer     = Column( Boolean )

