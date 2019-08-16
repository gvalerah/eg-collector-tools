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


# ------------------------------------------------ 
# Models File
# Authorization subsystem. 
# Static File. 
# GLVH 2018-11-23
# ------------------------------------------------

class Permission:
    VIEW                = 0x01
    DELETE              = 0x02
    MODIFY              = 0x04
    REPORT              = 0x08
    EXPORT              = 0x10
    VIEW_PRIVATE        = 0x20
    MODIFY_PRIVATE      = 0x40
    ADMINISTER          = 0x80

class Role(db.Model):
    __tablename__   = 'Roles'
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(64), unique=True)
    default         = db.Column(db.Boolean, default=False, index=True)
    permissions     = db.Column(db.Integer)
    users           = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'Reporter': (   Permission.VIEW |
                            Permission.REPORT |
                            Permission.EXPORT, True),
            'Charger': (    Permission.VIEW |
                            Permission.DELETE |
                            Permission.MODIFY |
                            Permission.REPORT, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__   = 'Users'
    id              = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(64), unique=True, index=True)
    username        = db.Column(db.String(64), unique=True, index=True)
    role_id            = db.Column(db.Integer, db.ForeignKey('Roles.id'))
    password_hash   = db.Column(db.String(128))
    confirmed       = db.Column(db.Boolean, default=True)

    """
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role_id is None:
            if self.email == current_app.config['COLLECTOR_ADMIN']:
                self.role_id = Role.query.filter_by(permissions=0xff).first()
            if self.role_id is None:
                self.role_id = Role.query.filter_by(default=True).first()
    """
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['COLLECTOR_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def __repr__(self):
        return '<User %r role=%r>' % (self.username,self.role)


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# ------------------------------------------------
# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 18:28:25
# =============================================================================

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class charge_item(db.Model):
    __tablename__ = 'Charge_Items'
    CU_Id         = db.Column( db.Integer, db.ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    CIT_Date      = db.Column( db.Date, primary_key=True )
    CIT_Time      = db.Column( db.String(10), primary_key=True )
    CIT_Quantity  = db.Column( db.Numeric(20,6) )
    CIT_Status    = db.Column( db.Integer, db.ForeignKey('CIT_Statuses.CIT_Status') )
    CIT_Is_Active = db.Column( db.Boolean )


    def __init__(self, CU_Id=0, CIT_Date=None, CIT_Time=None, CIT_Quantity=0.000000, CIT_Status=0, CIT_Is_Active=0):
        self.CU_Id         = CU_Id
        self.CIT_Date      = CIT_Date
        self.CIT_Time      = CIT_Time
        self.CIT_Quantity  = CIT_Quantity
        self.CIT_Status    = CIT_Status
        self.CIT_Is_Active = CIT_Is_Active

    def __repr__(self):
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active)

# =============================================================================

class frm_charge_item(Form):
    CU_Id                 = SelectField  ("Charge Unit Id?", coerce=int, validators=[Required()])
    CIT_Date              = DateField    ("Date?", validators=[Required()], format='%Y-%m-%d')
    CIT_Time              = StringField  ("Time?", validators=[Required()])
    CIT_Quantity          = DecimalField ("Quantity?", validators=[Required()])
    CIT_Status            = SelectField  ("Status?", coerce=int, validators=[Required()])
    CIT_Is_Active         = BooleanField ("Is Active?")

    submit_Save           = SubmitField  ('Save')
    submit_New            = SubmitField  ('New')
    submit_Cancel         = SubmitField  ('Cancel')

    has_FKs               = True

# =============================================================================

class frm_charge_item_delete(Form):
    submit_Delete         = SubmitField  ('Delete')
    submit_Cancel         = SubmitField  ('Cancel')

# =============================================================================

class Charge_Items(Base):
    __tablename__ = 'Charge_Items'
    engine        = None

    CU_Id         = Column( Integer, ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    CIT_Date      = Column( Date, primary_key=True )
    CIT_Time      = Column( String(10), primary_key=True )
    CIT_Quantity  = Column( Numeric(20,6) )
    CIT_Status    = Column( Integer, ForeignKey('CIT_Statuses.CIT_Status') )
    CIT_Is_Active = Column( Boolean )

    def __init__(self, CU_Id, CIT_Date, CIT_Time, CIT_Quantity, CIT_Status, CIT_Is_Active):
        self.set( CU_Id, CIT_Date, CIT_Time, CIT_Quantity, CIT_Status, CIT_Is_Active)

    def __repr__(self):
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class charge_unit(db.Model):
    __tablename__ = 'Charge_Units'
    CU_Id                  = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CI_Id                  = db.Column( db.Integer, db.ForeignKey('Configuration_Items.CI_Id') )
    CU_Description         = db.Column( db.String(45) )
    CU_UUID                = db.Column( db.String(45) )
    CU_Is_Billeable        = db.Column( db.Boolean )
    CU_Is_Always_Billeable = db.Column( db.Boolean )
    CU_Quantity            = db.Column( db.Numeric(20,6) )
    CU_Operation           = db.Column( db.String(10), db.ForeignKey('CU_Operations.CU_Operation') )
    Typ_Code               = db.Column( db.String(10), db.ForeignKey('CU_Types.Typ_Code') )
    CC_Id                  = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    CIT_Generation         = db.Column( db.Integer, db.ForeignKey('CIT_Generations.CIT_Generation') )
    Rat_Id                 = db.Column( db.Integer )
    CU_Reference_1         = db.Column( db.String(45) )
    CU_Reference_2         = db.Column( db.String(45) )
    CU_Reference_3         = db.Column( db.String(45) )

    charge_items           = db.relationship('charge_item',backref='charge_unit')
    rates                  = db.relationship('rate',backref='charge_unit')

    def __init__(self, CU_Id=0, CI_Id=None, CU_Description='None', CU_UUID='None', CU_Is_Billeable=0, CU_Is_Always_Billeable=0, CU_Quantity=None, CU_Operation='None', Typ_Code='None', CC_Id=None, CIT_Generation=None, Rat_Id=None, CU_Reference_1='None', CU_Reference_2='None', CU_Reference_3='None'):
        self.CU_Id                  = CU_Id
        self.CI_Id                  = CI_Id
        self.CU_Description         = CU_Description
        self.CU_UUID                = CU_UUID
        self.CU_Is_Billeable        = CU_Is_Billeable
        self.CU_Is_Always_Billeable = CU_Is_Always_Billeable
        self.CU_Quantity            = CU_Quantity
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CC_Id                  = CC_Id
        self.CIT_Generation         = CIT_Generation
        self.Rat_Id                 = Rat_Id
        self.CU_Reference_1         = CU_Reference_1
        self.CU_Reference_2         = CU_Reference_2
        self.CU_Reference_3         = CU_Reference_3

    def __repr__(self):
        return "<Charge_Units( CU_Id='%s', CI_Id='%s', CU_Description='%s', CU_UUID='%s', CU_Is_Billeable='%s', CU_Is_Always_Billeable='%s', CU_Quantity='%s', CU_Operation='%s', Typ_Code='%s', CC_Id='%s', CIT_Generation='%s', Rat_Id='%s', CU_Reference_1='%s', CU_Reference_2='%s', CU_Reference_3='%s')>" % \
                ( self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CC_Id, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3)

# =============================================================================

class frm_charge_unit(Form):
    CI_Id                          = SelectField  ("Configuration Item Id?", coerce=int, validators=[Required()])
    CU_Description                 = StringField  ("Description?")
    CU_UUID                        = StringField  ("UUID?")
    CU_Is_Billeable                = BooleanField ("Is Billeable?")
    CU_Is_Always_Billeable         = BooleanField ("Is Always Billeable?")
    CU_Quantity                    = DecimalField ("Quantity?", validators=[Required()])
    CU_Operation                   = SelectField  ("Conversion Operation?", validators=[Required()])
    Typ_Code                       = SelectField  ("Type?", validators=[Required()])
    CC_Id                          = SelectField  ("Cost Center Id?", coerce=int, validators=[Required()])
    CIT_Generation                 = SelectField  ("Item Generation Type?", coerce=int, validators=[Required()])
    CU_Reference_1                 = StringField  ("Reference 1?")
    CU_Reference_2                 = StringField  ("Reference 2?")
    CU_Reference_3                 = StringField  ("Reference 3?")

    submit_Save                    = SubmitField  ('Save')
    submit_New                     = SubmitField  ('New')
    submit_Cancel                  = SubmitField  ('Cancel')

    has_FKs                        = True

# =============================================================================

class frm_charge_unit_delete(Form):
    submit_Delete                  = SubmitField  ('Delete')
    submit_Cancel                  = SubmitField  ('Cancel')

# =============================================================================

class Charge_Units(Base):
    __tablename__ = 'Charge_Units'
    engine        = None

    CU_Id                  = Column( Integer, primary_key=True, autoincrement=True )
    CI_Id                  = Column( Integer, ForeignKey('Configuration_Items.CI_Id') )
    CU_Description         = Column( String(45) )
    CU_UUID                = Column( String(45) )
    CU_Is_Billeable        = Column( Boolean )
    CU_Is_Always_Billeable = Column( Boolean )
    CU_Quantity            = Column( Numeric(20,6) )
    CU_Operation           = Column( String(10), ForeignKey('CU_Operations.CU_Operation') )
    Typ_Code               = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    CC_Id                  = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    CIT_Generation         = Column( Integer, ForeignKey('CIT_Generations.CIT_Generation') )
    Rat_Id                 = Column( Integer )
    CU_Reference_1         = Column( String(45) )
    CU_Reference_2         = Column( String(45) )
    CU_Reference_3         = Column( String(45) )

    def __init__(self, CU_Id, CI_Id, CU_Description, CU_UUID, CU_Is_Billeable, CU_Is_Always_Billeable, CU_Quantity, CU_Operation, Typ_Code, CC_Id, CIT_Generation, Rat_Id, CU_Reference_1, CU_Reference_2, CU_Reference_3):
        self.set( CU_Id, CI_Id, CU_Description, CU_UUID, CU_Is_Billeable, CU_Is_Always_Billeable, CU_Quantity, CU_Operation, Typ_Code, CC_Id, CIT_Generation, Rat_Id, CU_Reference_1, CU_Reference_2, CU_Reference_3)

    def __repr__(self):
        return "<Charge_Units( CU_Id='%s', CI_Id='%s', CU_Description='%s', CU_UUID='%s', CU_Is_Billeable='%s', CU_Is_Always_Billeable='%s', CU_Quantity='%s', CU_Operation='%s', Typ_Code='%s', CC_Id='%s', CIT_Generation='%s', Rat_Id='%s', CU_Reference_1='%s', CU_Reference_2='%s', CU_Reference_3='%s')>" % \
                ( self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CC_Id, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cit_generation(db.Model):
    __tablename__ = 'CIT_Generations'
    CIT_Generation = db.Column( db.Integer, primary_key=True )
    Value          = db.Column( db.String(45) )

    charge_units   = db.relationship('charge_unit',backref='cit_generation')
    configuration_items = db.relationship('configuration_item',backref='cit_generation')

    def __init__(self, CIT_Generation=None, Value='None'):
        self.CIT_Generation = CIT_Generation
        self.Value          = Value

    def __repr__(self):
        return "<CIT_Generations( CIT_Generation='%s', Value='%s')>" % \
                ( self.CIT_Generation, self.Value)

# =============================================================================

class frm_cit_generation(Form):
    CIT_Generation         = IntegerField ("CIT_Generation?", validators=[Required()])
    Value                  = StringField  ("Value?")

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = False

# =============================================================================

class frm_cit_generation_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================

class CIT_Generations(Base):
    __tablename__ = 'CIT_Generations'
    engine        = None

    CIT_Generation = Column( Integer, primary_key=True )
    Value          = Column( String(45) )

    def __init__(self, CIT_Generation, Value):
        self.set( CIT_Generation, Value)

    def __repr__(self):
        return "<CIT_Generations( CIT_Generation='%s', Value='%s')>" % \
                ( self.CIT_Generation, self.Value)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cit_status(db.Model):
    __tablename__ = 'CIT_Statuses'
    CIT_Status = db.Column( db.Integer, primary_key=True )
    Value      = db.Column( db.String(45) )

    charge_items = db.relationship('charge_item',backref='cit_status')

    def __init__(self, CIT_Status=None, Value='None'):
        self.CIT_Status = CIT_Status
        self.Value      = Value

    def __repr__(self):
        return "<CIT_Statuses( CIT_Status='%s', Value='%s')>" % \
                ( self.CIT_Status, self.Value)

# =============================================================================

class frm_cit_status(Form):
    CIT_Status         = IntegerField ("CIT Status?", validators=[Required()])
    Value              = StringField  ("Vallue?")

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = False

# =============================================================================

class frm_cit_status_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================

class CIT_Statuses(Base):
    __tablename__ = 'CIT_Statuses'
    engine        = None

    CIT_Status = Column( Integer, primary_key=True )
    Value      = Column( String(45) )

    def __init__(self, CIT_Status, Value):
        self.set( CIT_Status, Value)

    def __repr__(self):
        return "<CIT_Statuses( CIT_Status='%s', Value='%s')>" % \
                ( self.CIT_Status, self.Value)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class configuration_item(db.Model):
    __tablename__ = 'Configuration_Items'
    CI_Id          = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CI_Name        = db.Column( db.String(45) )
    CI_UUID        = db.Column( db.String(45) )
    Pla_Id         = db.Column( db.Integer, db.ForeignKey('Platforms.Pla_Id') )
    CC_Id          = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    CIT_Generation = db.Column( db.Integer, db.ForeignKey('CIT_Generations.CIT_Generation') )
    Cus_Id         = db.Column( db.Integer, db.ForeignKey('Customers.Cus_Id') )

    charge_units   = db.relationship('charge_unit',backref='configuration_item')

    def __init__(self, CI_Id=0, CI_Name='None', CI_UUID='None', Pla_Id=None, CC_Id=None, CIT_Generation=0, Cus_Id=1):
        self.CI_Id          = CI_Id
        self.CI_Name        = CI_Name
        self.CI_UUID        = CI_UUID
        self.Pla_Id         = Pla_Id
        self.CC_Id          = CC_Id
        self.CIT_Generation = CIT_Generation
        self.Cus_Id         = Cus_Id

    def __repr__(self):
        return "<Configuration_Items( CI_Id='%s', CI_Name='%s', CI_UUID='%s', Pla_Id='%s', CC_Id='%s', CIT_Generation='%s', Cus_Id='%s')>" % \
                ( self.CI_Id, self.CI_Name, self.CI_UUID, self.Pla_Id, self.CC_Id, self.CIT_Generation, self.Cus_Id)

# =============================================================================

class frm_configuration_item(Form):
    CI_Name                = StringField  ("Name?")
    CI_UUID                = StringField  ("UUID?")
    Pla_Id                 = SelectField  ("Platform Id?", coerce=int, validators=[Required()])
    CC_Id                  = SelectField  ("Cost Center Id?", coerce=int, validators=[Required()])
    CIT_Generation         = SelectField  ("Default Item Generation Type?", coerce=int, validators=[Required()])
    Cus_Id                 = SelectField  ("Customer Id?", coerce=int, validators=[Required()])

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = True

# =============================================================================

class frm_configuration_item_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================

class Configuration_Items(Base):
    __tablename__ = 'Configuration_Items'
    engine        = None

    CI_Id          = Column( Integer, primary_key=True, autoincrement=True )
    CI_Name        = Column( String(45) )
    CI_UUID        = Column( String(45) )
    Pla_Id         = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id          = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    CIT_Generation = Column( Integer, ForeignKey('CIT_Generations.CIT_Generation') )
    Cus_Id         = Column( Integer, ForeignKey('Customers.Cus_Id') )

    def __init__(self, CI_Id, CI_Name, CI_UUID, Pla_Id, CC_Id, CIT_Generation, Cus_Id):
        self.set( CI_Id, CI_Name, CI_UUID, Pla_Id, CC_Id, CIT_Generation, Cus_Id)

    def __repr__(self):
        return "<Configuration_Items( CI_Id='%s', CI_Name='%s', CI_UUID='%s', Pla_Id='%s', CC_Id='%s', CIT_Generation='%s', Cus_Id='%s')>" % \
                ( self.CI_Id, self.CI_Name, self.CI_UUID, self.Pla_Id, self.CC_Id, self.CIT_Generation, self.Cus_Id)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cost_center(db.Model):
    __tablename__ = 'Cost_Centers'
    CC_Id          = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CC_Code        = db.Column( db.String(45) )
    CC_Description = db.Column( db.String(45) )
    Cur_Code       = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )

    charge_units   = db.relationship('charge_unit',backref='cost_center')
    configuration_items = db.relationship('configuration_item',backref='cost_center')
    customers      = db.relationship('customer',backref='cost_center')
    rates          = db.relationship('rate',backref='cost_center')

    def __init__(self, CC_Id=0, CC_Code='None', CC_Description='None', Cur_Code='None'):
        self.CC_Id          = CC_Id
        self.CC_Code        = CC_Code
        self.CC_Description = CC_Description
        self.Cur_Code       = Cur_Code

    def __repr__(self):
        return "<Cost_Centers( CC_Id='%s', CC_Code='%s', CC_Description='%s', Cur_Code='%s')>" % \
                ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code)

# =============================================================================

class frm_cost_center(Form):
    CC_Code                = StringField  ("Code?")
    CC_Description         = StringField  ("Description?")
    Cur_Code               = SelectField  ("Currency Code?", validators=[Required()])

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = True

# =============================================================================

class frm_cost_center_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================

class Cost_Centers(Base):
    __tablename__ = 'Cost_Centers'
    engine        = None

    CC_Id          = Column( Integer, primary_key=True, autoincrement=True )
    CC_Code        = Column( String(45) )
    CC_Description = Column( String(45) )
    Cur_Code       = Column( String(3), ForeignKey('Currencies.Cur_Code') )

    def __init__(self, CC_Id, CC_Code, CC_Description, Cur_Code):
        self.set( CC_Id, CC_Code, CC_Description, Cur_Code)

    def __repr__(self):
        return "<Cost_Centers( CC_Id='%s', CC_Code='%s', CC_Description='%s', Cur_Code='%s')>" % \
                ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class country_currency(db.Model):
    __tablename__ = 'Countries_Currencies'
    Cou_Code        = db.Column( db.String(2), db.ForeignKey('Countries.Cou_Code'), primary_key=True )
    Cur_Code        = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code'), primary_key=True )
    Cou_Cur_Comment = db.Column( db.String(45) )


    def __init__(self, Cou_Code='None', Cur_Code='None', Cou_Cur_Comment='None'):
        self.Cou_Code        = Cou_Code
        self.Cur_Code        = Cur_Code
        self.Cou_Cur_Comment = Cou_Cur_Comment

    def __repr__(self):
        return "<Countries_Currencies( Cou_Code='%s', Cur_Code='%s', Cou_Cur_Comment='%s')>" % \
                ( self.Cou_Code, self.Cur_Code, self.Cou_Cur_Comment)

# =============================================================================

class frm_country_currency(Form):
    Cou_Code                = SelectField  ("Country Code?", validators=[Required()])
    Cur_Code                = SelectField  ("Currency Code?", validators=[Required()])
    Cou_Cur_Comment         = StringField  ("Comment?")

    submit_Save             = SubmitField  ('Save')
    submit_New              = SubmitField  ('New')
    submit_Cancel           = SubmitField  ('Cancel')

    has_FKs                 = True

# =============================================================================

class frm_country_currency_delete(Form):
    submit_Delete           = SubmitField  ('Delete')
    submit_Cancel           = SubmitField  ('Cancel')

# =============================================================================

class Countries_Currencies(Base):
    __tablename__ = 'Countries_Currencies'
    engine        = None

    Cou_Code        = Column( String(2), ForeignKey('Countries.Cou_Code'), primary_key=True )
    Cur_Code        = Column( String(3), ForeignKey('Currencies.Cur_Code'), primary_key=True )
    Cou_Cur_Comment = Column( String(45) )

    def __init__(self, Cou_Code, Cur_Code, Cou_Cur_Comment):
        self.set( Cou_Code, Cur_Code, Cou_Cur_Comment)

    def __repr__(self):
        return "<Countries_Currencies( Cou_Code='%s', Cur_Code='%s', Cou_Cur_Comment='%s')>" % \
                ( self.Cou_Code, self.Cur_Code, self.Cou_Cur_Comment)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class country(db.Model):
    __tablename__ = 'Countries'
    Cou_Code = db.Column( db.String(2), primary_key=True )
    Cou_Name = db.Column( db.String(45) )
    Cou_A3   = db.Column( db.String(3) )
    Cou_N    = db.Column( db.Integer )

    countries_currencies = db.relationship('country_currency',backref='country')

    def __init__(self, Cou_Code='None', Cou_Name='None', Cou_A3='None', Cou_N=None):
        self.Cou_Code = Cou_Code
        self.Cou_Name = Cou_Name
        self.Cou_A3   = Cou_A3
        self.Cou_N    = Cou_N

    def __repr__(self):
        return "<Countries( Cou_Code='%s', Cou_Name='%s', Cou_A3='%s', Cou_N='%s')>" % \
                ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)

