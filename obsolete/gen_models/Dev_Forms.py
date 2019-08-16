# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-13 10:26:02
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

from db.base import Base

class Dev_Forms(Base):
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
    Length            = Column( Integer )
    Validation        = Column( Boolean )
    Validation_Type   = Column( String(45) )
    Validation_String = Column( String(128) )
    Caption_String    = Column( String(45) )
    Field_Order       = Column( Integer )
    Field_Format      = Column( String(45) )
    Form_Editable     = Column( Boolean )

"""


    def __init__(self, Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String):
        self.set( Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String)
    def __repr__(self):
        return "<Forms( Id='%s', Table='%s', Field='%s', Type='%s', Null='%s', Key='%s', Default='%s', Extra='%s', Foreign_Key='%s', Referenced_Table='%s', Foreign_Field='%s', Length='%s', Validation='%s', Validation_Type='%s', Validation_String='%s', Caption_String='%s')>" % \
                ( self.Id, self.Table, self.Field, self.Type, self.Null, self.Key, self.Default, self.Extra, self.Foreign_Key, self.Referenced_Table, self.Foreign_Field, self.Length, self.Validation, self.Validation_Type, self.Validation_String, self.Caption_String)

    def __copy__(self):
        return type(self)( self.Id, self.Table, self.Field, self.Type, self.Null, self.Key, self.Default, self.Extra, self.Foreign_Key, self.Referenced_Table, self.Foreign_Field, self.Length, self.Validation, self.Validation_Type, self.Validation_String, self.Caption_String)

    def __deepcopy__(self, memo): # memo is a dict of id's to copies
        id_self = id(self)        # memoization avoids unnecesary recursion
        _copy = memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self.Id                , memo)
                ,deepcopy(self.Table             , memo)
                ,deepcopy(self.Field             , memo)
                ,deepcopy(self.Type              , memo)
                ,deepcopy(self.Null              , memo)
                ,deepcopy(self.Key               , memo)
                ,deepcopy(self.Default           , memo)
                ,deepcopy(self.Extra             , memo)
                ,deepcopy(self.Foreign_Key       , memo)
                ,deepcopy(self.Referenced_Table  , memo)
                ,deepcopy(self.Foreign_Field     , memo)
                ,deepcopy(self.Length            , memo)
                ,deepcopy(self.Validation        , memo)
                ,deepcopy(self.Validation_Type   , memo)
                ,deepcopy(self.Validation_String , memo)
                ,deepcopy(self.Caption_String    , memo)
                )
            memo[id_self] = _copy
        return _copy

    def set(self, Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String):
        self.Id                = Id
        self.Table             = Table
        self.Field             = Field
        self.Type              = Type
        self.Null              = Null
        self.Key               = Key
        self.Default           = Default
        self.Extra             = Extra
        self.Foreign_Key       = Foreign_Key
        self.Referenced_Table  = Referenced_Table
        self.Foreign_Field     = Foreign_Field
        self.Length            = Length
        self.Validation        = Validation
        self.Validation_Type   = Validation_Type
        self.Validation_String = Validation_String
        self.Caption_String    = Caption_String

    def insert(self, Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String):
        self.set( Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        X = copy(self)
        session.add(X)
        session.commit()
        session.close()

    def merge(self, Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String):
        self.set( Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.merge()
        session.commit()
        session.close()

    def update(self, Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String):
        self.set( Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.query(Forms).filter(Forms.Id == Id).update({Forms.Table : Table,Forms.Field : Field,Forms.Type : Type,Forms.Null : Null,Forms.Key : Key,Forms.Default : Default,Forms.Extra : Extra,Forms.Foreign_Key : Foreign_Key,Forms.Referenced_Table : Referenced_Table,Forms.Foreign_Field : Foreign_Field,Forms.Length : Length,Forms.Validation : Validation,Forms.Validation_Type : Validation_Type,Forms.Validation_String : Validation_String,Forms.Caption_String : Caption_String})
        session.commit()
        session.close()

    def delete(self,Id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.query(Forms).filter(Forms.Id == Id).delete()
        session.commit()
        session.close()

    def queryall(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            results = session.query(Forms).all()
        except exc.NoResultFound:
            results = None
        return results

    def queryone(self,Id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            results = session.query(Forms).filter(Forms.Id == Id).one()
        except exc.NoResultFound:
            results = None
        return results

    def queryjoin(self,Id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            results = session.query(Forms).filter(Forms.Id == Id).one()
        except exc.NoResultFound:
            results = None
        return results

    def inject_list(self,rows):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        for row in (rows):
            X = copy(self)
            for f in range(len(row)):
                X.Id                = row[0]
                X.Table             = row[1]
                X.Field             = row[2]
                X.Type              = row[3]
                X.Null              = row[4]
                X.Key               = row[5]
                X.Default           = row[6]
                X.Extra             = row[7]
                X.Foreign_Key       = row[8]
                X.Referenced_Table  = row[9]
                X.Foreign_Field     = row[10]
                X.Length            = row[11]
                X.Validation        = row[12]
                X.Validation_Type   = row[13]
                X.Validation_String = row[14]
                X.Caption_String    = row[15]
            session.add(X)
        session.commit()
        session.close()

    def inject_dict(self,rows):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        for row in (rows):
            X = copy(self)
            for f in range(len(row)):
                X.Id                = row['Id']
                X.Table             = row['Table']
                X.Field             = row['Field']
                X.Type              = row['Type']
                X.Null              = row['Null']
                X.Key               = row['Key']
                X.Default           = row['Default']
                X.Extra             = row['Extra']
                X.Foreign_Key       = row['Foreign_Key']
                X.Referenced_Table  = row['Referenced_Table']
                X.Foreign_Field     = row['Foreign_Field']
                X.Length            = row['Length']
                X.Validation        = row['Validation']
                X.Validation_Type   = row['Validation_Type']
                X.Validation_String = row['Validation_String']
                X.Caption_String    = row['Caption_String']
            session.add(X)
        session.commit()
        session.close()

# =============================================================================
class frm_Forms(Form):
    submit                    = SubmitField('Save')

    has_FKs                   = False
    FK_List                   = {}
    engine                    = None

"""
