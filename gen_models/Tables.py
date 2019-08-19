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

    def __init__(self, Id, Name, Caption, Entity, Class_Name, Child_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children):
        self.set( Id, Name, Caption, Entity, Class_Name, Child_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children)
    def __repr__(self):
        return "<Tables( Id='%s', Name='%s', Caption='%s', Entity='%s', Class_Name='%s', Child_Table='%s', Use_Pagination='%s', Use_Children_Pagination='%s', Generate_Form_One='%s', Generate_Form_All='%s', Generate_Form_Filter='%s', Generate_Children='%s')>" % \
                ( self.Id, self.Name, self.Caption, self.Entity, self.Class_Name, self.Child_Table, self.Use_Pagination, self.Use_Children_Pagination, self.Generate_Form_One, self.Generate_Form_All, self.Generate_Form_Filter, self.Generate_Children)

    def __copy__(self):
        return type(self)( self.Id, self.Name, self.Caption, self.Entity, self.Class_Name, self.Child_Table, self.Use_Pagination, self.Use_Children_Pagination, self.Generate_Form_One, self.Generate_Form_All, self.Generate_Form_Filter, self.Generate_Children)

    def __deepcopy__(self, memo): # memo is a dict of id's to copies
        id_self = id(self)        # memoization avoids unnecesary recursion
        _copy = memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self.Id                      , memo)
                ,deepcopy(self.Name                    , memo)
                ,deepcopy(self.Caption                 , memo)
                ,deepcopy(self.Entity                  , memo)
                ,deepcopy(self.Class_Name              , memo)
                ,deepcopy(self.Child_Table             , memo)
                ,deepcopy(self.Use_Pagination          , memo)
                ,deepcopy(self.Use_Children_Pagination , memo)
                ,deepcopy(self.Generate_Form_One       , memo)
                ,deepcopy(self.Generate_Form_All       , memo)
                ,deepcopy(self.Generate_Form_Filter    , memo)
                ,deepcopy(self.Generate_Children       , memo)
                )
            memo[id_self] = _copy
        return _copy

    def set(self, Id, Name, Caption, Entity, Class_Name, Child_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children):
        self.Id                      = Id
        self.Name                    = Name
        self.Caption                 = Caption
        self.Entity                  = Entity
        self.Class_Name              = Class_Name
        self.Child_Table             = Child_Table
        self.Use_Pagination          = Use_Pagination
        self.Use_Children_Pagination = Use_Children_Pagination
        self.Generate_Form_One       = Generate_Form_One
        self.Generate_Form_All       = Generate_Form_All
        self.Generate_Form_Filter    = Generate_Form_Filter
        self.Generate_Children       = Generate_Children

    def insert(self, Id, Name, Caption, Entity, Class_Name, Child_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children):
        self.set( Id, Name, Caption, Entity, Class_Name, Child_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        X = copy(self)
        session.add(X)
        session.commit()
        session.close()

    def merge(self, Id, Name, Caption, Entity, Class_Name, Child_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children):
        self.set( Id, Name, Caption, Entity, Class_Name, Child_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.merge()
        session.commit()
        session.close()

    def update(self, Id, Name, Caption, Entity, Class_Name, Child_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children):
        self.set( Id, Name, Caption, Entity, Class_Name, Child_Table, Use_Pagination, Use_Children_Pagination, Generate_Form_One, Generate_Form_All, Generate_Form_Filter, Generate_Children)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.query(Tables).filter(Tables.Id == Id).update({Tables.Name : Name,Tables.Caption : Caption,Tables.Entity : Entity,Tables.Class_Name : Class_Name,Tables.Child_Table : Child_Table,Tables.Use_Pagination : Use_Pagination,Tables.Use_Children_Pagination : Use_Children_Pagination,Tables.Generate_Form_One : Generate_Form_One,Tables.Generate_Form_All : Generate_Form_All,Tables.Generate_Form_Filter : Generate_Form_Filter,Tables.Generate_Children : Generate_Children})
        session.commit()
        session.close()

    def delete(self,Id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.query(Tables).filter(Tables.Id == Id).delete()
        session.commit()
        session.close()

    def queryall(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            results = session.query(Tables).all()
        except exc.NoResultFound:
            results = None
        return results

    def queryone(self,Id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            results = session.query(Tables).filter(Tables.Id == Id).one()
        except exc.NoResultFound:
            results = None
        return results

    def queryjoin(self,Id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            results = session.query(Tables).filter(Tables.Id == Id).one()
        except exc.NoResultFound:
            results = None
        return results

    def inject_list(self,rows):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        for row in (rows):
            X = copy(self)
            for f in range(len(row)):
                X.Id                      = row[0]
                X.Name                    = row[1]
                X.Caption                 = row[2]
                X.Entity                  = row[3]
                X.Class_Name              = row[4]
                X.Child_Table             = row[5]
                X.Use_Pagination          = row[6]
                X.Use_Children_Pagination = row[7]
                X.Generate_Form_One       = row[8]
                X.Generate_Form_All       = row[9]
                X.Generate_Form_Filter    = row[10]
                X.Generate_Children       = row[11]
            session.add(X)
        session.commit()
        session.close()

    def inject_dict(self,rows):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        for row in (rows):
            X = copy(self)
            for f in range(len(row)):
                X.Id                      = row['Id']
                X.Name                    = row['Name']
                X.Caption                 = row['Caption']
                X.Entity                  = row['Entity']
                X.Class_Name              = row['Class_Name']
                X.Child_Table             = row['Child_Table']
                X.Use_Pagination          = row['Use_Pagination']
                X.Use_Children_Pagination = row['Use_Children_Pagination']
                X.Generate_Form_One       = row['Generate_Form_One']
                X.Generate_Form_All       = row['Generate_Form_All']
                X.Generate_Form_Filter    = row['Generate_Form_Filter']
                X.Generate_Children       = row['Generate_Children']
            session.add(X)
        session.commit()
        session.close()

# =============================================================================
class frm_Tables(Form):
    submit                          = SubmitField('Save')

    has_FKs                         = False
    FK_List                         = {}
    engine                          = None