# =============================================================================

class frm_country(Form):
    Cou_Code         = StringField  ("Code?", validators=[Required()])
    Cou_Name         = StringField  ("Name?")
    Cou_A3           = StringField  ("Alphanum Code?")
    Cou_N            = IntegerField ("ISO Numeric Code?")

    submit_Save      = SubmitField  ('Save')
    submit_New       = SubmitField  ('New')
    submit_Cancel    = SubmitField  ('Cancel')

    has_FKs          = False

# =============================================================================

class frm_country_delete(Form):
    submit_Delete    = SubmitField  ('Delete')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================

class Countries(Base):
    __tablename__ = 'Countries'
    engine        = None

    Cou_Code = Column( String(2), primary_key=True )
    Cou_Name = Column( String(45) )
    Cou_A3   = Column( String(3) )
    Cou_N    = Column( Integer )

    def __init__(self, Cou_Code, Cou_Name, Cou_A3, Cou_N):
        self.set( Cou_Code, Cou_Name, Cou_A3, Cou_N)

    def __repr__(self):
        return "<Countries( Cou_Code='%s', Cou_Name='%s', Cou_A3='%s', Cou_N='%s')>" % \
                ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cu_operation(db.Model):
    __tablename__ = 'CU_Operations'
    CU_Operation = db.Column( db.String(10), primary_key=True )
    Value        = db.Column( db.String(45) )
    Is_Multiply  = db.Column( db.Boolean )
    Factor       = db.Column( db.Integer )

    charge_units = db.relationship('charge_unit',backref='cu_operation')

    def __init__(self, CU_Operation='None', Value='None', Is_Multiply=None, Factor=None):
        self.CU_Operation = CU_Operation
        self.Value        = Value
        self.Is_Multiply  = Is_Multiply
        self.Factor       = Factor

    def __repr__(self):
        return "<CU_Operations( CU_Operation='%s', Value='%s', Is_Multiply='%s', Factor='%s')>" % \
                ( self.CU_Operation, self.Value, self.Is_Multiply, self.Factor)

# =============================================================================

class frm_cu_operation(Form):
    CU_Operation         = StringField  ("Operation?", validators=[Required()])
    Value                = StringField  ("Value?")
    Is_Multiply          = BooleanField ("Is Multiply?")
    Factor               = IntegerField ("Factor?")

    submit_Save          = SubmitField  ('Save')
    submit_New           = SubmitField  ('New')
    submit_Cancel        = SubmitField  ('Cancel')

    has_FKs              = False

# =============================================================================

class frm_cu_operation_delete(Form):
    submit_Delete        = SubmitField  ('Delete')
    submit_Cancel        = SubmitField  ('Cancel')

# =============================================================================

class CU_Operations(Base):
    __tablename__ = 'CU_Operations'
    engine        = None

    CU_Operation = Column( String(10), primary_key=True )
    Value        = Column( String(45) )
    Is_Multiply  = Column( Boolean )
    Factor       = Column( Integer )

    def __init__(self, CU_Operation, Value, Is_Multiply, Factor):
        self.set( CU_Operation, Value, Is_Multiply, Factor)

    def __repr__(self):
        return "<CU_Operations( CU_Operation='%s', Value='%s', Is_Multiply='%s', Factor='%s')>" % \
                ( self.CU_Operation, self.Value, self.Is_Multiply, self.Factor)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class currency(db.Model):
    __tablename__ = 'Currencies'
    Cur_Code    = db.Column( db.String(3), primary_key=True )
    Cur_Name    = db.Column( db.String(45) )
    Cur_Id      = db.Column( db.Integer )
    Cur_Comment = db.Column( db.String(128) )

    cost_centers = db.relationship('cost_center',backref='currency')
    countries_currencies = db.relationship('country_currency',backref='currency')
    exchange_rates = db.relationship('exchange_rate',backref='currency')
    rates       = db.relationship('rate',backref='currency')

    def __init__(self, Cur_Code='None', Cur_Name='None', Cur_Id=None, Cur_Comment='None'):
        self.Cur_Code    = Cur_Code
        self.Cur_Name    = Cur_Name
        self.Cur_Id      = Cur_Id
        self.Cur_Comment = Cur_Comment

    def __repr__(self):
        return "<Currencies( Cur_Code='%s', Cur_Name='%s', Cur_Id='%s', Cur_Comment='%s')>" % \
                ( self.Cur_Code, self.Cur_Name, self.Cur_Id, self.Cur_Comment)

# =============================================================================

class frm_currency(Form):
    Cur_Code            = StringField  ("Code?", validators=[Required()])
    Cur_Name            = StringField  ("Name?")
    Cur_Id              = IntegerField ("Id?")
    Cur_Comment         = StringField  ("Comment?")

    submit_Save         = SubmitField  ('Save')
    submit_New          = SubmitField  ('New')
    submit_Cancel       = SubmitField  ('Cancel')

    has_FKs             = False

# =============================================================================

class frm_currency_delete(Form):
    submit_Delete       = SubmitField  ('Delete')
    submit_Cancel       = SubmitField  ('Cancel')

# =============================================================================

class Currencies(Base):
    __tablename__ = 'Currencies'
    engine        = None

    Cur_Code    = Column( String(3), primary_key=True )
    Cur_Name    = Column( String(45) )
    Cur_Id      = Column( Integer )
    Cur_Comment = Column( String(128) )

    def __init__(self, Cur_Code, Cur_Name, Cur_Id, Cur_Comment):
        self.set( Cur_Code, Cur_Name, Cur_Id, Cur_Comment)

    def __repr__(self):
        return "<Currencies( Cur_Code='%s', Cur_Name='%s', Cur_Id='%s', Cur_Comment='%s')>" % \
                ( self.Cur_Code, self.Cur_Name, self.Cur_Id, self.Cur_Comment)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class customer(db.Model):
    __tablename__ = 'Customers'
    Cus_Id   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Cus_Name = db.Column( db.String(45) )
    CC_Id    = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )

    configuration_items = db.relationship('configuration_item',backref='customer')
    rates    = db.relationship('rate',backref='customer')

    def __init__(self, Cus_Id=0, Cus_Name='None', CC_Id=None):
        self.Cus_Id   = Cus_Id
        self.Cus_Name = Cus_Name
        self.CC_Id    = CC_Id

    def __repr__(self):
        return "<Customers( Cus_Id='%s', Cus_Name='%s', CC_Id='%s')>" % \
                ( self.Cus_Id, self.Cus_Name, self.CC_Id)

# =============================================================================

class frm_customer(Form):
    Cus_Name         = StringField  ("Name?")
    CC_Id            = SelectField  ("Cost Center Id?", coerce=int, validators=[Required()])

    submit_Save      = SubmitField  ('Save')
    submit_New       = SubmitField  ('New')
    submit_Cancel    = SubmitField  ('Cancel')

    has_FKs          = True

# =============================================================================

class frm_customer_delete(Form):
    submit_Delete    = SubmitField  ('Delete')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================

class Customers(Base):
    __tablename__ = 'Customers'
    engine        = None

    Cus_Id   = Column( Integer, primary_key=True, autoincrement=True )
    Cus_Name = Column( String(45) )
    CC_Id    = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )

    def __init__(self, Cus_Id, Cus_Name, CC_Id):
        self.set( Cus_Id, Cus_Name, CC_Id)

    def __repr__(self):
        return "<Customers( Cus_Id='%s', Cus_Name='%s', CC_Id='%s')>" % \
                ( self.Cus_Id, self.Cus_Name, self.CC_Id)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cu_type(db.Model):
    __tablename__ = 'CU_Types'
    Typ_Code        = db.Column( db.String(10), primary_key=True )
    Typ_Description = db.Column( db.String(45) )

    charge_units    = db.relationship('charge_unit',backref='cu_type')
    rates           = db.relationship('rate',backref='cu_type')

    def __init__(self, Typ_Code='None', Typ_Description='None'):
        self.Typ_Code        = Typ_Code
        self.Typ_Description = Typ_Description

    def __repr__(self):
        return "<CU_Types( Typ_Code='%s', Typ_Description='%s')>" % \
                ( self.Typ_Code, self.Typ_Description)

# =============================================================================

class frm_cu_type(Form):
    Typ_Code                = StringField  ("Type?", validators=[Required()])
    Typ_Description         = StringField  ("Description?")

    submit_Save             = SubmitField  ('Save')
    submit_New              = SubmitField  ('New')
    submit_Cancel           = SubmitField  ('Cancel')

    has_FKs                 = False

# =============================================================================

class frm_cu_type_delete(Form):
    submit_Delete           = SubmitField  ('Delete')
    submit_Cancel           = SubmitField  ('Cancel')

# =============================================================================

class CU_Types(Base):
    __tablename__ = 'CU_Types'
    engine        = None

    Typ_Code        = Column( String(10), primary_key=True )
    Typ_Description = Column( String(45) )

    def __init__(self, Typ_Code, Typ_Description):
        self.set( Typ_Code, Typ_Description)

    def __repr__(self):
        return "<CU_Types( Typ_Code='%s', Typ_Description='%s')>" % \
                ( self.Typ_Code, self.Typ_Description)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class exchange_rate(db.Model):
    __tablename__ = 'Exchange_Rates'
    ER_Id     = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Cur_Code  = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    ER_Factor = db.Column( db.Numeric(20,6) )
    ER_Date   = db.Column( db.Date )


    def __init__(self, ER_Id=0, Cur_Code='USD', ER_Factor=None, ER_Date=None):
        self.ER_Id     = ER_Id
        self.Cur_Code  = Cur_Code
        self.ER_Factor = ER_Factor
        self.ER_Date   = ER_Date

    def __repr__(self):
        return "<Exchange_Rates( ER_Id='%s', Cur_Code='%s', ER_Factor='%s', ER_Date='%s')>" % \
                ( self.ER_Id, self.Cur_Code, self.ER_Factor, self.ER_Date)

# =============================================================================

class frm_exchange_rate(Form):
    Cur_Code          = SelectField  ("Currency Code?", validators=[Required()])
    ER_Factor         = DecimalField ("Factor?", validators=[Required()])
    ER_Date           = DateField    ("Date?", format='%Y-%m-%d')

    submit_Save       = SubmitField  ('Save')
    submit_New        = SubmitField  ('New')
    submit_Cancel     = SubmitField  ('Cancel')

    has_FKs           = True

# =============================================================================

class frm_exchange_rate_delete(Form):
    submit_Delete     = SubmitField  ('Delete')
    submit_Cancel     = SubmitField  ('Cancel')

# =============================================================================

class Exchange_Rates(Base):
    __tablename__ = 'Exchange_Rates'
    engine        = None

    ER_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Cur_Code  = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    ER_Factor = Column( Numeric(20,6) )
    ER_Date   = Column( Date )

    def __init__(self, ER_Id, Cur_Code, ER_Factor, ER_Date):
        self.set( ER_Id, Cur_Code, ER_Factor, ER_Date)

    def __repr__(self):
        return "<Exchange_Rates( ER_Id='%s', Cur_Code='%s', ER_Factor='%s', ER_Date='%s')>" % \
                ( self.ER_Id, self.Cur_Code, self.ER_Factor, self.ER_Date)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class dev_form(db.Model):
    __tablename__ = 'Dev_Forms'
    Id                = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Table             = db.Column( db.String(45) )
    Field             = db.Column( db.String(45) )
    Type              = db.Column( db.String(45) )
    Null              = db.Column( db.String(45) )
    Key               = db.Column( db.String(45) )
    Default           = db.Column( db.String(45) )
    Extra             = db.Column( db.String(45) )
    Foreign_Key       = db.Column( db.String(45) )
    Referenced_Table  = db.Column( db.String(45) )
    Foreign_Field     = db.Column( db.String(45) )
    Foreign_Value     = db.Column( db.String(45) )
    Length            = db.Column( db.Integer )
    Validation        = db.Column( db.Boolean )
    Validation_Type   = db.Column( db.String(45) )
    Validation_String = db.Column( db.String(128) )
    Caption_String    = db.Column( db.String(45) )
    Field_Order       = db.Column( db.Integer )
    Field_Format      = db.Column( db.String(45) )
    Form_Editable     = db.Column( db.Boolean )


    def __init__(self, Id=0, Table='None', Field='None', Type='None', Null='None', Key='None', Default='None', Extra='None', Foreign_Key='None', Referenced_Table='None', Foreign_Field='None', Foreign_Value='None', Length=None, Validation=None, Validation_Type='None', Validation_String='None', Caption_String='None', Field_Order=None, Field_Format='None', Form_Editable=1):
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
        self.Foreign_Value     = Foreign_Value
        self.Length            = Length
        self.Validation        = Validation
        self.Validation_Type   = Validation_Type
        self.Validation_String = Validation_String
        self.Caption_String    = Caption_String
        self.Field_Order       = Field_Order
        self.Field_Format      = Field_Format
        self.Form_Editable     = Form_Editable

    def __repr__(self):
        return "<Dev_Forms( Id='%s', Table='%s', Field='%s', Type='%s', Null='%s', Key='%s', Default='%s', Extra='%s', Foreign_Key='%s', Referenced_Table='%s', Foreign_Field='%s', Foreign_Value='%s', Length='%s', Validation='%s', Validation_Type='%s', Validation_String='%s', Caption_String='%s', Field_Order='%s', Field_Format='%s', Form_Editable='%s')>" % \
                ( self.Id, self.Table, self.Field, self.Type, self.Null, self.Key, self.Default, self.Extra, self.Foreign_Key, self.Referenced_Table, self.Foreign_Field, self.Foreign_Value, self.Length, self.Validation, self.Validation_Type, self.Validation_String, self.Caption_String, self.Field_Order, self.Field_Format, self.Form_Editable)

# =============================================================================

class frm_dev_form(Form):
    Table                     = StringField  ("Table?")
    Field                     = StringField  ("Field?")
    Type                      = StringField  ("Type?")
    Null                      = StringField  ("Null?")
    Key                       = StringField  ("Key?")
    Default                   = StringField  ("Default?")
    Extra                     = StringField  ("Extra?")
    Foreign_Key               = StringField  ("Foreign Key?")
    Referenced_Table          = StringField  ("Referenced Table?")
    Foreign_Field             = StringField  ("Foreign Field?")
    Foreign_Value             = StringField  ("Foreign_Value?")
    Length                    = IntegerField ("Length?")
    Validation                = BooleanField ("Validation?")
    Validation_Type           = StringField  ("Validation Type?")
    Validation_String         = StringField  ("Validation String?")
    Caption_String            = StringField  ("Caption String?")
    Field_Order               = IntegerField ("Field Order?")
    Field_Format              = StringField  ("Field Format?")
    Form_Editable             = BooleanField ("Form Editable?")

    submit_Save               = SubmitField  ('Save')
    submit_New                = SubmitField  ('New')
    submit_Cancel             = SubmitField  ('Cancel')

    has_FKs                   = False

# =============================================================================

class frm_dev_form_delete(Form):
    submit_Delete             = SubmitField  ('Delete')
    submit_Cancel             = SubmitField  ('Cancel')

# =============================================================================

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
    Foreign_Value     = Column( String(45) )
    Length            = Column( Integer )
    Validation        = Column( Boolean )
    Validation_Type   = Column( String(45) )
    Validation_String = Column( String(128) )
    Caption_String    = Column( String(45) )
    Field_Order       = Column( Integer )
    Field_Format      = Column( String(45) )
    Form_Editable     = Column( Boolean )

    def __init__(self, Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Foreign_Value, Length, Validation, Validation_Type, Validation_String, Caption_String, Field_Order, Field_Format, Form_Editable):
        self.set( Id, Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Foreign_Value, Length, Validation, Validation_Type, Validation_String, Caption_String, Field_Order, Field_Format, Form_Editable)

    def __repr__(self):
        return "<Dev_Forms( Id='%s', Table='%s', Field='%s', Type='%s', Null='%s', Key='%s', Default='%s', Extra='%s', Foreign_Key='%s', Referenced_Table='%s', Foreign_Field='%s', Foreign_Value='%s', Length='%s', Validation='%s', Validation_Type='%s', Validation_String='%s', Caption_String='%s', Field_Order='%s', Field_Format='%s', Form_Editable='%s')>" % \
                ( self.Id, self.Table, self.Field, self.Type, self.Null, self.Key, self.Default, self.Extra, self.Foreign_Key, self.Referenced_Table, self.Foreign_Field, self.Foreign_Value, self.Length, self.Validation, self.Validation_Type, self.Validation_String, self.Caption_String, self.Field_Order, self.Field_Format, self.Form_Editable)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class measure_unit(db.Model):
    __tablename__ = 'Measure_Units'
    MU_Code        = db.Column( db.String(3), primary_key=True )
    MU_Description = db.Column( db.String(45) )

    rates          = db.relationship('rate',backref='measure_unit')

    def __init__(self, MU_Code='None', MU_Description='None'):
        self.MU_Code        = MU_Code
        self.MU_Description = MU_Description

    def __repr__(self):
        return "<Measure_Units( MU_Code='%s', MU_Description='%s')>" % \
                ( self.MU_Code, self.MU_Description)

# =============================================================================

class frm_measure_unit(Form):
    MU_Code                = StringField  ("Code?", validators=[Required()])
    MU_Description         = StringField  ("Description?")

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = False

# =============================================================================

class frm_measure_unit_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================

class Measure_Units(Base):
    __tablename__ = 'Measure_Units'
    engine        = None

    MU_Code        = Column( String(3), primary_key=True )
    MU_Description = Column( String(45) )

    def __init__(self, MU_Code, MU_Description):
        self.set( MU_Code, MU_Description)

    def __repr__(self):
        return "<Measure_Units( MU_Code='%s', MU_Description='%s')>" % \
                ( self.MU_Code, self.MU_Description)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class platform(db.Model):
    __tablename__ = 'Platforms'
    Pla_Id       = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Pla_Name     = db.Column( db.String(45) )
    Pla_Host     = db.Column( db.String(45) )
    Pla_Port     = db.Column( db.String(45) )
    Pla_User     = db.Column( db.String(45) )
    Pla_Password = db.Column( db.String(45) )

    configuration_items = db.relationship('configuration_item',backref='platform')
    rates        = db.relationship('rate',backref='platform')

    def __init__(self, Pla_Id=0, Pla_Name='None', Pla_Host='None', Pla_Port='None', Pla_User='None', Pla_Password='None'):
        self.Pla_Id       = Pla_Id
        self.Pla_Name     = Pla_Name
        self.Pla_Host     = Pla_Host
        self.Pla_Port     = Pla_Port
        self.Pla_User     = Pla_User
        self.Pla_Password = Pla_Password

    def __repr__(self):
        return "<Platforms( Pla_Id='%s', Pla_Name='%s', Pla_Host='%s', Pla_Port='%s', Pla_User='%s', Pla_Password='%s')>" % \
                ( self.Pla_Id, self.Pla_Name, self.Pla_Host, self.Pla_Port, self.Pla_User, self.Pla_Password)

# =============================================================================

class frm_platform(Form):
    Pla_Name             = StringField  ("Name?")
    Pla_Host             = StringField  ("Host?")
    Pla_Port             = StringField  ("Port?")
    Pla_User             = StringField  ("User?")
    Pla_Password         = StringField  ("Password?")

    submit_Save          = SubmitField  ('Save')
    submit_New           = SubmitField  ('New')
    submit_Cancel        = SubmitField  ('Cancel')

    has_FKs              = False

# =============================================================================

class frm_platform_delete(Form):
    submit_Delete        = SubmitField  ('Delete')
    submit_Cancel        = SubmitField  ('Cancel')

# =============================================================================

class Platforms(Base):
    __tablename__ = 'Platforms'
    engine        = None

    Pla_Id       = Column( Integer, primary_key=True, autoincrement=True )
    Pla_Name     = Column( String(45) )
    Pla_Host     = Column( String(45) )
    Pla_Port     = Column( String(45) )
    Pla_User     = Column( String(45) )
    Pla_Password = Column( String(45) )

    def __init__(self, Pla_Id, Pla_Name, Pla_Host, Pla_Port, Pla_User, Pla_Password):
        self.set( Pla_Id, Pla_Name, Pla_Host, Pla_Port, Pla_User, Pla_Password)

    def __repr__(self):
        return "<Platforms( Pla_Id='%s', Pla_Name='%s', Pla_Host='%s', Pla_Port='%s', Pla_User='%s', Pla_Password='%s')>" % \
                ( self.Pla_Id, self.Pla_Name, self.Pla_Host, self.Pla_Port, self.Pla_User, self.Pla_Password)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class rate(db.Model):
    __tablename__ = 'Rates'
    Rat_Id     = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Typ_Code   = db.Column( db.String(10), db.ForeignKey('CU_Types.Typ_Code') )
    Cus_Id     = db.Column( db.Integer, db.ForeignKey('Customers.Cus_Id') )
    Pla_Id     = db.Column( db.Integer, db.ForeignKey('Platforms.Pla_Id') )
    CC_Id      = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    CU_Id      = db.Column( db.Integer, db.ForeignKey('Charge_Units.CU_Id') )
    Rat_Price  = db.Column( db.Numeric(20,6) )
    Cur_Code   = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    MU_Code    = db.Column( db.String(3), db.ForeignKey('Measure_Units.MU_Code') )
    Rat_Period = db.Column( db.Integer, db.ForeignKey('Rat_Periods.Rat_Period') )
    Rat_Type   = db.Column( db.Integer )


    def __init__(self, Rat_Id=0, Typ_Code='None', Cus_Id=None, Pla_Id=None, CC_Id=None, CU_Id=None, Rat_Price=None, Cur_Code='None', MU_Code='None', Rat_Period=None, Rat_Type=None):
        self.Rat_Id     = Rat_Id
        self.Typ_Code   = Typ_Code
        self.Cus_Id     = Cus_Id
        self.Pla_Id     = Pla_Id
        self.CC_Id      = CC_Id
        self.CU_Id      = CU_Id
        self.Rat_Price  = Rat_Price
        self.Cur_Code   = Cur_Code
        self.MU_Code    = MU_Code
        self.Rat_Period = Rat_Period
        self.Rat_Type   = Rat_Type

    def __repr__(self):
        return "<Rates( Rat_Id='%s', Typ_Code='%s', Cus_Id='%s', Pla_Id='%s', CC_Id='%s', CU_Id='%s', Rat_Price='%s', Cur_Code='%s', MU_Code='%s', Rat_Period='%s', Rat_Type='%s')>" % \
                ( self.Rat_Id, self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CU_Id, self.Rat_Price, self.Cur_Code, self.MU_Code, self.Rat_Period, self.Rat_Type)

# =============================================================================

class frm_rate(Form):
    Typ_Code           = SelectField  ("Charge Unit Type?", validators=[Required()])
    Cus_Id             = SelectField  ("Customer Id?", coerce=int, validators=[Required()])
    Pla_Id             = SelectField  ("Platform Id?", coerce=int, validators=[Required()])
    CC_Id              = SelectField  ("Cost Center Id?", coerce=int, validators=[Required()])
    CU_Id              = SelectField  ("Charge Unit Id?", coerce=int, validators=[Required()])
    Rat_Price          = DecimalField ("Rate Price?", validators=[Required()])
    Cur_Code           = SelectField  ("Currency Code?", validators=[Required()])
    MU_Code            = SelectField  ("Measure Unit?", validators=[Required()])
    Rat_Period         = RadioField   ("Period?", coerce=int, validators=[Required()])

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = True

# =============================================================================

class frm_rate_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================

class Rates(Base):
    __tablename__ = 'Rates'
    engine        = None

    Rat_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Typ_Code   = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    Cus_Id     = Column( Integer, ForeignKey('Customers.Cus_Id') )
    Pla_Id     = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id      = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    CU_Id      = Column( Integer, ForeignKey('Charge_Units.CU_Id') )
    Rat_Price  = Column( Numeric(20,6) )
    Cur_Code   = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    MU_Code    = Column( String(3), ForeignKey('Measure_Units.MU_Code') )
    Rat_Period = Column( Integer, ForeignKey('Rat_Periods.Rat_Period') )
    Rat_Type   = Column( Integer )

    def __init__(self, Rat_Id, Typ_Code, Cus_Id, Pla_Id, CC_Id, CU_Id, Rat_Price, Cur_Code, MU_Code, Rat_Period, Rat_Type):
        self.set( Rat_Id, Typ_Code, Cus_Id, Pla_Id, CC_Id, CU_Id, Rat_Price, Cur_Code, MU_Code, Rat_Period, Rat_Type)

    def __repr__(self):
        return "<Rates( Rat_Id='%s', Typ_Code='%s', Cus_Id='%s', Pla_Id='%s', CC_Id='%s', CU_Id='%s', Rat_Price='%s', Cur_Code='%s', MU_Code='%s', Rat_Period='%s', Rat_Type='%s')>" % \
                ( self.Rat_Id, self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CU_Id, self.Rat_Price, self.Cur_Code, self.MU_Code, self.Rat_Period, self.Rat_Type)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class rat_period(db.Model):
    __tablename__ = 'Rat_Periods'
    Rat_Period = db.Column( db.Integer, primary_key=True )
    Value      = db.Column( db.String(45) )

    rates      = db.relationship('rate',backref='rat_period')

    def __init__(self, Rat_Period=None, Value='None'):
        self.Rat_Period = Rat_Period
        self.Value      = Value

    def __repr__(self):
        return "<Rat_Periods( Rat_Period='%s', Value='%s')>" % \
                ( self.Rat_Period, self.Value)

# =============================================================================

class frm_rat_period(Form):
    Rat_Period         = IntegerField ("Rate Period?", validators=[Required()])
    Value              = StringField  ("Value?")

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = False

# =============================================================================

class frm_rat_period_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================

class Rat_Periods(Base):
    __tablename__ = 'Rat_Periods'
    engine        = None

    Rat_Period = Column( Integer, primary_key=True )
    Value      = Column( String(45) )

    def __init__(self, Rat_Period, Value):
        self.set( Rat_Period, Value)

    def __repr__(self):
        return "<Rat_Periods( Rat_Period='%s', Value='%s')>" % \
                ( self.Rat_Period, self.Value)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class dev_table(db.Model):
    __tablename__ = 'Dev_Tables'
    Id                        = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Name                      = db.Column( db.String(45) )
    Caption                   = db.Column( db.String(45) )
    Entity                    = db.Column( db.String(45) )
    Class_Name                = db.Column( db.String(45) )
    Child_Table               = db.Column( db.String(45) )
    Parent_Table              = db.Column( db.String(45) )
    Use_Pagination            = db.Column( db.Boolean )
    Use_Children_Pagination   = db.Column( db.Boolean )
    Generate_Form_One         = db.Column( db.Boolean )
    Generate_Form_All         = db.Column( db.Boolean )
    Generate_Form_Filter      = db.Column( db.Boolean )
    Generate_Children         = db.Column( db.Boolean )
    Generate_Foreign_Fields   = db.Column( db.Boolean )
    Permission_View           = db.Column( db.Boolean )
    Permission_Delete         = db.Column( db.Boolean )
    Permission_Modify         = db.Column( db.Boolean )
    Permission_Report         = db.Column( db.Boolean )
    Permission_Export         = db.Column( db.Boolean )
    Permission_View_Private   = db.Column( db.Boolean )
    Permission_Modify_Private = db.Column( db.Boolean )
    Permission_Administer     = db.Column( db.Boolean )


    def __init__(self, Id=0, Name='None', Caption='None', Entity='None', Class_Name='None', Child_Table='None', Parent_Table='None', Use_Pagination=None, Use_Children_Pagination=None, Generate_Form_One=None, Generate_Form_All=None, Generate_Form_Filter=None, Generate_Children=None, Generate_Foreign_Fields=None, Permission_View=None, Permission_Delete=None, Permission_Modify=None, Permission_Report=None, Permission_Export=None, Permission_View_Private=None, Permission_Modify_Private=None, Permission_Administer=None):
        self.Id                        = Id
        self.Name                      = Name
        self.Caption                   = Caption
        self.Entity                    = Entity
        self.Class_Name                = Class_Name
        self.Child_Table               = Child_Table
        self.Parent_Table              = Parent_Table
        self.Use_Pagination            = Use_Pagination
        self.Use_Children_Pagination   = Use_Children_Pagination
        self.Generate_Form_One         = Generate_Form_One
        self.Generate_Form_All         = Generate_Form_All
        self.Generate_Form_Filter      = Generate_Form_Filter
        self.Generate_Children         = Generate_Children
        self.Generate_Foreign_Fields   = Generate_Foreign_Fields
        self.Permission_View           = Permission_View
        self.Permission_Delete         = Permission_Delete
        self.Permission_Modify         = Permission_Modify
        self.Permission_Report         = Permission_Report
        self.Permission_Export         = Permission_Export
        self.Permission_View_Private   = Permission_View_Private
        self.Permission_Modify_Private = Permission_Modify_Private
        self.Permission_Administer     = Permission_Administer

    def __repr__(self):
        return "<Dev_Tables( Id='%s', Name='%s', Caption='%s', Entity='%s', Class_Name='%s', Child_Table='%s', Parent_Table='%s', Use_Pagination='%s', Use_Children_Pagination='%s', Generate_Form_One='%s', Generate_Form_All='%s', Generate_Form_Filter='%s', Generate_Children='%s', Generate_Foreign_Fields='%s', Permission_View='%s', Permission_Delete='%s', Permission_Modify='%s', Permission_Report='%s', Permission_Export='%s', Permission_View_Private='%s', Permission_Modify_Private='%s', Permission_Administer='%s')>" % \
                ( self.Id, self.Name, self.Caption, self.Entity, self.Class_Name, self.Child_Table, self.Parent_Table, self.Use_Pagination, self.Use_Children_Pagination, self.Generate_Form_One, self.Generate_Form_All, self.Generate_Form_Filter, self.Generate_Children, self.Generate_Foreign_Fields, self.Permission_View, self.Permission_Delete, self.Permission_Modify, self.Permission_Report, self.Permission_Export, self.Permission_View_Private, self.Permission_Modify_Private, self.Permission_Administer)

# =============================================================================

class frm_dev_table(Form):
    Name                              = StringField  ("Name?")
    Caption                           = StringField  ("Caption?")
    Entity                            = StringField  ("Entity?")
    Class_Name                        = StringField  ("Class Name?")
    Child_Table                       = StringField  ("Child Table?")
    Parent_Table                      = StringField  ("Parent Table?")
    Use_Pagination                    = BooleanField ("Use Pagination?")
    Use_Children_Pagination           = BooleanField ("Use Children Pagination?")
    Generate_Form_One                 = BooleanField ("Generate Form One?")
    Generate_Form_All                 = BooleanField ("Generate form All?")
    Generate_Form_Filter              = BooleanField ("Generate Form Filter?")
    Generate_Children                 = BooleanField ("Generate Children?")
    Generate_Foreign_Fields           = BooleanField ("Generate Foreign Fields?")
    Permission_View                   = BooleanField ("Permission View?")
    Permission_Delete                 = BooleanField ("Permission Delete?")
    Permission_Modify                 = BooleanField ("Permission Modify?")
    Permission_Report                 = BooleanField ("Permission Report?")
    Permission_Export                 = BooleanField ("Permission Export?")
    Permission_View_Private           = BooleanField ("Permission View Private?")
    Permission_Modify_Private         = BooleanField ("Permission Modify Private?")
    Permission_Administer             = BooleanField ("Permission Administer?")

    submit_Save                       = SubmitField  ('Save')
    submit_New                        = SubmitField  ('New')
    submit_Cancel                     = SubmitField  ('Cancel')

    has_FKs                           = False

# =============================================================================

class frm_dev_table_delete(Form):
    submit_Delete                     = SubmitField  ('Delete')
    submit_Cancel                     = SubmitField  ('Cancel')

# =============================================================================

class Dev_Tables(Base):
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

    def __init__(self, Id, Name, Caption, Entity, Class_Name, Child_Table, Parent_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children, Generate_Foreign_Fields, Permission_View, Permission_Delete, Permission_Modify, Permission_Report, Permission_Export, Permission_View_Private, Permission_Modify_Private, Permission_Administer):
        self.set( Id, Name, Caption, Entity, Class_Name, Child_Table, Parent_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children, Generate_Foreign_Fields, Permission_View, Permission_Delete, Permission_Modify, Permission_Report, Permission_Export, Permission_View_Private, Permission_Modify_Private, Permission_Administer)

    def __repr__(self):
        return "<Dev_Tables( Id='%s', Name='%s', Caption='%s', Entity='%s', Class_Name='%s', Child_Table='%s', Parent_Table='%s', Use_Pagination='%s', Use_Children_Pagination='%s', Generate_Form_One='%s', Generate_Form_All='%s', Generate_Form_Filter='%s', Generate_Children='%s', Generate_Foreign_Fields='%s', Permission_View='%s', Permission_Delete='%s', Permission_Modify='%s', Permission_Report='%s', Permission_Export='%s', Permission_View_Private='%s', Permission_Modify_Private='%s', Permission_Administer='%s')>" % \
                ( self.Id, self.Name, self.Caption, self.Entity, self.Class_Name, self.Child_Table, self.Parent_Table, self.Use_Pagination, self.Use_Children_Pagination, self.Generate_Form_One, self.Generate_Form_All, self.Generate_Form_Filter, self.Generate_Children, self.Generate_Foreign_Fields, self.Permission_View, self.Permission_Delete, self.Permission_Modify, self.Permission_Report, self.Permission_Export, self.Permission_View_Private, self.Permission_Modify_Private, self.Permission_Administer)

# =============================================================================


# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class trace(db.Model):
    __tablename__ = 'Trace'
    ID   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    LINE = db.Column( db.String(128) )


    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

# =============================================================================

class frm_trace(Form):
    LINE         = StringField  ("LINE?")

    submit_Save  = SubmitField  ('Save')
    submit_New   = SubmitField  ('New')
    submit_Cancel = SubmitField  ('Cancel')

    has_FKs      = False

# =============================================================================

class frm_trace_delete(Form):
    submit_Delete = SubmitField  ('Delete')
    submit_Cancel = SubmitField  ('Cancel')

# =============================================================================

class Trace(Base):
    __tablename__ = 'Trace'
    engine        = None

    ID   = Column( Integer, primary_key=True, autoincrement=True )
    LINE = Column( String(128) )

    def __init__(self, ID, LINE):
        self.set( ID, LINE)

    def __repr__(self):
        return "<Trace( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

# =============================================================================


# =============================================================================
# Billing Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-10 22:23:58
# =============================================================================

"""
class country(db.Model):
    __tablename__ = 'Countries'
    Cou_Code = db.Column( db.String(2), primary_key=True )
    Cou_Name = db.Column( db.String(45) )
    Cou_A3   = db.Column( db.String(3) )
    Cou_N    = db.Column( db.Integer )

    countries_currencies = db.relationship('country_currency',backref='country')

    def __init__(self, Cou_Code=None, Cou_Name=None, Cou_A3=None, Cou_N=None):
        self.Cou_Code = Cou_Code
        self.Cou_Name = Cou_Name
        self.Cou_A3   = Cou_A3
        self.Cou_N    = Cou_N

    def __repr__(self):
        return "<Countries( Cou_Code='%s', Cou_Name='%s', Cou_A3='%s', Cou_N='%s')>" % \
                ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)
"""
# =============================================================================
class frm_billing_resume(Form):
    Cus_Id           = SelectField ("Customer?", validators=[Required()], coerce=int)
    CIT_Date_From    = StringField  ("Billing Data from?", validators=[Required()])
    CIT_Date_To      = StringField  ("Billing Data up to?", validators=[Required()])
    CIT_Status       = SelectField ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Cancel    = SubmitField  ('Cancel')
    
    has_FKs          = False
# =============================================================================
# Billing Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-10 22:23:58
# =============================================================================


# =============================================================================
class frm_charging_resume(Form):
    Cus_Id           = SelectField  ("Customer?", validators=[Required()], coerce=int)
    CIT_Date_From    = StringField  ("Billing Data from?", validators=[Required()])
    CIT_Date_To      = StringField  ("Billing Data up to?", validators=[Required()])
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
# Export Billing Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-17
# =============================================================================

# =============================================================================
class frm_export_billing_resume(Form):
    Cus_Id          = SelectField ("Customer?", validators=[Required()], coerce=int)
    CIT_Date_From   = StringField ("Billing Data from?", validators=[Required()])
    CIT_Date_To     = StringField ("Billing Data up to?", validators=[Required()])
    CIT_Status      = SelectField ("Status to Export?", coerce=int)
    Cur_Code        = SelectField ("Currency to Report?", coerce=str)

    submit_PDF      = SubmitField ('PDF')
    submit_XLS      = SubmitField ('XLS')
    submit_CSV      = SubmitField ('CSV')
    submit_JSON     = SubmitField ('JSON')
    submit_FIX      = SubmitField ('FIX')
    submit_Cancel   = SubmitField ('Cancel')
    
    has_FKs         = False
# =============================================================================
# Export Charging Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-27
# =============================================================================

# =============================================================================
class frm_export_Charging_Resume(Form):
    Export          = SelectField ("Export?", validators=[Required()])

    submit_PDF      = SubmitField ('PDF')
    submit_XLS      = SubmitField ('XLS')
    submit_CSV      = SubmitField ('CSV')
    submit_JSON     = SubmitField ('JSON')
    submit_FIX      = SubmitField ('FIX')
    submit_Cancel   = SubmitField ('Cancel')

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 18:58:45
# =============================================================================

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

