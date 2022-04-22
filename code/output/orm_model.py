# GV ---------------------------------------------------------------------- 
# GV ORM Models File
# GV Static File. 
# GV GLVH 2018-12-13
# GV GLVH 2021-04-02 datetime refactoring fixup
# GV Source: EG-Collector-Tools/code/src/orm_models_py_header.py
# GV ----------------------------------------------------------------------
# GV GV 20210403 from datetime               import datetime
import datetime

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer, Numeric
from sqlalchemy import Date, Time, DateTime
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
# GV ----------------------------------------------------------------------



# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

from sqlalchemy                 import Table, Column
from sqlalchemy                 import MetaData, ForeignKey
from sqlalchemy                 import Integer, BigInteger,SmallInteger
from sqlalchemy                 import String
from sqlalchemy                 import Date, Time
from sqlalchemy                 import Numeric, DateTime, Boolean, Text
from sqlalchemy                 import VARBINARY


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================
import json
import logging
from time import strftime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_cit_generations.py
import sqlalchemy
class CIT_Generations(Base):
    __tablename__ = 'CIT_Generations'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='CIT_Generations_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CIT_Generation = Column( Integer, primary_key=True )
    Value          = Column( String(45) )
    
    def __init__(self, CIT_Generation=None, Value='None',engine=None,logger=None):
        """ Initiates a CIT_Generations class record """
        self.engine=engine
        self.logger=logger
        self.CIT_Generation = CIT_Generation
        self.Value          = Value

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class CIT_Generations representation function """
        return "<CIT_Generations( CIT_Generation='%s', Value='%s')>" % \
                ( self.CIT_Generation, self.Value)

    def get_list(self):
        """ Gets CIT_Generations record in list format """
        __list = [ self.CIT_Generation, self.Value]
        return __list

    def get_tuple(self):
        """ Gets CIT_Generations record in tuple format """
        __tuple = ( self.CIT_Generation, self.Value)
        return __tuple

    def get_dict(self):
        """ Gets CIT_Generations record in dict format """
        __dict={'CIT_Generation':self.CIT_Generation,'Value':self.Value}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets CIT_Generations record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets CIT_Generations record column full details list """
        __list=[{'field': 'CIT_Generation', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Generation', 'is_time': False}, {'field': 'Value', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Value', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets CIT_Generations record column headers list """
        __list=['CIT_Generation', 'Value']

        return __list

    def get_column_types(self):
        """ Gets CIT_Generations record column data types list """
        __list=['Integer', 'String(45)']

        return __list

    def get_column_meta(self):
        """ Gets CIT_Generations record column data meta list """
        __list=[('CIT_Generation', 'Integer'), ('Value', 'String(45)')]

        return __list

    def search_key(self,CIT_Generation):
        """ Search for an unique CIT_Generations record using all key fields (CIT_Generation) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(CIT_Generations).filter(CIT_Generations.CIT_Generation==CIT_Generation).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='CIT_Generations.search_key(%s): Exception: %s'%(CIT_Generation,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='CIT_Generations.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class CIT_Generations log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_cit_statuses.py
import sqlalchemy
class CIT_Statuses(Base):
    __tablename__ = 'CIT_Statuses'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='CIT_Statuses_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CIT_Status = Column( Integer, primary_key=True )
    Value      = Column( String(45) )
    
    def __init__(self, CIT_Status=None, Value='None',engine=None,logger=None):
        """ Initiates a CIT_Statuses class record """
        self.engine=engine
        self.logger=logger
        self.CIT_Status = CIT_Status
        self.Value      = Value

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class CIT_Statuses representation function """
        return "<CIT_Statuses( CIT_Status='%s', Value='%s')>" % \
                ( self.CIT_Status, self.Value)

    def get_list(self):
        """ Gets CIT_Statuses record in list format """
        __list = [ self.CIT_Status, self.Value]
        return __list

    def get_tuple(self):
        """ Gets CIT_Statuses record in tuple format """
        __tuple = ( self.CIT_Status, self.Value)
        return __tuple

    def get_dict(self):
        """ Gets CIT_Statuses record in dict format """
        __dict={'CIT_Status':self.CIT_Status,'Value':self.Value}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets CIT_Statuses record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets CIT_Statuses record column full details list """
        __list=[{'field': 'CIT_Status', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT Status', 'is_time': False}, {'field': 'Value', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Vallue', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets CIT_Statuses record column headers list """
        __list=['CIT_Status', 'Value']

        return __list

    def get_column_types(self):
        """ Gets CIT_Statuses record column data types list """
        __list=['Integer', 'String(45)']

        return __list

    def get_column_meta(self):
        """ Gets CIT_Statuses record column data meta list """
        __list=[('CIT_Status', 'Integer'), ('Value', 'String(45)')]

        return __list

    def search_key(self,CIT_Status):
        """ Search for an unique CIT_Statuses record using all key fields (CIT_Status) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(CIT_Statuses).filter(CIT_Statuses.CIT_Status==CIT_Status).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='CIT_Statuses.search_key(%s): Exception: %s'%(CIT_Status,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='CIT_Statuses.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class CIT_Statuses log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_cu_operations.py
import sqlalchemy
class CU_Operations(Base):
    __tablename__ = 'CU_Operations'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='CU_Operations_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Operation = Column( String(10), primary_key=True )
    Value        = Column( String(45) )
    Is_Multiply  = Column( Boolean )
    Factor       = Column( Integer )
    
    def __init__(self, CU_Operation='None', Value='None', Is_Multiply=None, Factor=None,engine=None,logger=None):
        """ Initiates a CU_Operations class record """
        self.engine=engine
        self.logger=logger
        self.CU_Operation = CU_Operation
        self.Value        = Value
        self.Is_Multiply  = Is_Multiply
        self.Factor       = Factor

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class CU_Operations representation function """
        return "<CU_Operations( CU_Operation='%s', Value='%s', Is_Multiply='%s', Factor='%s')>" % \
                ( self.CU_Operation, self.Value, self.Is_Multiply, self.Factor)

    def get_list(self):
        """ Gets CU_Operations record in list format """
        __list = [ self.CU_Operation, self.Value, self.Is_Multiply, self.Factor]
        return __list

    def get_tuple(self):
        """ Gets CU_Operations record in tuple format """
        __tuple = ( self.CU_Operation, self.Value, self.Is_Multiply, self.Factor)
        return __tuple

    def get_dict(self):
        """ Gets CU_Operations record in dict format """
        __dict={'CU_Operation':self.CU_Operation,'Value':self.Value,'Is_Multiply':self.Is_Multiply,'Factor':self.Factor}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets CU_Operations record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets CU_Operations record column full details list """
        __list=[{'field': 'CU_Operation', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Operation', 'is_time': False}, {'field': 'Value', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Value', 'is_time': False}, {'field': 'Is_Multiply', 'type': 'tinyint', 'type_flask': 'db.Boolean', 'type_sqlalchemy': 'Boolean', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'BooleanField', 'is_id': False, 'header': 'Is Multiply', 'is_time': False}, {'field': 'Factor', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Factor', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets CU_Operations record column headers list """
        __list=['CU_Operation', 'Value', 'Is_Multiply', 'Factor']

        return __list

    def get_column_types(self):
        """ Gets CU_Operations record column data types list """
        __list=['String(10)', 'String(45)', 'Boolean', 'Integer']

        return __list

    def get_column_meta(self):
        """ Gets CU_Operations record column data meta list """
        __list=[('CU_Operation', 'String(10)'), ('Value', 'String(45)'), ('Is_Multiply', 'Boolean'), ('Factor', 'Integer')]

        return __list

    def search_key(self,CU_Operation):
        """ Search for an unique CU_Operations record using all key fields (CU_Operation) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(CU_Operations).filter(CU_Operations.CU_Operation==CU_Operation).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='CU_Operations.search_key(%s): Exception: %s'%(CU_Operation,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='CU_Operations.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class CU_Operations log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_cu_types.py
import sqlalchemy
class CU_Types(Base):
    __tablename__ = 'CU_Types'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='CU_Types_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Typ_Code        = Column( String(10), primary_key=True )
    Typ_Description = Column( String(45) )
    
    def __init__(self, Typ_Code='None', Typ_Description='None',engine=None,logger=None):
        """ Initiates a CU_Types class record """
        self.engine=engine
        self.logger=logger
        self.Typ_Code        = Typ_Code
        self.Typ_Description = Typ_Description

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class CU_Types representation function """
        return "<CU_Types( Typ_Code='%s', Typ_Description='%s')>" % \
                ( self.Typ_Code, self.Typ_Description)

    def get_list(self):
        """ Gets CU_Types record in list format """
        __list = [ self.Typ_Code, self.Typ_Description]
        return __list

    def get_tuple(self):
        """ Gets CU_Types record in tuple format """
        __tuple = ( self.Typ_Code, self.Typ_Description)
        return __tuple

    def get_dict(self):
        """ Gets CU_Types record in dict format """
        __dict={'Typ_Code':self.Typ_Code,'Typ_Description':self.Typ_Description}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets CU_Types record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets CU_Types record column full details list """
        __list=[{'field': 'Typ_Code', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Type', 'is_time': False}, {'field': 'Typ_Description', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Description', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets CU_Types record column headers list """
        __list=['Typ_Code', 'Typ_Description']

        return __list

    def get_column_types(self):
        """ Gets CU_Types record column data types list """
        __list=['String(10)', 'String(45)']

        return __list

    def get_column_meta(self):
        """ Gets CU_Types record column data meta list """
        __list=[('Typ_Code', 'String(10)'), ('Typ_Description', 'String(45)')]

        return __list

    def search_key(self,Typ_Code):
        """ Search for an unique CU_Types record using all key fields (Typ_Code) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(CU_Types).filter(CU_Types.Typ_Code==Typ_Code).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='CU_Types.search_key(%s): Exception: %s'%(Typ_Code,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='CU_Types.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class CU_Types log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_charge_items.py
import sqlalchemy
class Charge_Items(Base):
    __tablename__ = 'Charge_Items'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Charge_Items_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Id         = Column( Integer, ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    CIT_Date      = Column( Date )
    CIT_Time      = Column( Time )
    CIT_Quantity  = Column( Numeric(20,12) )
    CIT_Status    = Column( Integer, ForeignKey('CIT_Statuses.CIT_Status') )
    CIT_Is_Active = Column( Boolean )
    CIT_DateTime  = Column( DateTime, primary_key=True )
    
    def __init__(self, CU_Id=0, CIT_Date=None, CIT_Time=None, CIT_Quantity=0.000000000000, CIT_Status=0, CIT_Is_Active=0, CIT_DateTime=datetime.datetime.utcnow(),engine=None,logger=None):
        """ Initiates a Charge_Items class record """
        self.engine=engine
        self.logger=logger
        self.CU_Id         = CU_Id
        self.CIT_Date      = CIT_Date
        self.CIT_Time      = CIT_Time
        self.CIT_Quantity  = CIT_Quantity
        self.CIT_Status    = CIT_Status
        self.CIT_Is_Active = CIT_Is_Active
        self.CIT_DateTime  = CIT_DateTime

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Charge_Items representation function """
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s', CIT_DateTime='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime)

    def get_list(self):
        """ Gets Charge_Items record in list format """
        __list = [ self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime]
        return __list

    def get_tuple(self):
        """ Gets Charge_Items record in tuple format """
        __tuple = ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime)
        return __tuple

    def get_dict(self):
        """ Gets Charge_Items record in dict format """
        __dict={'CU_Id':self.CU_Id,'CIT_Date':self.CIT_Date,'CIT_Time':self.CIT_Time,'CIT_Quantity':self.CIT_Quantity,'CIT_Status':self.CIT_Status,'CIT_Is_Active':self.CIT_Is_Active,'CIT_DateTime':self.CIT_DateTime}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Charge_Items record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Charge_Items record column full details list """
        __list=[{'field': 'CU_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CU_Id', 'referenced_table': 'Charge_Units', 'referenced_class': 'charge_unit', 'foreign_key': 'CU_Id', 'foreign_value': 'CU_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Charge Unit Id', 'is_time': False}, {'field': 'CIT_Date', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'Date', 'is_time': False}, {'field': 'CIT_Time', 'type': 'time', 'type_flask': 'db.Time', 'type_sqlalchemy': 'Time', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'TimeField', 'is_id': False, 'header': 'Time', 'is_time': True}, {'field': 'CIT_Quantity', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'NO', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Quantity', 'is_time': False}, {'field': 'CIT_Status', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': True, 'referenced_table': 'CIT_Statuses', 'referenced_class': 'cit_status', 'foreign_key': 'CIT_Status', 'foreign_field': 'CIT_Status', 'foreign_value': 'Value', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Status', 'is_time': False}, {'field': 'CIT_Is_Active', 'type': 'tinyint', 'type_flask': 'db.Boolean', 'type_sqlalchemy': 'Boolean', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'BooleanField', 'is_id': False, 'header': 'Is Active', 'is_time': False}, {'field': 'CIT_DateTime', 'type': 'timestamp', 'type_flask': 'db.DateTime', 'type_sqlalchemy': 'DateTime', 'null': 'NO', 'key': 'PRI', 'default': 'CURRENT_TIMESTAMP', 'extra': 'DEFAULT_GENERATED', 'is_form_editable': False, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateTimeField', 'is_id': False, 'header': 'CIT_DateTime', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Charge_Items record column headers list """
        __list=['CU_Id', 'CIT_Date', 'CIT_Time', 'CIT_Quantity', 'CIT_Status', 'CIT_Is_Active', 'CIT_DateTime']

        return __list

    def get_column_types(self):
        """ Gets Charge_Items record column data types list """
        __list=['Integer', 'Date', 'Time', 'Numeric(20,12)', 'Integer', 'Boolean', 'DateTime']

        return __list

    def get_column_meta(self):
        """ Gets Charge_Items record column data meta list """
        __list=[('CU_Id', 'Integer'), ('CIT_Date', 'Date'), ('CIT_Time', 'Time'), ('CIT_Quantity', 'Numeric(20,12)'), ('CIT_Status', 'Integer'), ('CIT_Is_Active', 'Boolean'), ('CIT_DateTime', 'DateTime')]

        return __list

    def search_key(self,CU_Id,CIT_DateTime):
        """ Search for an unique Charge_Items record using all key fields (CU_Id,CIT_DateTime) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Charge_Items).filter(Charge_Items.CU_Id==CU_Id).filter(Charge_Items.CIT_DateTime==CIT_DateTime).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Charge_Items.search_key(%s,%s): Exception: %s'%(CU_Id,CIT_DateTime,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Charge_Items.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Charge_Items log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:865 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_charge_items.py
# gen_model_flask.py:866 Table sharding code follows:
def get_Charge_Items(table_name_suffix):
  class Charge_Items_Class(Base):
    __tablename__ = 'Charge_Items_%s'%(table_name_suffix)
    engine        = None
    logger        = None

    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Charge_Items_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table_args__ = {'extend_existing':True}
           __class__.__table__.name = name
           __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Id         = Column( Integer, ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    CIT_Date      = Column( Date )
    CIT_Time      = Column( Time )
    CIT_Quantity  = Column( Numeric(20,12) )
    CIT_Status    = Column( Integer, ForeignKey('CIT_Statuses.CIT_Status') )
    CIT_Is_Active = Column( Boolean )
    CIT_DateTime  = Column( DateTime, primary_key=True )
    
    def __init__(self, CU_Id=0, CIT_Date=None, CIT_Time=None, CIT_Quantity=0.000000000000, CIT_Status=0, CIT_Is_Active=0, CIT_DateTime=datetime.datetime.utcnow(),engine=None,logger=None):
        """ Initiates a Charge_Items class record """
        self.engine=engine
        self.logger=logger
        self.CU_Id         = CU_Id
        self.CIT_Date      = CIT_Date
        self.CIT_Time      = CIT_Time
        self.CIT_Quantity  = CIT_Quantity
        self.CIT_Status    = CIT_Status
        self.CIT_Is_Active = CIT_Is_Active
        self.CIT_DateTime  = CIT_DateTime

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Charge_Items representation function """
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s', CIT_DateTime='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime)

    def get_list(self):
        """ Gets Charge_Items record in list format """
        __list = [ self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime]
        return __list

    def get_tuple(self):
        """ Gets Charge_Items record in tuple format """
        __tuple = ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime)
        return __tuple

    def get_dict(self):
        """ Gets Charge_Items record in dict format """
        __dict={'CU_Id':self.CU_Id,'CIT_Date':self.CIT_Date,'CIT_Time':self.CIT_Time,'CIT_Quantity':self.CIT_Quantity,'CIT_Status':self.CIT_Status,'CIT_Is_Active':self.CIT_Is_Active,'CIT_DateTime':self.CIT_DateTime}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Charge_Items record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Charge_Items record column full details list """
        __list=[{'field': 'CU_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CU_Id', 'referenced_table': 'Charge_Units', 'referenced_class': 'charge_unit', 'foreign_key': 'CU_Id', 'foreign_value': 'CU_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Charge Unit Id', 'is_time': False}, {'field': 'CIT_Date', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'Date', 'is_time': False}, {'field': 'CIT_Time', 'type': 'time', 'type_flask': 'db.Time', 'type_sqlalchemy': 'Time', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'TimeField', 'is_id': False, 'header': 'Time', 'is_time': True}, {'field': 'CIT_Quantity', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'NO', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Quantity', 'is_time': False}, {'field': 'CIT_Status', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': True, 'referenced_table': 'CIT_Statuses', 'referenced_class': 'cit_status', 'foreign_key': 'CIT_Status', 'foreign_field': 'CIT_Status', 'foreign_value': 'Value', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Status', 'is_time': False}, {'field': 'CIT_Is_Active', 'type': 'tinyint', 'type_flask': 'db.Boolean', 'type_sqlalchemy': 'Boolean', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'BooleanField', 'is_id': False, 'header': 'Is Active', 'is_time': False}, {'field': 'CIT_DateTime', 'type': 'timestamp', 'type_flask': 'db.DateTime', 'type_sqlalchemy': 'DateTime', 'null': 'NO', 'key': 'PRI', 'default': 'CURRENT_TIMESTAMP', 'extra': 'DEFAULT_GENERATED', 'is_form_editable': False, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateTimeField', 'is_id': False, 'header': 'CIT_DateTime', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Charge_Items record column headers list """
        __list=['CU_Id', 'CIT_Date', 'CIT_Time', 'CIT_Quantity', 'CIT_Status', 'CIT_Is_Active', 'CIT_DateTime']

        return __list

    def get_column_types(self):
        """ Gets Charge_Items record column data types list """
        __list=['Integer', 'Date', 'Time', 'Numeric(20,12)', 'Integer', 'Boolean', 'DateTime']

        return __list

    def get_column_meta(self):
        """ Gets Charge_Items record column data meta list """
        __list=[('CU_Id', 'Integer'), ('CIT_Date', 'Date'), ('CIT_Time', 'Time'), ('CIT_Quantity', 'Numeric(20,12)'), ('CIT_Status', 'Integer'), ('CIT_Is_Active', 'Boolean'), ('CIT_DateTime', 'DateTime')]

        return __list

    def search_key(self,CU_Id,CIT_DateTime):
        """ Search for an unique Charge_Items record using all key fields (CU_Id,CIT_DateTime) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Charge_Items).filter(Charge_Items.CU_Id==CU_Id).filter(Charge_Items.CIT_DateTime==CIT_DateTime).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Charge_Items.search_key(%s,%s): Exception: %s'%(CU_Id,CIT_DateTime,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Charge_Items.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Charge_Items log function """
        if self.logger is not None:
            self.logger.log(level,message)

  Charge_Items_Class.__name__ = 'Charge_Items_%s'%(table_name_suffix)
  x = Charge_Items_Class
  return x

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_charge_resumes.py
import sqlalchemy
class Charge_Resumes(Base):
    __tablename__ = 'Charge_Resumes'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Charge_Resumes_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    User_Id                = Column( Integer, primary_key=True )
    Cus_Id                 = Column( Integer, primary_key=True )
    CR_Date_From           = Column( Date, primary_key=True )
    CR_Date_To             = Column( Date, primary_key=True )
    CIT_Status             = Column( Integer, primary_key=True )
    Cur_Code               = Column( String(3), primary_key=True )
    CU_Id                  = Column( Integer, primary_key=True )
    CIT_Count              = Column( Integer )
    CIT_Quantity           = Column( Numeric(20,12) )
    CIT_Generation         = Column( Integer )
    CI_CC_Id               = Column( Integer )
    CU_Operation           = Column( String(10) )
    Typ_Code               = Column( String(10) )
    CC_Cur_Code            = Column( String(3) )
    CI_Id                  = Column( Integer )
    Rat_Id                 = Column( Integer )
    Rat_Price              = Column( Numeric(20,12) )
    Rat_MU_Code            = Column( String(3) )
    Rat_Cur_Code           = Column( String(3) )
    Rat_Period             = Column( Integer )
    Rat_Hourly             = Column( Numeric(20,12) )
    Rat_Daily              = Column( Numeric(20,12) )
    Rat_Monthly            = Column( Numeric(20,12) )
    CR_Quantity            = Column( Numeric(20,12) )
    CR_Quantity_at_Rate    = Column( Numeric(20,12) )
    CC_XR                  = Column( Numeric(20,12) )
    CR_Cur_XR              = Column( Numeric(20,12) )
    CR_ST_at_Rate_Cur      = Column( Numeric(20,12) )
    CR_ST_at_CC_Cur        = Column( Numeric(20,12) )
    CR_ST_at_Cur           = Column( Numeric(20,12) )
    Cus_Name               = Column( String(255) )
    CI_Name                = Column( String(255) )
    CU_Description         = Column( String(255) )
    CC_Description         = Column( String(255) )
    Rat_Period_Description = Column( String(10) )
    CC_Code                = Column( String(45) )
    Pla_Id                 = Column( Integer )
    Pla_Name               = Column( String(255) )
    
    def __init__(self, User_Id=None, Cus_Id=None, CR_Date_From=None, CR_Date_To=None, CIT_Status=None, Cur_Code='None', CU_Id=None, CIT_Count=None, CIT_Quantity=None, CIT_Generation=1, CI_CC_Id=None, CU_Operation='None', Typ_Code='None', CC_Cur_Code='None', CI_Id=None, Rat_Id=None, Rat_Price=None, Rat_MU_Code='None', Rat_Cur_Code='None', Rat_Period=None, Rat_Hourly=None, Rat_Daily=None, Rat_Monthly=None, CR_Quantity=None, CR_Quantity_at_Rate=None, CC_XR=None, CR_Cur_XR=None, CR_ST_at_Rate_Cur=None, CR_ST_at_CC_Cur=None, CR_ST_at_Cur=None, Cus_Name='None', CI_Name='None', CU_Description='None', CC_Description='None', Rat_Period_Description='None', CC_Code='None', Pla_Id=None, Pla_Name='None',engine=None,logger=None):
        """ Initiates a Charge_Resumes class record """
        self.engine=engine
        self.logger=logger
        self.User_Id                = User_Id
        self.Cus_Id                 = Cus_Id
        self.CR_Date_From           = CR_Date_From
        self.CR_Date_To             = CR_Date_To
        self.CIT_Status             = CIT_Status
        self.Cur_Code               = Cur_Code
        self.CU_Id                  = CU_Id
        self.CIT_Count              = CIT_Count
        self.CIT_Quantity           = CIT_Quantity
        self.CIT_Generation         = CIT_Generation
        self.CI_CC_Id               = CI_CC_Id
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CC_Cur_Code            = CC_Cur_Code
        self.CI_Id                  = CI_Id
        self.Rat_Id                 = Rat_Id
        self.Rat_Price              = Rat_Price
        self.Rat_MU_Code            = Rat_MU_Code
        self.Rat_Cur_Code           = Rat_Cur_Code
        self.Rat_Period             = Rat_Period
        self.Rat_Hourly             = Rat_Hourly
        self.Rat_Daily              = Rat_Daily
        self.Rat_Monthly            = Rat_Monthly
        self.CR_Quantity            = CR_Quantity
        self.CR_Quantity_at_Rate    = CR_Quantity_at_Rate
        self.CC_XR                  = CC_XR
        self.CR_Cur_XR              = CR_Cur_XR
        self.CR_ST_at_Rate_Cur      = CR_ST_at_Rate_Cur
        self.CR_ST_at_CC_Cur        = CR_ST_at_CC_Cur
        self.CR_ST_at_Cur           = CR_ST_at_Cur
        self.Cus_Name               = Cus_Name
        self.CI_Name                = CI_Name
        self.CU_Description         = CU_Description
        self.CC_Description         = CC_Description
        self.Rat_Period_Description = Rat_Period_Description
        self.CC_Code                = CC_Code
        self.Pla_Id                 = Pla_Id
        self.Pla_Name               = Pla_Name

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Charge_Resumes representation function """
        return "<Charge_Resumes( User_Id='%s', Cus_Id='%s', CR_Date_From='%s', CR_Date_To='%s', CIT_Status='%s', Cur_Code='%s', CU_Id='%s', CIT_Count='%s', CIT_Quantity='%s', CIT_Generation='%s', CI_CC_Id='%s', CU_Operation='%s', Typ_Code='%s', CC_Cur_Code='%s', CI_Id='%s', Rat_Id='%s', Rat_Price='%s', Rat_MU_Code='%s', Rat_Cur_Code='%s', Rat_Period='%s', Rat_Hourly='%s', Rat_Daily='%s', Rat_Monthly='%s', CR_Quantity='%s', CR_Quantity_at_Rate='%s', CC_XR='%s', CR_Cur_XR='%s', CR_ST_at_Rate_Cur='%s', CR_ST_at_CC_Cur='%s', CR_ST_at_Cur='%s', Cus_Name='%s', CI_Name='%s', CU_Description='%s', CC_Description='%s', Rat_Period_Description='%s', CC_Code='%s', Pla_Id='%s', Pla_Name='%s')>" % \
                ( self.User_Id, self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CU_Id, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.CC_Code, self.Pla_Id, self.Pla_Name)

    def get_list(self):
        """ Gets Charge_Resumes record in list format """
        __list = [ self.User_Id, self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CU_Id, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.CC_Code, self.Pla_Id, self.Pla_Name]
        return __list

    def get_tuple(self):
        """ Gets Charge_Resumes record in tuple format """
        __tuple = ( self.User_Id, self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CU_Id, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.CC_Code, self.Pla_Id, self.Pla_Name)
        return __tuple

    def get_dict(self):
        """ Gets Charge_Resumes record in dict format """
        __dict={'User_Id':self.User_Id,'Cus_Id':self.Cus_Id,'CR_Date_From':self.CR_Date_From,'CR_Date_To':self.CR_Date_To,'CIT_Status':self.CIT_Status,'Cur_Code':self.Cur_Code,'CU_Id':self.CU_Id,'CIT_Count':self.CIT_Count,'CIT_Quantity':self.CIT_Quantity,'CIT_Generation':self.CIT_Generation,'CI_CC_Id':self.CI_CC_Id,'CU_Operation':self.CU_Operation,'Typ_Code':self.Typ_Code,'CC_Cur_Code':self.CC_Cur_Code,'CI_Id':self.CI_Id,'Rat_Id':self.Rat_Id,'Rat_Price':self.Rat_Price,'Rat_MU_Code':self.Rat_MU_Code,'Rat_Cur_Code':self.Rat_Cur_Code,'Rat_Period':self.Rat_Period,'Rat_Hourly':self.Rat_Hourly,'Rat_Daily':self.Rat_Daily,'Rat_Monthly':self.Rat_Monthly,'CR_Quantity':self.CR_Quantity,'CR_Quantity_at_Rate':self.CR_Quantity_at_Rate,'CC_XR':self.CC_XR,'CR_Cur_XR':self.CR_Cur_XR,'CR_ST_at_Rate_Cur':self.CR_ST_at_Rate_Cur,'CR_ST_at_CC_Cur':self.CR_ST_at_CC_Cur,'CR_ST_at_Cur':self.CR_ST_at_Cur,'Cus_Name':self.Cus_Name,'CI_Name':self.CI_Name,'CU_Description':self.CU_Description,'CC_Description':self.CC_Description,'Rat_Period_Description':self.Rat_Period_Description,'CC_Code':self.CC_Code,'Pla_Id':self.Pla_Id,'Pla_Name':self.Pla_Name}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Charge_Resumes record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Charge_Resumes record column full details list """
        __list=[{'field': 'User_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'User_Id', 'is_time': False}, {'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Cus_Id', 'is_time': False}, {'field': 'CR_Date_From', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'CR_Date_From', 'is_time': False}, {'field': 'CR_Date_To', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'CR_Date_To', 'is_time': False}, {'field': 'CIT_Status', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Status', 'is_time': False}, {'field': 'Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Cur_Code', 'is_time': False}, {'field': 'CU_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CU_Id', 'is_time': False}, {'field': 'CIT_Count', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Count', 'is_time': False}, {'field': 'CIT_Quantity', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CIT_Quantity', 'is_time': False}, {'field': 'CIT_Generation', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Generation', 'is_time': False}, {'field': 'CI_CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 11, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CI_CC_Id', 'is_time': False}, {'field': 'CU_Operation', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 12, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CU_Operation', 'is_time': False}, {'field': 'Typ_Code', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 13, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Typ_Code', 'is_time': False}, {'field': 'CC_Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 14, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CC_Cur_Code', 'is_time': False}, {'field': 'CI_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 15, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CI_Id', 'is_time': False}, {'field': 'Rat_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 16, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Rat_Id', 'is_time': False}, {'field': 'Rat_Price', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 17, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Rat_Price', 'is_time': False}, {'field': 'Rat_MU_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 18, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Rat_MU_Code', 'is_time': False}, {'field': 'Rat_Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 19, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Rat_Cur_Code', 'is_time': False}, {'field': 'Rat_Period', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 20, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Rat_Period', 'is_time': False}, {'field': 'Rat_Hourly', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 21, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Rat_Hourly', 'is_time': False}, {'field': 'Rat_Daily', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 22, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Rat_Daily', 'is_time': False}, {'field': 'Rat_Monthly', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 23, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Rat_Monthly', 'is_time': False}, {'field': 'CR_Quantity', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 24, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Quantity', 'is_time': False}, {'field': 'CR_Quantity_at_Rate', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 25, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Quantity_at_Rate', 'is_time': False}, {'field': 'CC_XR', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 26, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CC_XR', 'is_time': False}, {'field': 'CR_Cur_XR', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 27, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Cur_XR', 'is_time': False}, {'field': 'CR_ST_at_Rate_Cur', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 28, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_ST_at_Rate_Cur', 'is_time': False}, {'field': 'CR_ST_at_CC_Cur', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 29, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_ST_at_CC_Cur', 'is_time': False}, {'field': 'CR_ST_at_Cur', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 30, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_ST_at_Cur', 'is_time': False}, {'field': 'Cus_Name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 31, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Cus_Name', 'is_time': False}, {'field': 'CI_Name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 32, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CI_Name', 'is_time': False}, {'field': 'CU_Description', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 33, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CU_Description', 'is_time': False}, {'field': 'CC_Description', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 34, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CC_Description', 'is_time': False}, {'field': 'Rat_Period_Description', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 35, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Rat_Period_Description', 'is_time': False}, {'field': 'CC_Code', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 36, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CC_Code', 'is_time': False}, {'field': 'Pla_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 37, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Pla_Id', 'is_time': False}, {'field': 'Pla_Name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 38, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Pla_Name', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Charge_Resumes record column headers list """
        __list=['User_Id', 'Cus_Id', 'CR_Date_From', 'CR_Date_To', 'CIT_Status', 'Cur_Code', 'CU_Id', 'CIT_Count', 'CIT_Quantity', 'CIT_Generation', 'CI_CC_Id', 'CU_Operation', 'Typ_Code', 'CC_Cur_Code', 'CI_Id', 'Rat_Id', 'Rat_Price', 'Rat_MU_Code', 'Rat_Cur_Code', 'Rat_Period', 'Rat_Hourly', 'Rat_Daily', 'Rat_Monthly', 'CR_Quantity', 'CR_Quantity_at_Rate', 'CC_XR', 'CR_Cur_XR', 'CR_ST_at_Rate_Cur', 'CR_ST_at_CC_Cur', 'CR_ST_at_Cur', 'Cus_Name', 'CI_Name', 'CU_Description', 'CC_Description', 'Rat_Period_Description', 'CC_Code', 'Pla_Id', 'Pla_Name']

        return __list

    def get_column_types(self):
        """ Gets Charge_Resumes record column data types list """
        __list=['Integer', 'Integer', 'Date', 'Date', 'Integer', 'String(3)', 'Integer', 'Integer', 'Numeric(20,12)', 'Integer', 'Integer', 'String(10)', 'String(10)', 'String(3)', 'Integer', 'Integer', 'Numeric(20,12)', 'String(3)', 'String(3)', 'Integer', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'String(255)', 'String(255)', 'String(255)', 'String(255)', 'String(10)', 'String(45)', 'Integer', 'String(255)']

        return __list

    def get_column_meta(self):
        """ Gets Charge_Resumes record column data meta list """
        __list=[('User_Id', 'Integer'), ('Cus_Id', 'Integer'), ('CR_Date_From', 'Date'), ('CR_Date_To', 'Date'), ('CIT_Status', 'Integer'), ('Cur_Code', 'String(3)'), ('CU_Id', 'Integer'), ('CIT_Count', 'Integer'), ('CIT_Quantity', 'Numeric(20,12)'), ('CIT_Generation', 'Integer'), ('CI_CC_Id', 'Integer'), ('CU_Operation', 'String(10)'), ('Typ_Code', 'String(10)'), ('CC_Cur_Code', 'String(3)'), ('CI_Id', 'Integer'), ('Rat_Id', 'Integer'), ('Rat_Price', 'Numeric(20,12)'), ('Rat_MU_Code', 'String(3)'), ('Rat_Cur_Code', 'String(3)'), ('Rat_Period', 'Integer'), ('Rat_Hourly', 'Numeric(20,12)'), ('Rat_Daily', 'Numeric(20,12)'), ('Rat_Monthly', 'Numeric(20,12)'), ('CR_Quantity', 'Numeric(20,12)'), ('CR_Quantity_at_Rate', 'Numeric(20,12)'), ('CC_XR', 'Numeric(20,12)'), ('CR_Cur_XR', 'Numeric(20,12)'), ('CR_ST_at_Rate_Cur', 'Numeric(20,12)'), ('CR_ST_at_CC_Cur', 'Numeric(20,12)'), ('CR_ST_at_Cur', 'Numeric(20,12)'), ('Cus_Name', 'String(255)'), ('CI_Name', 'String(255)'), ('CU_Description', 'String(255)'), ('CC_Description', 'String(255)'), ('Rat_Period_Description', 'String(10)'), ('CC_Code', 'String(45)'), ('Pla_Id', 'Integer'), ('Pla_Name', 'String(255)')]

        return __list

    def search_key(self,User_Id,Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id):
        """ Search for an unique Charge_Resumes record using all key fields (User_Id,Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Charge_Resumes).filter(Charge_Resumes.User_Id==User_Id).filter(Charge_Resumes.Cus_Id==Cus_Id).filter(Charge_Resumes.CR_Date_From==CR_Date_From).filter(Charge_Resumes.CR_Date_To==CR_Date_To).filter(Charge_Resumes.CIT_Status==CIT_Status).filter(Charge_Resumes.Cur_Code==Cur_Code).filter(Charge_Resumes.CU_Id==CU_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Charge_Resumes.search_key(%s,%s,%s,%s,%s,%s,%s): Exception: %s'%(User_Id,Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Charge_Resumes.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Charge_Resumes log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_charge_unit_egm.py
import sqlalchemy
class Charge_Unit_EGM(Base):
    __tablename__ = 'Charge_Unit_EGM'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Charge_Unit_EGM_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Id           = Column( Integer, ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    Archive         = Column( Integer )
    Path            = Column( String(256) )
    Metric          = Column( String(256) )
    Host            = Column( String(45) )
    Port            = Column( Integer )
    User            = Column( String(45) )
    Password        = Column( String(45) )
    Public_Key_File = Column( String(256) )
    Passphrase      = Column( String(256) )
    
    def __init__(self, CU_Id=None, Archive=None, Path='None', Metric='None', Host='localhost', Port=22, User='None', Password='None', Public_Key_File='None', Passphrase='None',engine=None,logger=None):
        """ Initiates a Charge_Unit_EGM class record """
        self.engine=engine
        self.logger=logger
        self.CU_Id           = CU_Id
        self.Archive         = Archive
        self.Path            = Path
        self.Metric          = Metric
        self.Host            = Host
        self.Port            = Port
        self.User            = User
        self.Password        = Password
        self.Public_Key_File = Public_Key_File
        self.Passphrase      = Passphrase

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Charge_Unit_EGM representation function """
        return "<Charge_Unit_EGM( CU_Id='%s', Archive='%s', Path='%s', Metric='%s', Host='%s', Port='%s', User='%s', Password='%s', Public_Key_File='%s', Passphrase='%s')>" % \
                ( self.CU_Id, self.Archive, self.Path, self.Metric, self.Host, self.Port, self.User, self.Password, self.Public_Key_File, self.Passphrase)

    def get_list(self):
        """ Gets Charge_Unit_EGM record in list format """
        __list = [ self.CU_Id, self.Archive, self.Path, self.Metric, self.Host, self.Port, self.User, self.Password, self.Public_Key_File, self.Passphrase]
        return __list

    def get_tuple(self):
        """ Gets Charge_Unit_EGM record in tuple format """
        __tuple = ( self.CU_Id, self.Archive, self.Path, self.Metric, self.Host, self.Port, self.User, self.Password, self.Public_Key_File, self.Passphrase)
        return __tuple

    def get_dict(self):
        """ Gets Charge_Unit_EGM record in dict format """
        __dict={'CU_Id':self.CU_Id,'Archive':self.Archive,'Path':self.Path,'Metric':self.Metric,'Host':self.Host,'Port':self.Port,'User':self.User,'Password':self.Password,'Public_Key_File':self.Public_Key_File,'Passphrase':self.Passphrase}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Charge_Unit_EGM record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Charge_Unit_EGM record column full details list """
        __list=[{'field': 'CU_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CU_Id', 'referenced_table': 'Charge_Units', 'referenced_class': 'charge_unit', 'foreign_key': 'CU_Id', 'foreign_value': 'CU_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Charge Unit Id', 'is_time': False}, {'field': 'Archive', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Archive', 'is_time': False}, {'field': 'Path', 'type': 'varchar(256)', 'type_flask': 'db.String(256)', 'type_sqlalchemy': 'String(256)', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Path', 'is_time': False}, {'field': 'Metric', 'type': 'varchar(256)', 'type_flask': 'db.String(256)', 'type_sqlalchemy': 'String(256)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Metric', 'is_time': False}, {'field': 'Host', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'NO', 'key': '', 'default': 'localhost', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Host', 'is_time': False}, {'field': 'Port', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': '', 'default': '22', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Port', 'is_time': False}, {'field': 'User', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'User', 'is_time': False}, {'field': 'Password', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Password', 'is_time': False}, {'field': 'Public_Key_File', 'type': 'varchar(256)', 'type_flask': 'db.String(256)', 'type_sqlalchemy': 'String(256)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Public_Key_File', 'is_time': False}, {'field': 'Passphrase', 'type': 'varchar(256)', 'type_flask': 'db.String(256)', 'type_sqlalchemy': 'String(256)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Passphrase', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Charge_Unit_EGM record column headers list """
        __list=['CU_Id', 'Archive', 'Path', 'Metric', 'Host', 'Port', 'User', 'Password', 'Public_Key_File', 'Passphrase']

        return __list

    def get_column_types(self):
        """ Gets Charge_Unit_EGM record column data types list """
        __list=['Integer', 'Integer', 'String(256)', 'String(256)', 'String(45)', 'Integer', 'String(45)', 'String(45)', 'String(256)', 'String(256)']

        return __list

    def get_column_meta(self):
        """ Gets Charge_Unit_EGM record column data meta list """
        __list=[('CU_Id', 'Integer'), ('Archive', 'Integer'), ('Path', 'String(256)'), ('Metric', 'String(256)'), ('Host', 'String(45)'), ('Port', 'Integer'), ('User', 'String(45)'), ('Password', 'String(45)'), ('Public_Key_File', 'String(256)'), ('Passphrase', 'String(256)')]

        return __list

    def search_key(self,CU_Id):
        """ Search for an unique Charge_Unit_EGM record using all key fields (CU_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Charge_Unit_EGM).filter(Charge_Unit_EGM.CU_Id==CU_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Charge_Unit_EGM.search_key(%s): Exception: %s'%(CU_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Charge_Unit_EGM.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Charge_Unit_EGM log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_charge_units.py
import sqlalchemy
class Charge_Units(Base):
    __tablename__ = 'Charge_Units'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Charge_Units_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Id                  = Column( Integer, primary_key=True, autoincrement=True )
    CI_Id                  = Column( Integer, ForeignKey('Configuration_Items.CI_Id') )
    CU_Description         = Column( String(255) )
    CU_UUID                = Column( String(45) )
    CU_Is_Billeable        = Column( Boolean )
    CU_Is_Always_Billeable = Column( Boolean )
    CU_Quantity            = Column( Numeric(20,12) )
    CU_Operation           = Column( String(10), ForeignKey('CU_Operations.CU_Operation') )
    Typ_Code               = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    CIT_Generation         = Column( Integer, ForeignKey('CIT_Generations.CIT_Generation') )
    Rat_Id                 = Column( Integer )
    CU_Reference_1         = Column( String(45) )
    CU_Reference_2         = Column( String(45) )
    CU_Reference_3         = Column( String(45) )
    
    def __init__(self, CU_Id=0, CI_Id=None, CU_Description='None', CU_UUID='None', CU_Is_Billeable=0, CU_Is_Always_Billeable=0, CU_Quantity=None, CU_Operation='None', Typ_Code='None', CIT_Generation=None, Rat_Id=None, CU_Reference_1='None', CU_Reference_2='None', CU_Reference_3='None',engine=None,logger=None):
        """ Initiates a Charge_Units class record """
        self.engine=engine
        self.logger=logger
        self.CU_Id                  = CU_Id
        self.CI_Id                  = CI_Id
        self.CU_Description         = CU_Description
        self.CU_UUID                = CU_UUID
        self.CU_Is_Billeable        = CU_Is_Billeable
        self.CU_Is_Always_Billeable = CU_Is_Always_Billeable
        self.CU_Quantity            = CU_Quantity
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CIT_Generation         = CIT_Generation
        self.Rat_Id                 = Rat_Id
        self.CU_Reference_1         = CU_Reference_1
        self.CU_Reference_2         = CU_Reference_2
        self.CU_Reference_3         = CU_Reference_3

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Charge_Units representation function """
        return "<Charge_Units( CU_Id='%s', CI_Id='%s', CU_Description='%s', CU_UUID='%s', CU_Is_Billeable='%s', CU_Is_Always_Billeable='%s', CU_Quantity='%s', CU_Operation='%s', Typ_Code='%s', CIT_Generation='%s', Rat_Id='%s', CU_Reference_1='%s', CU_Reference_2='%s', CU_Reference_3='%s')>" % \
                ( self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3)

    def get_list(self):
        """ Gets Charge_Units record in list format """
        __list = [ self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3]
        return __list

    def get_tuple(self):
        """ Gets Charge_Units record in tuple format """
        __tuple = ( self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3)
        return __tuple

    def get_dict(self):
        """ Gets Charge_Units record in dict format """
        __dict={'CU_Id':self.CU_Id,'CI_Id':self.CI_Id,'CU_Description':self.CU_Description,'CU_UUID':self.CU_UUID,'CU_Is_Billeable':self.CU_Is_Billeable,'CU_Is_Always_Billeable':self.CU_Is_Always_Billeable,'CU_Quantity':self.CU_Quantity,'CU_Operation':self.CU_Operation,'Typ_Code':self.Typ_Code,'CIT_Generation':self.CIT_Generation,'Rat_Id':self.Rat_Id,'CU_Reference_1':self.CU_Reference_1,'CU_Reference_2':self.CU_Reference_2,'CU_Reference_3':self.CU_Reference_3}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Charge_Units record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Charge_Units record column full details list """
        __list=[{'field': 'CU_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'Id', 'is_time': False}, {'field': 'CI_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CI_Id', 'referenced_table': 'Configuration_Items', 'referenced_class': 'configuration_item', 'foreign_key': 'CI_Id', 'foreign_value': 'CI_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Configuration Item Id', 'is_time': False}, {'field': 'CU_Description', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Description', 'is_time': False}, {'field': 'CU_UUID', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'UUID', 'is_time': False}, {'field': 'CU_Is_Billeable', 'type': 'tinyint', 'type_flask': 'db.Boolean', 'type_sqlalchemy': 'Boolean', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'BooleanField', 'is_id': False, 'header': 'Is Billeable', 'is_time': False}, {'field': 'CU_Is_Always_Billeable', 'type': 'tinyint', 'type_flask': 'db.Boolean', 'type_sqlalchemy': 'Boolean', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'BooleanField', 'is_id': False, 'header': 'Is Always Billeable', 'is_time': False}, {'field': 'CU_Quantity', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Quantity', 'is_time': False}, {'field': 'CU_Operation', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CU_Operation', 'referenced_table': 'CU_Operations', 'referenced_class': 'cu_operation', 'foreign_key': 'CU_Operation', 'foreign_value': 'Value', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Conversion Operation', 'is_time': False}, {'field': 'Typ_Code', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Typ_Code', 'referenced_table': 'CU_Types', 'referenced_class': 'cu_type', 'foreign_key': 'Typ_Code', 'foreign_value': 'Typ_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Type', 'is_time': False}, {'field': 'CIT_Generation', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CIT_Generation', 'referenced_table': 'CIT_Generations', 'referenced_class': 'cit_generation', 'foreign_key': 'CIT_Generation', 'foreign_value': 'Value', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Item Generation Type', 'is_time': False}, {'field': 'Rat_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 11, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Rate Id', 'is_time': False}, {'field': 'CU_Reference_1', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 12, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Reference 1', 'is_time': False}, {'field': 'CU_Reference_2', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 13, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Reference 2', 'is_time': False}, {'field': 'CU_Reference_3', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 14, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Reference 3', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Charge_Units record column headers list """
        __list=['CU_Id', 'CI_Id', 'CU_Description', 'CU_UUID', 'CU_Is_Billeable', 'CU_Is_Always_Billeable', 'CU_Quantity', 'CU_Operation', 'Typ_Code', 'CIT_Generation', 'Rat_Id', 'CU_Reference_1', 'CU_Reference_2', 'CU_Reference_3']

        return __list

    def get_column_types(self):
        """ Gets Charge_Units record column data types list """
        __list=['Integer', 'Integer', 'String(255)', 'String(45)', 'Boolean', 'Boolean', 'Numeric(20,12)', 'String(10)', 'String(10)', 'Integer', 'Integer', 'String(45)', 'String(45)', 'String(45)']

        return __list

    def get_column_meta(self):
        """ Gets Charge_Units record column data meta list """
        __list=[('CU_Id', 'Integer'), ('CI_Id', 'Integer'), ('CU_Description', 'String(255)'), ('CU_UUID', 'String(45)'), ('CU_Is_Billeable', 'Boolean'), ('CU_Is_Always_Billeable', 'Boolean'), ('CU_Quantity', 'Numeric(20,12)'), ('CU_Operation', 'String(10)'), ('Typ_Code', 'String(10)'), ('CIT_Generation', 'Integer'), ('Rat_Id', 'Integer'), ('CU_Reference_1', 'String(45)'), ('CU_Reference_2', 'String(45)'), ('CU_Reference_3', 'String(45)')]

        return __list

    def search_key(self,CU_Id):
        """ Search for an unique Charge_Units record using all key fields (CU_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Charge_Units).filter(Charge_Units.CU_Id==CU_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Charge_Units.search_key(%s): Exception: %s'%(CU_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Charge_Units.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Charge_Units log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_configuration_items.py
import sqlalchemy
class Configuration_Items(Base):
    __tablename__ = 'Configuration_Items'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Configuration_Items_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CI_Id                       = Column( Integer, primary_key=True, autoincrement=True )
    CI_Name                     = Column( String(255) )
    CI_UUID                     = Column( String(45) )
    Pla_Id                      = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id                       = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    Cus_Id                      = Column( Integer, ForeignKey('Customers.Cus_Id') )
    CI_Commissioning_DateTime   = Column( DateTime )
    CI_Decommissioning_DateTime = Column( DateTime )
    
    def __init__(self, CI_Id=0, CI_Name='None', CI_UUID='None', Pla_Id=None, CC_Id=None, Cus_Id=1, CI_Commissioning_DateTime=None, CI_Decommissioning_DateTime=None,engine=None,logger=None):
        """ Initiates a Configuration_Items class record """
        self.engine=engine
        self.logger=logger
        self.CI_Id                       = CI_Id
        self.CI_Name                     = CI_Name
        self.CI_UUID                     = CI_UUID
        self.Pla_Id                      = Pla_Id
        self.CC_Id                       = CC_Id
        self.Cus_Id                      = Cus_Id
        self.CI_Commissioning_DateTime   = CI_Commissioning_DateTime
        self.CI_Decommissioning_DateTime = CI_Decommissioning_DateTime

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Configuration_Items representation function """
        return "<Configuration_Items( CI_Id='%s', CI_Name='%s', CI_UUID='%s', Pla_Id='%s', CC_Id='%s', Cus_Id='%s', CI_Commissioning_DateTime='%s', CI_Decommissioning_DateTime='%s')>" % \
                ( self.CI_Id, self.CI_Name, self.CI_UUID, self.Pla_Id, self.CC_Id, self.Cus_Id, self.CI_Commissioning_DateTime, self.CI_Decommissioning_DateTime)

    def get_list(self):
        """ Gets Configuration_Items record in list format """
        __list = [ self.CI_Id, self.CI_Name, self.CI_UUID, self.Pla_Id, self.CC_Id, self.Cus_Id, self.CI_Commissioning_DateTime, self.CI_Decommissioning_DateTime]
        return __list

    def get_tuple(self):
        """ Gets Configuration_Items record in tuple format """
        __tuple = ( self.CI_Id, self.CI_Name, self.CI_UUID, self.Pla_Id, self.CC_Id, self.Cus_Id, self.CI_Commissioning_DateTime, self.CI_Decommissioning_DateTime)
        return __tuple

    def get_dict(self):
        """ Gets Configuration_Items record in dict format """
        __dict={'CI_Id':self.CI_Id,'CI_Name':self.CI_Name,'CI_UUID':self.CI_UUID,'Pla_Id':self.Pla_Id,'CC_Id':self.CC_Id,'Cus_Id':self.Cus_Id,'CI_Commissioning_DateTime':self.CI_Commissioning_DateTime,'CI_Decommissioning_DateTime':self.CI_Decommissioning_DateTime}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Configuration_Items record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Configuration_Items record column full details list """
        __list=[{'field': 'CI_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'Id', 'is_time': False}, {'field': 'CI_Name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Name', 'is_time': False}, {'field': 'CI_UUID', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'UUID', 'is_time': False}, {'field': 'Pla_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Pla_Id', 'referenced_table': 'Platforms', 'referenced_class': 'platform', 'foreign_key': 'Pla_Id', 'foreign_value': 'Pla_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Platform Id', 'is_time': False}, {'field': 'CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CC_Id', 'referenced_table': 'Cost_Centers', 'referenced_class': 'cost_center', 'foreign_key': 'CC_Id', 'foreign_value': 'CC_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Cost Center Id', 'is_time': False}, {'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Cus_Id', 'referenced_table': 'Customers', 'referenced_class': 'customer', 'foreign_key': 'Cus_Id', 'foreign_value': 'Cus_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Customer Id', 'is_time': False}, {'field': 'CI_Commissioning_DateTime', 'type': 'timestamp', 'type_flask': 'db.DateTime', 'type_sqlalchemy': 'DateTime', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateTimeField', 'is_id': False, 'header': 'Commissioning Date and Time', 'is_time': False}, {'field': 'CI_Decommissioning_DateTime', 'type': 'timestamp', 'type_flask': 'db.DateTime', 'type_sqlalchemy': 'DateTime', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateTimeField', 'is_id': False, 'header': 'Decommissioning Date and Time', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Configuration_Items record column headers list """
        __list=['CI_Id', 'CI_Name', 'CI_UUID', 'Pla_Id', 'CC_Id', 'Cus_Id', 'CI_Commissioning_DateTime', 'CI_Decommissioning_DateTime']

        return __list

    def get_column_types(self):
        """ Gets Configuration_Items record column data types list """
        __list=['Integer', 'String(255)', 'String(45)', 'Integer', 'Integer', 'Integer', 'DateTime', 'DateTime']

        return __list

    def get_column_meta(self):
        """ Gets Configuration_Items record column data meta list """
        __list=[('CI_Id', 'Integer'), ('CI_Name', 'String(255)'), ('CI_UUID', 'String(45)'), ('Pla_Id', 'Integer'), ('CC_Id', 'Integer'), ('Cus_Id', 'Integer'), ('CI_Commissioning_DateTime', 'DateTime'), ('CI_Decommissioning_DateTime', 'DateTime')]

        return __list

    def search_key(self,CI_Id):
        """ Search for an unique Configuration_Items record using all key fields (CI_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Configuration_Items).filter(Configuration_Items.CI_Id==CI_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Configuration_Items.search_key(%s): Exception: %s'%(CI_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Configuration_Items.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Configuration_Items log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_cost_centers.py
import sqlalchemy
class Cost_Centers(Base):
    __tablename__ = 'Cost_Centers'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Cost_Centers_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CC_Id          = Column( Integer, primary_key=True, autoincrement=True )
    CC_Code        = Column( String(45) )
    CC_Description = Column( String(255) )
    Cur_Code       = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    CC_Parent_Code = Column( String(45) )
    CC_Reg_Exp     = Column( String(45) )
    CC_Reference   = Column( String(245) )
    Cus_Id         = Column( Integer )
    
    def __init__(self, CC_Id=0, CC_Code='None', CC_Description='None', Cur_Code='None', CC_Parent_Code='1', CC_Reg_Exp='None', CC_Reference='None', Cus_Id=None,engine=None,logger=None):
        """ Initiates a Cost_Centers class record """
        self.engine=engine
        self.logger=logger
        self.CC_Id          = CC_Id
        self.CC_Code        = CC_Code
        self.CC_Description = CC_Description
        self.Cur_Code       = Cur_Code
        self.CC_Parent_Code = CC_Parent_Code
        self.CC_Reg_Exp     = CC_Reg_Exp
        self.CC_Reference   = CC_Reference
        self.Cus_Id         = Cus_Id

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Cost_Centers representation function """
        return "<Cost_Centers( CC_Id='%s', CC_Code='%s', CC_Description='%s', Cur_Code='%s', CC_Parent_Code='%s', CC_Reg_Exp='%s', CC_Reference='%s', Cus_Id='%s')>" % \
                ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code, self.CC_Parent_Code, self.CC_Reg_Exp, self.CC_Reference, self.Cus_Id)

    def get_list(self):
        """ Gets Cost_Centers record in list format """
        __list = [ self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code, self.CC_Parent_Code, self.CC_Reg_Exp, self.CC_Reference, self.Cus_Id]
        return __list

    def get_tuple(self):
        """ Gets Cost_Centers record in tuple format """
        __tuple = ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code, self.CC_Parent_Code, self.CC_Reg_Exp, self.CC_Reference, self.Cus_Id)
        return __tuple

    def get_dict(self):
        """ Gets Cost_Centers record in dict format """
        __dict={'CC_Id':self.CC_Id,'CC_Code':self.CC_Code,'CC_Description':self.CC_Description,'Cur_Code':self.Cur_Code,'CC_Parent_Code':self.CC_Parent_Code,'CC_Reg_Exp':self.CC_Reg_Exp,'CC_Reference':self.CC_Reference,'Cus_Id':self.Cus_Id}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Cost_Centers record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Cost_Centers record column full details list """
        __list=[{'field': 'CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'Cost Center Id', 'is_time': False}, {'field': 'CC_Code', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Code', 'is_time': False}, {'field': 'CC_Description', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Description', 'is_time': False}, {'field': 'Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Cur_Code', 'referenced_table': 'Currencies', 'referenced_class': 'currency', 'foreign_key': 'Cur_Code', 'foreign_value': 'Cur_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Currency Code', 'is_time': False}, {'field': 'CC_Parent_Code', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'NO', 'key': '', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Parent Code', 'is_time': False}, {'field': 'CC_Reg_Exp', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': False, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Regular Expression', 'is_time': False}, {'field': 'CC_Reference', 'type': 'varchar(245)', 'type_flask': 'db.String(245)', 'type_sqlalchemy': 'String(245)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Reference', 'is_time': False}, {'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Cus_Id', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Cost_Centers record column headers list """
        __list=['CC_Id', 'CC_Code', 'CC_Description', 'Cur_Code', 'CC_Parent_Code', 'CC_Reg_Exp', 'CC_Reference', 'Cus_Id']

        return __list

    def get_column_types(self):
        """ Gets Cost_Centers record column data types list """
        __list=['Integer', 'String(45)', 'String(255)', 'String(3)', 'String(45)', 'String(45)', 'String(245)', 'Integer']

        return __list

    def get_column_meta(self):
        """ Gets Cost_Centers record column data meta list """
        __list=[('CC_Id', 'Integer'), ('CC_Code', 'String(45)'), ('CC_Description', 'String(255)'), ('Cur_Code', 'String(3)'), ('CC_Parent_Code', 'String(45)'), ('CC_Reg_Exp', 'String(45)'), ('CC_Reference', 'String(245)'), ('Cus_Id', 'Integer')]

        return __list

    def search_key(self,CC_Id):
        """ Search for an unique Cost_Centers record using all key fields (CC_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Cost_Centers).filter(Cost_Centers.CC_Id==CC_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Cost_Centers.search_key(%s): Exception: %s'%(CC_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Cost_Centers.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Cost_Centers log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_countries.py
import sqlalchemy
class Countries(Base):
    __tablename__ = 'Countries'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Countries_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Cou_Code = Column( String(2), primary_key=True )
    Cou_Name = Column( String(45) )
    Cou_A3   = Column( String(3) )
    Cou_N    = Column( Integer )
    
    def __init__(self, Cou_Code='None', Cou_Name='None', Cou_A3='None', Cou_N=None,engine=None,logger=None):
        """ Initiates a Countries class record """
        self.engine=engine
        self.logger=logger
        self.Cou_Code = Cou_Code
        self.Cou_Name = Cou_Name
        self.Cou_A3   = Cou_A3
        self.Cou_N    = Cou_N

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Countries representation function """
        return "<Countries( Cou_Code='%s', Cou_Name='%s', Cou_A3='%s', Cou_N='%s')>" % \
                ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)

    def get_list(self):
        """ Gets Countries record in list format """
        __list = [ self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N]
        return __list

    def get_tuple(self):
        """ Gets Countries record in tuple format """
        __tuple = ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)
        return __tuple

    def get_dict(self):
        """ Gets Countries record in dict format """
        __dict={'Cou_Code':self.Cou_Code,'Cou_Name':self.Cou_Name,'Cou_A3':self.Cou_A3,'Cou_N':self.Cou_N}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Countries record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Countries record column full details list """
        __list=[{'field': 'Cou_Code', 'type': 'varchar(2)', 'type_flask': 'db.String(2)', 'type_sqlalchemy': 'String(2)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Code', 'is_time': False}, {'field': 'Cou_Name', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Name', 'is_time': False}, {'field': 'Cou_A3', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Alphanum Code', 'is_time': False}, {'field': 'Cou_N', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'ISO Numeric Code', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Countries record column headers list """
        __list=['Cou_Code', 'Cou_Name', 'Cou_A3', 'Cou_N']

        return __list

    def get_column_types(self):
        """ Gets Countries record column data types list """
        __list=['String(2)', 'String(45)', 'String(3)', 'Integer']

        return __list

    def get_column_meta(self):
        """ Gets Countries record column data meta list """
        __list=[('Cou_Code', 'String(2)'), ('Cou_Name', 'String(45)'), ('Cou_A3', 'String(3)'), ('Cou_N', 'Integer')]

        return __list

    def search_key(self,Cou_Code):
        """ Search for an unique Countries record using all key fields (Cou_Code) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Countries).filter(Countries.Cou_Code==Cou_Code).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Countries.search_key(%s): Exception: %s'%(Cou_Code,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Countries.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Countries log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_countries_currencies.py
import sqlalchemy
class Countries_Currencies(Base):
    __tablename__ = 'Countries_Currencies'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Countries_Currencies_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Cou_Code        = Column( String(2), ForeignKey('Countries.Cou_Code'), primary_key=True )
    Cur_Code        = Column( String(3), ForeignKey('Currencies.Cur_Code'), primary_key=True )
    Cou_Cur_Comment = Column( String(45) )
    
    def __init__(self, Cou_Code='None', Cur_Code='None', Cou_Cur_Comment='None',engine=None,logger=None):
        """ Initiates a Countries_Currencies class record """
        self.engine=engine
        self.logger=logger
        self.Cou_Code        = Cou_Code
        self.Cur_Code        = Cur_Code
        self.Cou_Cur_Comment = Cou_Cur_Comment

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Countries_Currencies representation function """
        return "<Countries_Currencies( Cou_Code='%s', Cur_Code='%s', Cou_Cur_Comment='%s')>" % \
                ( self.Cou_Code, self.Cur_Code, self.Cou_Cur_Comment)

    def get_list(self):
        """ Gets Countries_Currencies record in list format """
        __list = [ self.Cou_Code, self.Cur_Code, self.Cou_Cur_Comment]
        return __list

    def get_tuple(self):
        """ Gets Countries_Currencies record in tuple format """
        __tuple = ( self.Cou_Code, self.Cur_Code, self.Cou_Cur_Comment)
        return __tuple

    def get_dict(self):
        """ Gets Countries_Currencies record in dict format """
        __dict={'Cou_Code':self.Cou_Code,'Cur_Code':self.Cur_Code,'Cou_Cur_Comment':self.Cou_Cur_Comment}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Countries_Currencies record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Countries_Currencies record column full details list """
        __list=[{'field': 'Cou_Code', 'type': 'varchar(2)', 'type_flask': 'db.String(2)', 'type_sqlalchemy': 'String(2)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Cou_Code', 'referenced_table': 'Countries', 'referenced_class': 'country', 'foreign_key': 'Cou_Code', 'foreign_value': 'Cou_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Country Code', 'is_time': False}, {'field': 'Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Cur_Code', 'referenced_table': 'Currencies', 'referenced_class': 'currency', 'foreign_key': 'Cur_Code', 'foreign_value': 'Cur_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Currency Code', 'is_time': False}, {'field': 'Cou_Cur_Comment', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Comment', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Countries_Currencies record column headers list """
        __list=['Cou_Code', 'Cur_Code', 'Cou_Cur_Comment']

        return __list

    def get_column_types(self):
        """ Gets Countries_Currencies record column data types list """
        __list=['String(2)', 'String(3)', 'String(45)']

        return __list

    def get_column_meta(self):
        """ Gets Countries_Currencies record column data meta list """
        __list=[('Cou_Code', 'String(2)'), ('Cur_Code', 'String(3)'), ('Cou_Cur_Comment', 'String(45)')]

        return __list

    def search_key(self,Cou_Code,Cur_Code):
        """ Search for an unique Countries_Currencies record using all key fields (Cou_Code,Cur_Code) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Countries_Currencies).filter(Countries_Currencies.Cou_Code==Cou_Code).filter(Countries_Currencies.Cur_Code==Cur_Code).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Countries_Currencies.search_key(%s,%s): Exception: %s'%(Cou_Code,Cur_Code,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Countries_Currencies.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Countries_Currencies log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_currencies.py
import sqlalchemy
class Currencies(Base):
    __tablename__ = 'Currencies'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Currencies_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Cur_Code    = Column( String(3), primary_key=True )
    Cur_Name    = Column( String(45) )
    Cur_Id      = Column( Integer )
    Cur_Comment = Column( String(128) )
    
    def __init__(self, Cur_Code='None', Cur_Name='None', Cur_Id=None, Cur_Comment='None',engine=None,logger=None):
        """ Initiates a Currencies class record """
        self.engine=engine
        self.logger=logger
        self.Cur_Code    = Cur_Code
        self.Cur_Name    = Cur_Name
        self.Cur_Id      = Cur_Id
        self.Cur_Comment = Cur_Comment

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Currencies representation function """
        return "<Currencies( Cur_Code='%s', Cur_Name='%s', Cur_Id='%s', Cur_Comment='%s')>" % \
                ( self.Cur_Code, self.Cur_Name, self.Cur_Id, self.Cur_Comment)

    def get_list(self):
        """ Gets Currencies record in list format """
        __list = [ self.Cur_Code, self.Cur_Name, self.Cur_Id, self.Cur_Comment]
        return __list

    def get_tuple(self):
        """ Gets Currencies record in tuple format """
        __tuple = ( self.Cur_Code, self.Cur_Name, self.Cur_Id, self.Cur_Comment)
        return __tuple

    def get_dict(self):
        """ Gets Currencies record in dict format """
        __dict={'Cur_Code':self.Cur_Code,'Cur_Name':self.Cur_Name,'Cur_Id':self.Cur_Id,'Cur_Comment':self.Cur_Comment}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Currencies record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Currencies record column full details list """
        __list=[{'field': 'Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Code', 'is_time': False}, {'field': 'Cur_Name', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Name', 'is_time': False}, {'field': 'Cur_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Id', 'is_time': False}, {'field': 'Cur_Comment', 'type': 'varchar(128)', 'type_flask': 'db.String(128)', 'type_sqlalchemy': 'String(128)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Comment', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Currencies record column headers list """
        __list=['Cur_Code', 'Cur_Name', 'Cur_Id', 'Cur_Comment']

        return __list

    def get_column_types(self):
        """ Gets Currencies record column data types list """
        __list=['String(3)', 'String(45)', 'Integer', 'String(128)']

        return __list

    def get_column_meta(self):
        """ Gets Currencies record column data meta list """
        __list=[('Cur_Code', 'String(3)'), ('Cur_Name', 'String(45)'), ('Cur_Id', 'Integer'), ('Cur_Comment', 'String(128)')]

        return __list

    def search_key(self,Cur_Code):
        """ Search for an unique Currencies record using all key fields (Cur_Code) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Currencies).filter(Currencies.Cur_Code==Cur_Code).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Currencies.search_key(%s): Exception: %s'%(Cur_Code,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Currencies.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Currencies log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_customers.py
import sqlalchemy
class Customers(Base):
    __tablename__ = 'Customers'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Customers_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Cus_Id   = Column( Integer, primary_key=True, autoincrement=True )
    Cus_Name = Column( String(255) )
    CC_Id    = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    
    def __init__(self, Cus_Id=0, Cus_Name='None', CC_Id=None,engine=None,logger=None):
        """ Initiates a Customers class record """
        self.engine=engine
        self.logger=logger
        self.Cus_Id   = Cus_Id
        self.Cus_Name = Cus_Name
        self.CC_Id    = CC_Id

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Customers representation function """
        return "<Customers( Cus_Id='%s', Cus_Name='%s', CC_Id='%s')>" % \
                ( self.Cus_Id, self.Cus_Name, self.CC_Id)

    def get_list(self):
        """ Gets Customers record in list format """
        __list = [ self.Cus_Id, self.Cus_Name, self.CC_Id]
        return __list

    def get_tuple(self):
        """ Gets Customers record in tuple format """
        __tuple = ( self.Cus_Id, self.Cus_Name, self.CC_Id)
        return __tuple

    def get_dict(self):
        """ Gets Customers record in dict format """
        __dict={'Cus_Id':self.Cus_Id,'Cus_Name':self.Cus_Name,'CC_Id':self.CC_Id}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Customers record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Customers record column full details list """
        __list=[{'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'Id', 'is_time': False}, {'field': 'Cus_Name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'NO', 'key': 'UNI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Name', 'is_time': False}, {'field': 'CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CC_Id', 'referenced_table': 'Cost_Centers', 'referenced_class': 'cost_center', 'foreign_key': 'CC_Id', 'foreign_value': 'CC_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Cost Center Id', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Customers record column headers list """
        __list=['Cus_Id', 'Cus_Name', 'CC_Id']

        return __list

    def get_column_types(self):
        """ Gets Customers record column data types list """
        __list=['Integer', 'String(255)', 'Integer']

        return __list

    def get_column_meta(self):
        """ Gets Customers record column data meta list """
        __list=[('Cus_Id', 'Integer'), ('Cus_Name', 'String(255)'), ('CC_Id', 'Integer')]

        return __list

    def search_key(self,Cus_Id):
        """ Search for an unique Customers record using all key fields (Cus_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Customers).filter(Customers.Cus_Id==Cus_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Customers.search_key(%s): Exception: %s'%(Cus_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Customers.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Customers log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_exchange_rates.py
import sqlalchemy
class Exchange_Rates(Base):
    __tablename__ = 'Exchange_Rates'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Exchange_Rates_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    ER_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Cur_Code  = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    ER_Factor = Column( Numeric(20,12) )
    ER_Date   = Column( Date )
    
    def __init__(self, ER_Id=0, Cur_Code='None', ER_Factor=None, ER_Date=None,engine=None,logger=None):
        """ Initiates a Exchange_Rates class record """
        self.engine=engine
        self.logger=logger
        self.ER_Id     = ER_Id
        self.Cur_Code  = Cur_Code
        self.ER_Factor = ER_Factor
        self.ER_Date   = ER_Date

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Exchange_Rates representation function """
        return "<Exchange_Rates( ER_Id='%s', Cur_Code='%s', ER_Factor='%s', ER_Date='%s')>" % \
                ( self.ER_Id, self.Cur_Code, self.ER_Factor, self.ER_Date)

    def get_list(self):
        """ Gets Exchange_Rates record in list format """
        __list = [ self.ER_Id, self.Cur_Code, self.ER_Factor, self.ER_Date]
        return __list

    def get_tuple(self):
        """ Gets Exchange_Rates record in tuple format """
        __tuple = ( self.ER_Id, self.Cur_Code, self.ER_Factor, self.ER_Date)
        return __tuple

    def get_dict(self):
        """ Gets Exchange_Rates record in dict format """
        __dict={'ER_Id':self.ER_Id,'Cur_Code':self.Cur_Code,'ER_Factor':self.ER_Factor,'ER_Date':self.ER_Date}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Exchange_Rates record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Exchange_Rates record column full details list """
        __list=[{'field': 'ER_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'Id', 'is_time': False}, {'field': 'Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Cur_Code', 'referenced_table': 'Currencies', 'referenced_class': 'currency', 'foreign_key': 'Cur_Code', 'foreign_value': 'Cur_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Currency Code', 'is_time': False}, {'field': 'ER_Factor', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Factor', 'is_time': False}, {'field': 'ER_Date', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'Date', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Exchange_Rates record column headers list """
        __list=['ER_Id', 'Cur_Code', 'ER_Factor', 'ER_Date']

        return __list

    def get_column_types(self):
        """ Gets Exchange_Rates record column data types list """
        __list=['Integer', 'String(3)', 'Numeric(20,12)', 'Date']

        return __list

    def get_column_meta(self):
        """ Gets Exchange_Rates record column data meta list """
        __list=[('ER_Id', 'Integer'), ('Cur_Code', 'String(3)'), ('ER_Factor', 'Numeric(20,12)'), ('ER_Date', 'Date')]

        return __list

    def search_key(self,ER_Id):
        """ Search for an unique Exchange_Rates record using all key fields (ER_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Exchange_Rates).filter(Exchange_Rates.ER_Id==ER_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Exchange_Rates.search_key(%s): Exception: %s'%(ER_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Exchange_Rates.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Exchange_Rates log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_interface.py
import sqlalchemy
class Interface(Base):
    __tablename__ = 'Interface'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Interface_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Id          = Column( Integer, primary_key=True, autoincrement=True )
    User_Id     = Column( Integer )
    Table_name  = Column( String(45) )
    Option_Type = Column( Integer )
    Argument_1  = Column( String(256) )
    Argument_2  = Column( String(256) )
    Argument_3  = Column( String(256) )
    Is_Active   = Column( Boolean )
    
    def __init__(self, Id=0, User_Id=None, Table_name='None', Option_Type=None, Argument_1='None', Argument_2='None', Argument_3='None', Is_Active=None,engine=None,logger=None):
        """ Initiates a Interface class record """
        self.engine=engine
        self.logger=logger
        self.Id          = Id
        self.User_Id     = User_Id
        self.Table_name  = Table_name
        self.Option_Type = Option_Type
        self.Argument_1  = Argument_1
        self.Argument_2  = Argument_2
        self.Argument_3  = Argument_3
        self.Is_Active   = Is_Active

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Interface representation function """
        return "<Interface( Id='%s', User_Id='%s', Table_name='%s', Option_Type='%s', Argument_1='%s', Argument_2='%s', Argument_3='%s', Is_Active='%s')>" % \
                ( self.Id, self.User_Id, self.Table_name, self.Option_Type, self.Argument_1, self.Argument_2, self.Argument_3, self.Is_Active)

    def get_list(self):
        """ Gets Interface record in list format """
        __list = [ self.Id, self.User_Id, self.Table_name, self.Option_Type, self.Argument_1, self.Argument_2, self.Argument_3, self.Is_Active]
        return __list

    def get_tuple(self):
        """ Gets Interface record in tuple format """
        __tuple = ( self.Id, self.User_Id, self.Table_name, self.Option_Type, self.Argument_1, self.Argument_2, self.Argument_3, self.Is_Active)
        return __tuple

    def get_dict(self):
        """ Gets Interface record in dict format """
        __dict={'Id':self.Id,'User_Id':self.User_Id,'Table_name':self.Table_name,'Option_Type':self.Option_Type,'Argument_1':self.Argument_1,'Argument_2':self.Argument_2,'Argument_3':self.Argument_3,'Is_Active':self.Is_Active}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Interface record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Interface record column full details list """
        __list=[{'field': 'Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'Id', 'is_time': False}, {'field': 'User_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'User_Id', 'is_time': False}, {'field': 'Table_name', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Table_name', 'is_time': False}, {'field': 'Option_Type', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Option_Type', 'is_time': False}, {'field': 'Argument_1', 'type': 'varchar(256)', 'type_flask': 'db.String(256)', 'type_sqlalchemy': 'String(256)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Argument_1', 'is_time': False}, {'field': 'Argument_2', 'type': 'varchar(256)', 'type_flask': 'db.String(256)', 'type_sqlalchemy': 'String(256)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Argument_2', 'is_time': False}, {'field': 'Argument_3', 'type': 'varchar(256)', 'type_flask': 'db.String(256)', 'type_sqlalchemy': 'String(256)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Argument_3', 'is_time': False}, {'field': 'Is_Active', 'type': 'tinyint', 'type_flask': 'db.Boolean', 'type_sqlalchemy': 'Boolean', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'BooleanField', 'is_id': False, 'header': 'Is_Active', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Interface record column headers list """
        __list=['Id', 'User_Id', 'Table_name', 'Option_Type', 'Argument_1', 'Argument_2', 'Argument_3', 'Is_Active']

        return __list

    def get_column_types(self):
        """ Gets Interface record column data types list """
        __list=['Integer', 'Integer', 'String(45)', 'Integer', 'String(256)', 'String(256)', 'String(256)', 'Boolean']

        return __list

    def get_column_meta(self):
        """ Gets Interface record column data meta list """
        __list=[('Id', 'Integer'), ('User_Id', 'Integer'), ('Table_name', 'String(45)'), ('Option_Type', 'Integer'), ('Argument_1', 'String(256)'), ('Argument_2', 'String(256)'), ('Argument_3', 'String(256)'), ('Is_Active', 'Boolean')]

        return __list

    def search_key(self,Id):
        """ Search for an unique Interface record using all key fields (Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Interface).filter(Interface.Id==Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Interface.search_key(%s): Exception: %s'%(Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Interface.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Interface log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_measure_units.py
import sqlalchemy
class Measure_Units(Base):
    __tablename__ = 'Measure_Units'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Measure_Units_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    MU_Code        = Column( String(3), primary_key=True )
    MU_Description = Column( String(45) )
    
    def __init__(self, MU_Code='None', MU_Description='None',engine=None,logger=None):
        """ Initiates a Measure_Units class record """
        self.engine=engine
        self.logger=logger
        self.MU_Code        = MU_Code
        self.MU_Description = MU_Description

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Measure_Units representation function """
        return "<Measure_Units( MU_Code='%s', MU_Description='%s')>" % \
                ( self.MU_Code, self.MU_Description)

    def get_list(self):
        """ Gets Measure_Units record in list format """
        __list = [ self.MU_Code, self.MU_Description]
        return __list

    def get_tuple(self):
        """ Gets Measure_Units record in tuple format """
        __tuple = ( self.MU_Code, self.MU_Description)
        return __tuple

    def get_dict(self):
        """ Gets Measure_Units record in dict format """
        __dict={'MU_Code':self.MU_Code,'MU_Description':self.MU_Description}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Measure_Units record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Measure_Units record column full details list """
        __list=[{'field': 'MU_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Code', 'is_time': False}, {'field': 'MU_Description', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Description', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Measure_Units record column headers list """
        __list=['MU_Code', 'MU_Description']

        return __list

    def get_column_types(self):
        """ Gets Measure_Units record column data types list """
        __list=['String(3)', 'String(45)']

        return __list

    def get_column_meta(self):
        """ Gets Measure_Units record column data meta list """
        __list=[('MU_Code', 'String(3)'), ('MU_Description', 'String(45)')]

        return __list

    def search_key(self,MU_Code):
        """ Search for an unique Measure_Units record using all key fields (MU_Code) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Measure_Units).filter(Measure_Units.MU_Code==MU_Code).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Measure_Units.search_key(%s): Exception: %s'%(MU_Code,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Measure_Units.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Measure_Units log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_platforms.py
import sqlalchemy
class Platforms(Base):
    __tablename__ = 'Platforms'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Platforms_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Pla_Id       = Column( Integer, primary_key=True, autoincrement=True )
    Pla_Name     = Column( String(255) )
    Pla_Host     = Column( String(45) )
    Pla_Port     = Column( String(45) )
    Pla_User     = Column( String(45) )
    Pla_Password = Column( String(45) )
    
    def __init__(self, Pla_Id=0, Pla_Name='None', Pla_Host='None', Pla_Port='None', Pla_User='None', Pla_Password='None',engine=None,logger=None):
        """ Initiates a Platforms class record """
        self.engine=engine
        self.logger=logger
        self.Pla_Id       = Pla_Id
        self.Pla_Name     = Pla_Name
        self.Pla_Host     = Pla_Host
        self.Pla_Port     = Pla_Port
        self.Pla_User     = Pla_User
        self.Pla_Password = Pla_Password

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Platforms representation function """
        return "<Platforms( Pla_Id='%s', Pla_Name='%s', Pla_Host='%s', Pla_Port='%s', Pla_User='%s', Pla_Password='%s')>" % \
                ( self.Pla_Id, self.Pla_Name, self.Pla_Host, self.Pla_Port, self.Pla_User, self.Pla_Password)

    def get_list(self):
        """ Gets Platforms record in list format """
        __list = [ self.Pla_Id, self.Pla_Name, self.Pla_Host, self.Pla_Port, self.Pla_User, self.Pla_Password]
        return __list

    def get_tuple(self):
        """ Gets Platforms record in tuple format """
        __tuple = ( self.Pla_Id, self.Pla_Name, self.Pla_Host, self.Pla_Port, self.Pla_User, self.Pla_Password)
        return __tuple

    def get_dict(self):
        """ Gets Platforms record in dict format """
        __dict={'Pla_Id':self.Pla_Id,'Pla_Name':self.Pla_Name,'Pla_Host':self.Pla_Host,'Pla_Port':self.Pla_Port,'Pla_User':self.Pla_User,'Pla_Password':self.Pla_Password}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Platforms record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Platforms record column full details list """
        __list=[{'field': 'Pla_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'Id', 'is_time': False}, {'field': 'Pla_Name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'NO', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Name', 'is_time': False}, {'field': 'Pla_Host', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Host', 'is_time': False}, {'field': 'Pla_Port', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Port', 'is_time': False}, {'field': 'Pla_User', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'User', 'is_time': False}, {'field': 'Pla_Password', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Password', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Platforms record column headers list """
        __list=['Pla_Id', 'Pla_Name', 'Pla_Host', 'Pla_Port', 'Pla_User', 'Pla_Password']

        return __list

    def get_column_types(self):
        """ Gets Platforms record column data types list """
        __list=['Integer', 'String(255)', 'String(45)', 'String(45)', 'String(45)', 'String(45)']

        return __list

    def get_column_meta(self):
        """ Gets Platforms record column data meta list """
        __list=[('Pla_Id', 'Integer'), ('Pla_Name', 'String(255)'), ('Pla_Host', 'String(45)'), ('Pla_Port', 'String(45)'), ('Pla_User', 'String(45)'), ('Pla_Password', 'String(45)')]

        return __list

    def search_key(self,Pla_Id):
        """ Search for an unique Platforms record using all key fields (Pla_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Platforms).filter(Platforms.Pla_Id==Pla_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Platforms.search_key(%s): Exception: %s'%(Pla_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Platforms.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Platforms log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_rat_periods.py
import sqlalchemy
class Rat_Periods(Base):
    __tablename__ = 'Rat_Periods'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Rat_Periods_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Rat_Period = Column( Integer, primary_key=True )
    Value      = Column( String(45) )
    
    def __init__(self, Rat_Period=None, Value='None',engine=None,logger=None):
        """ Initiates a Rat_Periods class record """
        self.engine=engine
        self.logger=logger
        self.Rat_Period = Rat_Period
        self.Value      = Value

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Rat_Periods representation function """
        return "<Rat_Periods( Rat_Period='%s', Value='%s')>" % \
                ( self.Rat_Period, self.Value)

    def get_list(self):
        """ Gets Rat_Periods record in list format """
        __list = [ self.Rat_Period, self.Value]
        return __list

    def get_tuple(self):
        """ Gets Rat_Periods record in tuple format """
        __tuple = ( self.Rat_Period, self.Value)
        return __tuple

    def get_dict(self):
        """ Gets Rat_Periods record in dict format """
        __dict={'Rat_Period':self.Rat_Period,'Value':self.Value}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Rat_Periods record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Rat_Periods record column full details list """
        __list=[{'field': 'Rat_Period', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Rate Period', 'is_time': False}, {'field': 'Value', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Value', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Rat_Periods record column headers list """
        __list=['Rat_Period', 'Value']

        return __list

    def get_column_types(self):
        """ Gets Rat_Periods record column data types list """
        __list=['Integer', 'String(45)']

        return __list

    def get_column_meta(self):
        """ Gets Rat_Periods record column data meta list """
        __list=[('Rat_Period', 'Integer'), ('Value', 'String(45)')]

        return __list

    def search_key(self,Rat_Period):
        """ Search for an unique Rat_Periods record using all key fields (Rat_Period) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Rat_Periods).filter(Rat_Periods.Rat_Period==Rat_Period).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Rat_Periods.search_key(%s): Exception: %s'%(Rat_Period,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Rat_Periods.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Rat_Periods log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_rates.py
import sqlalchemy
class Rates(Base):
    __tablename__ = 'Rates'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Rates_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Rat_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Typ_Code   = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    Cus_Id     = Column( Integer, ForeignKey('Customers.Cus_Id') )
    Pla_Id     = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id      = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    CI_Id      = Column( Integer, ForeignKey('Configuration_Items.CI_Id') )
    Rat_Price  = Column( Numeric(20,12) )
    Cur_Code   = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    MU_Code    = Column( String(3), ForeignKey('Measure_Units.MU_Code') )
    Rat_Period = Column( Integer, ForeignKey('Rat_Periods.Rat_Period') )
    Rat_Type   = Column( Integer )
    # @property
    #
    
    
    def __init__(self, Rat_Id=0, Typ_Code='None', Cus_Id=None, Pla_Id=None, CC_Id=None, CI_Id=None, Rat_Price=None, Cur_Code='None', MU_Code='None', Rat_Period=None, Rat_Type=None,engine=None,logger=None):
        """ Initiates a Rates class record """
        self.engine=engine
        self.logger=logger
        self.Rat_Id     = Rat_Id
        self.Typ_Code   = Typ_Code
        self.Cus_Id     = Cus_Id
        self.Pla_Id     = Pla_Id
        self.CC_Id      = CC_Id
        self.CI_Id      = CI_Id
        self.Rat_Price  = Rat_Price
        self.Cur_Code   = Cur_Code
        self.MU_Code    = MU_Code
        self.Rat_Period = Rat_Period
        self.Rat_Type   = Rat_Type

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Rates representation function """
        return "<Rates( Rat_Id='%s', Typ_Code='%s', Cus_Id='%s', Pla_Id='%s', CC_Id='%s', CI_Id='%s', Rat_Price='%s', Cur_Code='%s', MU_Code='%s', Rat_Period='%s', Rat_Type='%s')>" % \
                ( self.Rat_Id, self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CI_Id, self.Rat_Price, self.Cur_Code, self.MU_Code, self.Rat_Period, self.Rat_Type)

    def get_list(self):
        """ Gets Rates record in list format """
        __list = [ self.Rat_Id, self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CI_Id, self.Rat_Price, self.Cur_Code, self.MU_Code, self.Rat_Period, self.Rat_Type]
        return __list

    def get_tuple(self):
        """ Gets Rates record in tuple format """
        __tuple = ( self.Rat_Id, self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CI_Id, self.Rat_Price, self.Cur_Code, self.MU_Code, self.Rat_Period, self.Rat_Type)
        return __tuple

    def get_dict(self):
        """ Gets Rates record in dict format """
        __dict={'Rat_Id':self.Rat_Id,'Typ_Code':self.Typ_Code,'Cus_Id':self.Cus_Id,'Pla_Id':self.Pla_Id,'CC_Id':self.CC_Id,'CI_Id':self.CI_Id,'Rat_Price':self.Rat_Price,'Cur_Code':self.Cur_Code,'MU_Code':self.MU_Code,'Rat_Period':self.Rat_Period,'Rat_Type':self.Rat_Type}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Rates record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Rates record column full details list """
        __list=[{'field': 'Rat_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'Id', 'is_time': False}, {'field': 'Typ_Code', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Typ_Code', 'referenced_table': 'CU_Types', 'referenced_class': 'cu_type', 'foreign_key': 'Typ_Code', 'foreign_value': 'Typ_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Charge Unit Type', 'is_time': False}, {'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Cus_Id', 'referenced_table': 'Customers', 'referenced_class': 'customer', 'foreign_key': 'Cus_Id', 'foreign_value': 'Cus_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Customer Id', 'is_time': False}, {'field': 'Pla_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Pla_Id', 'referenced_table': 'Platforms', 'referenced_class': 'platform', 'foreign_key': 'Pla_Id', 'foreign_value': 'Pla_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Platform Id', 'is_time': False}, {'field': 'CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CC_Id', 'referenced_table': 'Cost_Centers', 'referenced_class': 'cost_center', 'foreign_key': 'CC_Id', 'foreign_value': 'CC_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Cost Center Id', 'is_time': False}, {'field': 'CI_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CI_Id', 'referenced_table': 'Configuration_Items', 'referenced_class': 'configuration_item', 'foreign_key': 'CI_Id', 'foreign_value': 'CI_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Configuration Item', 'is_time': False}, {'field': 'Rat_Price', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Rate Price', 'is_time': False}, {'field': 'Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Cur_Code', 'referenced_table': 'Currencies', 'referenced_class': 'currency', 'foreign_key': 'Cur_Code', 'foreign_value': 'Cur_Name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Currency Code', 'is_time': False}, {'field': 'MU_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'MU_Code', 'referenced_table': 'Measure_Units', 'referenced_class': 'measure_unit', 'foreign_key': 'MU_Code', 'foreign_value': 'MU_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'Measure Unit', 'is_time': False}, {'field': 'Rat_Period', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'Rat_Period', 'referenced_table': 'Rat_Periods', 'referenced_class': 'rat_period', 'foreign_key': 'Rat_Period', 'foreign_value': 'Value', 'is_numeric': False, 'form_type': 'RadioField', 'is_id': False, 'header': 'Period', 'is_time': False}, {'field': 'Rat_Type', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': False, 'format': None, 'order': 11, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Rate Type', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Rates record column headers list """
        __list=['Rat_Id', 'Typ_Code', 'Cus_Id', 'Pla_Id', 'CC_Id', 'CI_Id', 'Rat_Price', 'Cur_Code', 'MU_Code', 'Rat_Period', 'Rat_Type']

        return __list

    def get_column_types(self):
        """ Gets Rates record column data types list """
        __list=['Integer', 'String(10)', 'Integer', 'Integer', 'Integer', 'Integer', 'Numeric(20,12)', 'String(3)', 'String(3)', 'Integer', 'Integer']

        return __list

    def get_column_meta(self):
        """ Gets Rates record column data meta list """
        __list=[('Rat_Id', 'Integer'), ('Typ_Code', 'String(10)'), ('Cus_Id', 'Integer'), ('Pla_Id', 'Integer'), ('CC_Id', 'Integer'), ('CI_Id', 'Integer'), ('Rat_Price', 'Numeric(20,12)'), ('Cur_Code', 'String(3)'), ('MU_Code', 'String(3)'), ('Rat_Period', 'Integer'), ('Rat_Type', 'Integer')]

        return __list

    def search_key(self,Rat_Id):
        """ Search for an unique Rates record using all key fields (Rat_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Rates).filter(Rates.Rat_Id==Rat_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Rates.search_key(%s): Exception: %s'%(Rat_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Rates.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Rates log function """
        if self.logger is not None:
            self.logger.log(level,message)
    # method
    def method(self):
        pass

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_roles.py
import sqlalchemy
class Roles(Base):
    __tablename__ = 'Roles'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Roles_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    id          = Column( Integer, primary_key=True )
    name        = Column( String(64) )
    default     = Column( Boolean )
    permissions = Column( Integer )
    
    def __init__(self, id=None, name='None', default=None, permissions=None,engine=None,logger=None):
        """ Initiates a Roles class record """
        self.engine=engine
        self.logger=logger
        self.id          = id
        self.name        = name
        self.default     = default
        self.permissions = permissions

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Roles representation function """
        return "<Roles( id='%s', name='%s', default='%s', permissions='%s')>" % \
                ( self.id, self.name, self.default, self.permissions)

    def get_list(self):
        """ Gets Roles record in list format """
        __list = [ self.id, self.name, self.default, self.permissions]
        return __list

    def get_tuple(self):
        """ Gets Roles record in tuple format """
        __tuple = ( self.id, self.name, self.default, self.permissions)
        return __tuple

    def get_dict(self):
        """ Gets Roles record in dict format """
        __dict={'id':self.id,'name':self.name,'default':self.default,'permissions':self.permissions}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Roles record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Roles record column full details list """
        __list=[{'field': 'id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'id', 'is_time': False}, {'field': 'name', 'type': 'varchar(64)', 'type_flask': 'db.String(64)', 'type_sqlalchemy': 'String(64)', 'null': 'YES', 'key': 'UNI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'name', 'is_time': False}, {'field': 'default', 'type': 'tinyint', 'type_flask': 'db.Boolean', 'type_sqlalchemy': 'Boolean', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'BooleanField', 'is_id': False, 'header': 'default', 'is_time': False}, {'field': 'permissions', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'permissions', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Roles record column headers list """
        __list=['id', 'name', 'default', 'permissions']

        return __list

    def get_column_types(self):
        """ Gets Roles record column data types list """
        __list=['Integer', 'String(64)', 'Boolean', 'Integer']

        return __list

    def get_column_meta(self):
        """ Gets Roles record column data meta list """
        __list=[('id', 'Integer'), ('name', 'String(64)'), ('default', 'Boolean'), ('permissions', 'Integer')]

        return __list

    def search_key(self,id):
        """ Search for an unique Roles record using all key fields (id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Roles).filter(Roles.id==id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Roles.search_key(%s): Exception: %s'%(id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Roles.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Roles log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_st_use_per_cu.py
import sqlalchemy
class ST_Use_Per_CU(Base):
    __tablename__ = 'ST_Use_Per_CU'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='ST_Use_Per_CU_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Id                  = Column( Integer, primary_key=True )
    From                   = Column( DateTime, primary_key=True )
    To                     = Column( DateTime, primary_key=True )
    Total_Slices           = Column( Integer )
    Found_Slices           = Column( Integer )
    Not_Found_Slices       = Column( Integer )
    Period_Initial_Q       = Column( Numeric(20,12) )
    Period_Increase        = Column( Numeric(20,12) )
    Period_Increase_Count  = Column( Integer )
    Period_Reduction       = Column( Numeric(20,12) )
    Period_Reduction_Count = Column( Integer )
    Period_Final_Q         = Column( Numeric(20,12) )
    CI_Id                  = Column( Integer )
    CC_Id                  = Column( Integer )
    Cus_Id                 = Column( Integer )
    Rat_Id                 = Column( Integer )
    Typ_Code               = Column( String(10) )
    Pla_Id                 = Column( Integer )
    Mean                   = Column( Numeric(20,12) )
    Variance               = Column( Numeric(20,12) )
    StdDev                 = Column( Numeric(20,12) )
    Min                    = Column( Numeric(20,12) )
    Max                    = Column( Numeric(20,12) )
    
    def __init__(self, CU_Id=None, From=None, To=None, Total_Slices=0, Found_Slices=0, Not_Found_Slices=0, Period_Initial_Q=0.000000000000, Period_Increase=0.000000000000, Period_Increase_Count=0, Period_Reduction=0.000000000000, Period_Reduction_Count=0, Period_Final_Q=0.000000000000, CI_Id=1, CC_Id=1, Cus_Id=1, Rat_Id=1, Typ_Code='NUL', Pla_Id=1, Mean=0.000000000000, Variance=0.000000000000, StdDev=0.000000000000, Min=0.000000000000, Max=0.000000000000,engine=None,logger=None):
        """ Initiates a ST_Use_Per_CU class record """
        self.engine=engine
        self.logger=logger
        self.CU_Id                  = CU_Id
        self.From                   = From
        self.To                     = To
        self.Total_Slices           = Total_Slices
        self.Found_Slices           = Found_Slices
        self.Not_Found_Slices       = Not_Found_Slices
        self.Period_Initial_Q       = Period_Initial_Q
        self.Period_Increase        = Period_Increase
        self.Period_Increase_Count  = Period_Increase_Count
        self.Period_Reduction       = Period_Reduction
        self.Period_Reduction_Count = Period_Reduction_Count
        self.Period_Final_Q         = Period_Final_Q
        self.CI_Id                  = CI_Id
        self.CC_Id                  = CC_Id
        self.Cus_Id                 = Cus_Id
        self.Rat_Id                 = Rat_Id
        self.Typ_Code               = Typ_Code
        self.Pla_Id                 = Pla_Id
        self.Mean                   = Mean
        self.Variance               = Variance
        self.StdDev                 = StdDev
        self.Min                    = Min
        self.Max                    = Max

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class ST_Use_Per_CU representation function """
        return "<ST_Use_Per_CU( CU_Id='%s', From='%s', To='%s', Total_Slices='%s', Found_Slices='%s', Not_Found_Slices='%s', Period_Initial_Q='%s', Period_Increase='%s', Period_Increase_Count='%s', Period_Reduction='%s', Period_Reduction_Count='%s', Period_Final_Q='%s', CI_Id='%s', CC_Id='%s', Cus_Id='%s', Rat_Id='%s', Typ_Code='%s', Pla_Id='%s', Mean='%s', Variance='%s', StdDev='%s', Min='%s', Max='%s')>" % \
                ( self.CU_Id, self.From, self.To, self.Total_Slices, self.Found_Slices, self.Not_Found_Slices, self.Period_Initial_Q, self.Period_Increase, self.Period_Increase_Count, self.Period_Reduction, self.Period_Reduction_Count, self.Period_Final_Q, self.CI_Id, self.CC_Id, self.Cus_Id, self.Rat_Id, self.Typ_Code, self.Pla_Id, self.Mean, self.Variance, self.StdDev, self.Min, self.Max)

    def get_list(self):
        """ Gets ST_Use_Per_CU record in list format """
        __list = [ self.CU_Id, self.From, self.To, self.Total_Slices, self.Found_Slices, self.Not_Found_Slices, self.Period_Initial_Q, self.Period_Increase, self.Period_Increase_Count, self.Period_Reduction, self.Period_Reduction_Count, self.Period_Final_Q, self.CI_Id, self.CC_Id, self.Cus_Id, self.Rat_Id, self.Typ_Code, self.Pla_Id, self.Mean, self.Variance, self.StdDev, self.Min, self.Max]
        return __list

    def get_tuple(self):
        """ Gets ST_Use_Per_CU record in tuple format """
        __tuple = ( self.CU_Id, self.From, self.To, self.Total_Slices, self.Found_Slices, self.Not_Found_Slices, self.Period_Initial_Q, self.Period_Increase, self.Period_Increase_Count, self.Period_Reduction, self.Period_Reduction_Count, self.Period_Final_Q, self.CI_Id, self.CC_Id, self.Cus_Id, self.Rat_Id, self.Typ_Code, self.Pla_Id, self.Mean, self.Variance, self.StdDev, self.Min, self.Max)
        return __tuple

    def get_dict(self):
        """ Gets ST_Use_Per_CU record in dict format """
        __dict={'CU_Id':self.CU_Id,'From':self.From,'To':self.To,'Total_Slices':self.Total_Slices,'Found_Slices':self.Found_Slices,'Not_Found_Slices':self.Not_Found_Slices,'Period_Initial_Q':self.Period_Initial_Q,'Period_Increase':self.Period_Increase,'Period_Increase_Count':self.Period_Increase_Count,'Period_Reduction':self.Period_Reduction,'Period_Reduction_Count':self.Period_Reduction_Count,'Period_Final_Q':self.Period_Final_Q,'CI_Id':self.CI_Id,'CC_Id':self.CC_Id,'Cus_Id':self.Cus_Id,'Rat_Id':self.Rat_Id,'Typ_Code':self.Typ_Code,'Pla_Id':self.Pla_Id,'Mean':self.Mean,'Variance':self.Variance,'StdDev':self.StdDev,'Min':self.Min,'Max':self.Max}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets ST_Use_Per_CU record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets ST_Use_Per_CU record column full details list """
        __list=[{'field': 'CU_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CU_Id', 'is_time': False}, {'field': 'From', 'type': 'timestamp', 'type_flask': 'db.DateTime', 'type_sqlalchemy': 'DateTime', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateTimeField', 'is_id': False, 'header': 'From', 'is_time': False}, {'field': 'To', 'type': 'timestamp', 'type_flask': 'db.DateTime', 'type_sqlalchemy': 'DateTime', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateTimeField', 'is_id': False, 'header': 'To', 'is_time': False}, {'field': 'Total_Slices', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Total_Slices', 'is_time': False}, {'field': 'Found_Slices', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Found_Slices', 'is_time': False}, {'field': 'Not_Found_Slices', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Not_Found_Slices', 'is_time': False}, {'field': 'Period_Initial_Q', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Period_Initial_Q', 'is_time': False}, {'field': 'Period_Increase', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Period_Increase', 'is_time': False}, {'field': 'Period_Increase_Count', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Period_Increase_Count', 'is_time': False}, {'field': 'Period_Reduction', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Period_Reduction', 'is_time': False}, {'field': 'Period_Reduction_Count', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 11, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Period_Reduction_Count', 'is_time': False}, {'field': 'Period_Final_Q', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 12, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Period_Final_Q', 'is_time': False}, {'field': 'CI_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 13, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CI_Id', 'is_time': False}, {'field': 'CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 14, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CC_Id', 'is_time': False}, {'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 15, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Cus_Id', 'is_time': False}, {'field': 'Rat_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 16, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Rat_id', 'is_time': False}, {'field': 'Typ_Code', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'YES', 'key': '', 'default': 'NUL', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 17, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Typ_Code', 'is_time': False}, {'field': 'Pla_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 18, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Pla_Id', 'is_time': False}, {'field': 'Mean', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 19, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Mean', 'is_time': False}, {'field': 'Variance', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 20, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Variance', 'is_time': False}, {'field': 'StdDev', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 21, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'StdDev', 'is_time': False}, {'field': 'Min', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 22, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Min', 'is_time': False}, {'field': 'Max', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 23, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Max', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets ST_Use_Per_CU record column headers list """
        __list=['CU_Id', 'From', 'To', 'Total_Slices', 'Found_Slices', 'Not_Found_Slices', 'Period_Initial_Q', 'Period_Increase', 'Period_Increase_Count', 'Period_Reduction', 'Period_Reduction_Count', 'Period_Final_Q', 'CI_Id', 'CC_Id', 'Cus_Id', 'Rat_Id', 'Typ_Code', 'Pla_Id', 'Mean', 'Variance', 'StdDev', 'Min', 'Max']

        return __list

    def get_column_types(self):
        """ Gets ST_Use_Per_CU record column data types list """
        __list=['Integer', 'DateTime', 'DateTime', 'Integer', 'Integer', 'Integer', 'Numeric(20,12)', 'Numeric(20,12)', 'Integer', 'Numeric(20,12)', 'Integer', 'Numeric(20,12)', 'Integer', 'Integer', 'Integer', 'Integer', 'String(10)', 'Integer', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)']

        return __list

    def get_column_meta(self):
        """ Gets ST_Use_Per_CU record column data meta list """
        __list=[('CU_Id', 'Integer'), ('From', 'DateTime'), ('To', 'DateTime'), ('Total_Slices', 'Integer'), ('Found_Slices', 'Integer'), ('Not_Found_Slices', 'Integer'), ('Period_Initial_Q', 'Numeric(20,12)'), ('Period_Increase', 'Numeric(20,12)'), ('Period_Increase_Count', 'Integer'), ('Period_Reduction', 'Numeric(20,12)'), ('Period_Reduction_Count', 'Integer'), ('Period_Final_Q', 'Numeric(20,12)'), ('CI_Id', 'Integer'), ('CC_Id', 'Integer'), ('Cus_Id', 'Integer'), ('Rat_Id', 'Integer'), ('Typ_Code', 'String(10)'), ('Pla_Id', 'Integer'), ('Mean', 'Numeric(20,12)'), ('Variance', 'Numeric(20,12)'), ('StdDev', 'Numeric(20,12)'), ('Min', 'Numeric(20,12)'), ('Max', 'Numeric(20,12)')]

        return __list

    def search_key(self,CU_Id,From,To):
        """ Search for an unique ST_Use_Per_CU record using all key fields (CU_Id,From,To) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(ST_Use_Per_CU).filter(ST_Use_Per_CU.CU_Id==CU_Id).filter(ST_Use_Per_CU.From==From).filter(ST_Use_Per_CU.To==To).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='ST_Use_Per_CU.search_key(%s,%s,%s): Exception: %s'%(CU_Id,From,To,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='ST_Use_Per_CU.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class ST_Use_Per_CU log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_st_use_per_type.py
import sqlalchemy
class ST_Use_Per_Type(Base):
    __tablename__ = 'ST_Use_Per_Type'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='ST_Use_Per_Type_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Typ_Code = Column( String(10), primary_key=True )
    Cus_Id   = Column( Integer, primary_key=True )
    Pla_Id   = Column( Integer, primary_key=True )
    CC_Id    = Column( Integer, primary_key=True )
    CI_Id    = Column( Integer, primary_key=True )
    Year     = Column( Integer, primary_key=True )
    Month    = Column( Integer, primary_key=True )
    Count    = Column( Integer )
    Mean     = Column( Numeric(20,12) )
    Variance = Column( Numeric(20,12) )
    StdDev   = Column( Numeric(20,12) )
    Min      = Column( Numeric(20,12) )
    Max      = Column( Numeric(20,12) )
    
    def __init__(self, Typ_Code='None', Cus_Id=1, Pla_Id=1, CC_Id=1, CI_Id=1, Year=None, Month=None, Count=0, Mean=None, Variance=None, StdDev=None, Min=None, Max=None,engine=None,logger=None):
        """ Initiates a ST_Use_Per_Type class record """
        self.engine=engine
        self.logger=logger
        self.Typ_Code = Typ_Code
        self.Cus_Id   = Cus_Id
        self.Pla_Id   = Pla_Id
        self.CC_Id    = CC_Id
        self.CI_Id    = CI_Id
        self.Year     = Year
        self.Month    = Month
        self.Count    = Count
        self.Mean     = Mean
        self.Variance = Variance
        self.StdDev   = StdDev
        self.Min      = Min
        self.Max      = Max

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class ST_Use_Per_Type representation function """
        return "<ST_Use_Per_Type( Typ_Code='%s', Cus_Id='%s', Pla_Id='%s', CC_Id='%s', CI_Id='%s', Year='%s', Month='%s', Count='%s', Mean='%s', Variance='%s', StdDev='%s', Min='%s', Max='%s')>" % \
                ( self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CI_Id, self.Year, self.Month, self.Count, self.Mean, self.Variance, self.StdDev, self.Min, self.Max)

    def get_list(self):
        """ Gets ST_Use_Per_Type record in list format """
        __list = [ self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CI_Id, self.Year, self.Month, self.Count, self.Mean, self.Variance, self.StdDev, self.Min, self.Max]
        return __list

    def get_tuple(self):
        """ Gets ST_Use_Per_Type record in tuple format """
        __tuple = ( self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CI_Id, self.Year, self.Month, self.Count, self.Mean, self.Variance, self.StdDev, self.Min, self.Max)
        return __tuple

    def get_dict(self):
        """ Gets ST_Use_Per_Type record in dict format """
        __dict={'Typ_Code':self.Typ_Code,'Cus_Id':self.Cus_Id,'Pla_Id':self.Pla_Id,'CC_Id':self.CC_Id,'CI_Id':self.CI_Id,'Year':self.Year,'Month':self.Month,'Count':self.Count,'Mean':self.Mean,'Variance':self.Variance,'StdDev':self.StdDev,'Min':self.Min,'Max':self.Max}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets ST_Use_Per_Type record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets ST_Use_Per_Type record column full details list """
        __list=[{'field': 'Typ_Code', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Typ_Code', 'is_time': False}, {'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Cus_Id', 'is_time': False}, {'field': 'Pla_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Pla_Id', 'is_time': False}, {'field': 'CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CC_Id', 'is_time': False}, {'field': 'CI_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CI_Id', 'is_time': False}, {'field': 'Year', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Year', 'is_time': False}, {'field': 'Month', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Month', 'is_time': False}, {'field': 'Count', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Count', 'is_time': False}, {'field': 'Mean', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Mean', 'is_time': False}, {'field': 'Variance', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Variance', 'is_time': False}, {'field': 'StdDev', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 11, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'StdDev', 'is_time': False}, {'field': 'Min', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 12, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Min', 'is_time': False}, {'field': 'Max', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 13, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Max', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets ST_Use_Per_Type record column headers list """
        __list=['Typ_Code', 'Cus_Id', 'Pla_Id', 'CC_Id', 'CI_Id', 'Year', 'Month', 'Count', 'Mean', 'Variance', 'StdDev', 'Min', 'Max']

        return __list

    def get_column_types(self):
        """ Gets ST_Use_Per_Type record column data types list """
        __list=['String(10)', 'Integer', 'Integer', 'Integer', 'Integer', 'Integer', 'Integer', 'Integer', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)']

        return __list

    def get_column_meta(self):
        """ Gets ST_Use_Per_Type record column data meta list """
        __list=[('Typ_Code', 'String(10)'), ('Cus_Id', 'Integer'), ('Pla_Id', 'Integer'), ('CC_Id', 'Integer'), ('CI_Id', 'Integer'), ('Year', 'Integer'), ('Month', 'Integer'), ('Count', 'Integer'), ('Mean', 'Numeric(20,12)'), ('Variance', 'Numeric(20,12)'), ('StdDev', 'Numeric(20,12)'), ('Min', 'Numeric(20,12)'), ('Max', 'Numeric(20,12)')]

        return __list

    def search_key(self,Typ_Code,Cus_Id,Pla_Id,CC_Id,CI_Id,Year,Month):
        """ Search for an unique ST_Use_Per_Type record using all key fields (Typ_Code,Cus_Id,Pla_Id,CC_Id,CI_Id,Year,Month) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(ST_Use_Per_Type).filter(ST_Use_Per_Type.Typ_Code==Typ_Code).filter(ST_Use_Per_Type.Cus_Id==Cus_Id).filter(ST_Use_Per_Type.Pla_Id==Pla_Id).filter(ST_Use_Per_Type.CC_Id==CC_Id).filter(ST_Use_Per_Type.CI_Id==CI_Id).filter(ST_Use_Per_Type.Year==Year).filter(ST_Use_Per_Type.Month==Month).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='ST_Use_Per_Type.search_key(%s,%s,%s,%s,%s,%s,%s): Exception: %s'%(Typ_Code,Cus_Id,Pla_Id,CC_Id,CI_Id,Year,Month,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='ST_Use_Per_Type.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class ST_Use_Per_Type log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_statistics.py
import sqlalchemy
class Statistics(Base):
    __tablename__ = 'Statistics'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Statistics_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CR_Date_From        = Column( Date, primary_key=True )
    CR_Date_To          = Column( Date, primary_key=True )
    User_Id             = Column( Integer, primary_key=True )
    Cus_Id              = Column( Integer, primary_key=True )
    CC_Id               = Column( Integer, primary_key=True )
    CI_Id               = Column( Integer, primary_key=True )
    CU_Id               = Column( Integer, primary_key=True )
    Typ_Code            = Column( String(10), primary_key=True )
    Period              = Column( String(45), primary_key=True )
    Agregation          = Column( Integer, primary_key=True )
    CR_Quantity_at_Rate = Column( Numeric(24,12) )
    CR_Quantity         = Column( Numeric(24,12) )
    CR_ST_at_Cur        = Column( Numeric(20,12) )
    Cur_Code            = Column( String(3) )
    CIT_Status          = Column( Integer )
    CIT_Count           = Column( Integer )
    Pla_Id              = Column( Integer )
    
    def __init__(self, CR_Date_From=None, CR_Date_To=None, User_Id=None, Cus_Id=0, CC_Id=0, CI_Id=1, CU_Id=0, Typ_Code='NUL', Period='None', Agregation=0, CR_Quantity_at_Rate=0.000000000000, CR_Quantity=0.000000000000, CR_ST_at_Cur=0.000000000000, Cur_Code='None', CIT_Status=None, CIT_Count=0, Pla_Id=0,engine=None,logger=None):
        """ Initiates a Statistics class record """
        self.engine=engine
        self.logger=logger
        self.CR_Date_From        = CR_Date_From
        self.CR_Date_To          = CR_Date_To
        self.User_Id             = User_Id
        self.Cus_Id              = Cus_Id
        self.CC_Id               = CC_Id
        self.CI_Id               = CI_Id
        self.CU_Id               = CU_Id
        self.Typ_Code            = Typ_Code
        self.Period              = Period
        self.Agregation          = Agregation
        self.CR_Quantity_at_Rate = CR_Quantity_at_Rate
        self.CR_Quantity         = CR_Quantity
        self.CR_ST_at_Cur        = CR_ST_at_Cur
        self.Cur_Code            = Cur_Code
        self.CIT_Status          = CIT_Status
        self.CIT_Count           = CIT_Count
        self.Pla_Id              = Pla_Id

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Statistics representation function """
        return "<Statistics( CR_Date_From='%s', CR_Date_To='%s', User_Id='%s', Cus_Id='%s', CC_Id='%s', CI_Id='%s', CU_Id='%s', Typ_Code='%s', Period='%s', Agregation='%s', CR_Quantity_at_Rate='%s', CR_Quantity='%s', CR_ST_at_Cur='%s', Cur_Code='%s', CIT_Status='%s', CIT_Count='%s', Pla_Id='%s')>" % \
                ( self.CR_Date_From, self.CR_Date_To, self.User_Id, self.Cus_Id, self.CC_Id, self.CI_Id, self.CU_Id, self.Typ_Code, self.Period, self.Agregation, self.CR_Quantity_at_Rate, self.CR_Quantity, self.CR_ST_at_Cur, self.Cur_Code, self.CIT_Status, self.CIT_Count, self.Pla_Id)

    def get_list(self):
        """ Gets Statistics record in list format """
        __list = [ self.CR_Date_From, self.CR_Date_To, self.User_Id, self.Cus_Id, self.CC_Id, self.CI_Id, self.CU_Id, self.Typ_Code, self.Period, self.Agregation, self.CR_Quantity_at_Rate, self.CR_Quantity, self.CR_ST_at_Cur, self.Cur_Code, self.CIT_Status, self.CIT_Count, self.Pla_Id]
        return __list

    def get_tuple(self):
        """ Gets Statistics record in tuple format """
        __tuple = ( self.CR_Date_From, self.CR_Date_To, self.User_Id, self.Cus_Id, self.CC_Id, self.CI_Id, self.CU_Id, self.Typ_Code, self.Period, self.Agregation, self.CR_Quantity_at_Rate, self.CR_Quantity, self.CR_ST_at_Cur, self.Cur_Code, self.CIT_Status, self.CIT_Count, self.Pla_Id)
        return __tuple

    def get_dict(self):
        """ Gets Statistics record in dict format """
        __dict={'CR_Date_From':self.CR_Date_From,'CR_Date_To':self.CR_Date_To,'User_Id':self.User_Id,'Cus_Id':self.Cus_Id,'CC_Id':self.CC_Id,'CI_Id':self.CI_Id,'CU_Id':self.CU_Id,'Typ_Code':self.Typ_Code,'Period':self.Period,'Agregation':self.Agregation,'CR_Quantity_at_Rate':self.CR_Quantity_at_Rate,'CR_Quantity':self.CR_Quantity,'CR_ST_at_Cur':self.CR_ST_at_Cur,'Cur_Code':self.Cur_Code,'CIT_Status':self.CIT_Status,'CIT_Count':self.CIT_Count,'Pla_Id':self.Pla_Id}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Statistics record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Statistics record column full details list """
        __list=[{'field': 'CR_Date_From', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'CR_Date_From', 'is_time': False}, {'field': 'CR_Date_To', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'CR_Date_To', 'is_time': False}, {'field': 'User_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'User_Id', 'is_time': False}, {'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Cus_Id', 'is_time': False}, {'field': 'CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CC_Id', 'is_time': False}, {'field': 'CI_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CI_Id', 'is_time': False}, {'field': 'CU_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CU_Id', 'is_time': False}, {'field': 'Typ_Code', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'NO', 'key': 'PRI', 'default': 'NUL', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Typ_Code', 'is_time': False}, {'field': 'Period', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Period', 'is_time': False}, {'field': 'Agregation', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Agregation', 'is_time': False}, {'field': 'CR_Quantity_at_Rate', 'type': 'decimal(24,12)', 'type_flask': 'db.Numeric(24,12)', 'type_sqlalchemy': 'Numeric(24,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 11, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Quantity_at_Rate', 'is_time': False}, {'field': 'CR_Quantity', 'type': 'decimal(24,12)', 'type_flask': 'db.Numeric(24,12)', 'type_sqlalchemy': 'Numeric(24,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 12, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Quantity', 'is_time': False}, {'field': 'CR_ST_at_Cur', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 13, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_ST_at_Cur', 'is_time': False}, {'field': 'Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 14, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Cur_Code', 'is_time': False}, {'field': 'CIT_Status', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 15, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Status', 'is_time': False}, {'field': 'CIT_Count', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 16, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Count', 'is_time': False}, {'field': 'Pla_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 17, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Pla_Id', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Statistics record column headers list """
        __list=['CR_Date_From', 'CR_Date_To', 'User_Id', 'Cus_Id', 'CC_Id', 'CI_Id', 'CU_Id', 'Typ_Code', 'Period', 'Agregation', 'CR_Quantity_at_Rate', 'CR_Quantity', 'CR_ST_at_Cur', 'Cur_Code', 'CIT_Status', 'CIT_Count', 'Pla_Id']

        return __list

    def get_column_types(self):
        """ Gets Statistics record column data types list """
        __list=['Date', 'Date', 'Integer', 'Integer', 'Integer', 'Integer', 'Integer', 'String(10)', 'String(45)', 'Integer', 'Numeric(24,12)', 'Numeric(24,12)', 'Numeric(20,12)', 'String(3)', 'Integer', 'Integer', 'Integer']

        return __list

    def get_column_meta(self):
        """ Gets Statistics record column data meta list """
        __list=[('CR_Date_From', 'Date'), ('CR_Date_To', 'Date'), ('User_Id', 'Integer'), ('Cus_Id', 'Integer'), ('CC_Id', 'Integer'), ('CI_Id', 'Integer'), ('CU_Id', 'Integer'), ('Typ_Code', 'String(10)'), ('Period', 'String(45)'), ('Agregation', 'Integer'), ('CR_Quantity_at_Rate', 'Numeric(24,12)'), ('CR_Quantity', 'Numeric(24,12)'), ('CR_ST_at_Cur', 'Numeric(20,12)'), ('Cur_Code', 'String(3)'), ('CIT_Status', 'Integer'), ('CIT_Count', 'Integer'), ('Pla_Id', 'Integer')]

        return __list

    def search_key(self,CR_Date_From,CR_Date_To,User_Id,Cus_Id,CC_Id,CI_Id,CU_Id,Typ_Code,Period,Agregation):
        """ Search for an unique Statistics record using all key fields (CR_Date_From,CR_Date_To,User_Id,Cus_Id,CC_Id,CI_Id,CU_Id,Typ_Code,Period,Agregation) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Statistics).filter(Statistics.CR_Date_From==CR_Date_From).filter(Statistics.CR_Date_To==CR_Date_To).filter(Statistics.User_Id==User_Id).filter(Statistics.Cus_Id==Cus_Id).filter(Statistics.CC_Id==CC_Id).filter(Statistics.CI_Id==CI_Id).filter(Statistics.CU_Id==CU_Id).filter(Statistics.Typ_Code==Typ_Code).filter(Statistics.Period==Period).filter(Statistics.Agregation==Agregation).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Statistics.search_key(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s): Exception: %s'%(CR_Date_From,CR_Date_To,User_Id,Cus_Id,CC_Id,CI_Id,CU_Id,Typ_Code,Period,Agregation,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Statistics.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Statistics log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:865 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_statistics.py
# gen_model_flask.py:866 Table sharding code follows:
def get_Statistics(table_name_suffix):
  class Statistics_Class(Base):
    __tablename__ = 'Statistics_%s'%(table_name_suffix)
    engine        = None
    logger        = None

    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Statistics_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table_args__ = {'extend_existing':True}
           __class__.__table__.name = name
           __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CR_Date_From        = Column( Date, primary_key=True )
    CR_Date_To          = Column( Date, primary_key=True )
    User_Id             = Column( Integer, primary_key=True )
    Cus_Id              = Column( Integer, primary_key=True )
    CC_Id               = Column( Integer, primary_key=True )
    CI_Id               = Column( Integer, primary_key=True )
    CU_Id               = Column( Integer, primary_key=True )
    Typ_Code            = Column( String(10), primary_key=True )
    Period              = Column( String(45), primary_key=True )
    Agregation          = Column( Integer, primary_key=True )
    CR_Quantity_at_Rate = Column( Numeric(24,12) )
    CR_Quantity         = Column( Numeric(24,12) )
    CR_ST_at_Cur        = Column( Numeric(20,12) )
    Cur_Code            = Column( String(3) )
    CIT_Status          = Column( Integer )
    CIT_Count           = Column( Integer )
    Pla_Id              = Column( Integer )
    
    def __init__(self, CR_Date_From=None, CR_Date_To=None, User_Id=None, Cus_Id=0, CC_Id=0, CI_Id=1, CU_Id=0, Typ_Code='NUL', Period='None', Agregation=0, CR_Quantity_at_Rate=0.000000000000, CR_Quantity=0.000000000000, CR_ST_at_Cur=0.000000000000, Cur_Code='None', CIT_Status=None, CIT_Count=0, Pla_Id=0,engine=None,logger=None):
        """ Initiates a Statistics class record """
        self.engine=engine
        self.logger=logger
        self.CR_Date_From        = CR_Date_From
        self.CR_Date_To          = CR_Date_To
        self.User_Id             = User_Id
        self.Cus_Id              = Cus_Id
        self.CC_Id               = CC_Id
        self.CI_Id               = CI_Id
        self.CU_Id               = CU_Id
        self.Typ_Code            = Typ_Code
        self.Period              = Period
        self.Agregation          = Agregation
        self.CR_Quantity_at_Rate = CR_Quantity_at_Rate
        self.CR_Quantity         = CR_Quantity
        self.CR_ST_at_Cur        = CR_ST_at_Cur
        self.Cur_Code            = Cur_Code
        self.CIT_Status          = CIT_Status
        self.CIT_Count           = CIT_Count
        self.Pla_Id              = Pla_Id

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Statistics representation function """
        return "<Statistics( CR_Date_From='%s', CR_Date_To='%s', User_Id='%s', Cus_Id='%s', CC_Id='%s', CI_Id='%s', CU_Id='%s', Typ_Code='%s', Period='%s', Agregation='%s', CR_Quantity_at_Rate='%s', CR_Quantity='%s', CR_ST_at_Cur='%s', Cur_Code='%s', CIT_Status='%s', CIT_Count='%s', Pla_Id='%s')>" % \
                ( self.CR_Date_From, self.CR_Date_To, self.User_Id, self.Cus_Id, self.CC_Id, self.CI_Id, self.CU_Id, self.Typ_Code, self.Period, self.Agregation, self.CR_Quantity_at_Rate, self.CR_Quantity, self.CR_ST_at_Cur, self.Cur_Code, self.CIT_Status, self.CIT_Count, self.Pla_Id)

    def get_list(self):
        """ Gets Statistics record in list format """
        __list = [ self.CR_Date_From, self.CR_Date_To, self.User_Id, self.Cus_Id, self.CC_Id, self.CI_Id, self.CU_Id, self.Typ_Code, self.Period, self.Agregation, self.CR_Quantity_at_Rate, self.CR_Quantity, self.CR_ST_at_Cur, self.Cur_Code, self.CIT_Status, self.CIT_Count, self.Pla_Id]
        return __list

    def get_tuple(self):
        """ Gets Statistics record in tuple format """
        __tuple = ( self.CR_Date_From, self.CR_Date_To, self.User_Id, self.Cus_Id, self.CC_Id, self.CI_Id, self.CU_Id, self.Typ_Code, self.Period, self.Agregation, self.CR_Quantity_at_Rate, self.CR_Quantity, self.CR_ST_at_Cur, self.Cur_Code, self.CIT_Status, self.CIT_Count, self.Pla_Id)
        return __tuple

    def get_dict(self):
        """ Gets Statistics record in dict format """
        __dict={'CR_Date_From':self.CR_Date_From,'CR_Date_To':self.CR_Date_To,'User_Id':self.User_Id,'Cus_Id':self.Cus_Id,'CC_Id':self.CC_Id,'CI_Id':self.CI_Id,'CU_Id':self.CU_Id,'Typ_Code':self.Typ_Code,'Period':self.Period,'Agregation':self.Agregation,'CR_Quantity_at_Rate':self.CR_Quantity_at_Rate,'CR_Quantity':self.CR_Quantity,'CR_ST_at_Cur':self.CR_ST_at_Cur,'Cur_Code':self.Cur_Code,'CIT_Status':self.CIT_Status,'CIT_Count':self.CIT_Count,'Pla_Id':self.Pla_Id}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Statistics record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Statistics record column full details list """
        __list=[{'field': 'CR_Date_From', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'CR_Date_From', 'is_time': False}, {'field': 'CR_Date_To', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'CR_Date_To', 'is_time': False}, {'field': 'User_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'User_Id', 'is_time': False}, {'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Cus_Id', 'is_time': False}, {'field': 'CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CC_Id', 'is_time': False}, {'field': 'CI_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CI_Id', 'is_time': False}, {'field': 'CU_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CU_Id', 'is_time': False}, {'field': 'Typ_Code', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'NO', 'key': 'PRI', 'default': 'NUL', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Typ_Code', 'is_time': False}, {'field': 'Period', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Period', 'is_time': False}, {'field': 'Agregation', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Agregation', 'is_time': False}, {'field': 'CR_Quantity_at_Rate', 'type': 'decimal(24,12)', 'type_flask': 'db.Numeric(24,12)', 'type_sqlalchemy': 'Numeric(24,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 11, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Quantity_at_Rate', 'is_time': False}, {'field': 'CR_Quantity', 'type': 'decimal(24,12)', 'type_flask': 'db.Numeric(24,12)', 'type_sqlalchemy': 'Numeric(24,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 12, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Quantity', 'is_time': False}, {'field': 'CR_ST_at_Cur', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': '0.000000000000', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 13, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_ST_at_Cur', 'is_time': False}, {'field': 'Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 14, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Cur_Code', 'is_time': False}, {'field': 'CIT_Status', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 15, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Status', 'is_time': False}, {'field': 'CIT_Count', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 16, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Count', 'is_time': False}, {'field': 'Pla_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 17, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Pla_Id', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Statistics record column headers list """
        __list=['CR_Date_From', 'CR_Date_To', 'User_Id', 'Cus_Id', 'CC_Id', 'CI_Id', 'CU_Id', 'Typ_Code', 'Period', 'Agregation', 'CR_Quantity_at_Rate', 'CR_Quantity', 'CR_ST_at_Cur', 'Cur_Code', 'CIT_Status', 'CIT_Count', 'Pla_Id']

        return __list

    def get_column_types(self):
        """ Gets Statistics record column data types list """
        __list=['Date', 'Date', 'Integer', 'Integer', 'Integer', 'Integer', 'Integer', 'String(10)', 'String(45)', 'Integer', 'Numeric(24,12)', 'Numeric(24,12)', 'Numeric(20,12)', 'String(3)', 'Integer', 'Integer', 'Integer']

        return __list

    def get_column_meta(self):
        """ Gets Statistics record column data meta list """
        __list=[('CR_Date_From', 'Date'), ('CR_Date_To', 'Date'), ('User_Id', 'Integer'), ('Cus_Id', 'Integer'), ('CC_Id', 'Integer'), ('CI_Id', 'Integer'), ('CU_Id', 'Integer'), ('Typ_Code', 'String(10)'), ('Period', 'String(45)'), ('Agregation', 'Integer'), ('CR_Quantity_at_Rate', 'Numeric(24,12)'), ('CR_Quantity', 'Numeric(24,12)'), ('CR_ST_at_Cur', 'Numeric(20,12)'), ('Cur_Code', 'String(3)'), ('CIT_Status', 'Integer'), ('CIT_Count', 'Integer'), ('Pla_Id', 'Integer')]

        return __list

    def search_key(self,CR_Date_From,CR_Date_To,User_Id,Cus_Id,CC_Id,CI_Id,CU_Id,Typ_Code,Period,Agregation):
        """ Search for an unique Statistics record using all key fields (CR_Date_From,CR_Date_To,User_Id,Cus_Id,CC_Id,CI_Id,CU_Id,Typ_Code,Period,Agregation) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Statistics).filter(Statistics.CR_Date_From==CR_Date_From).filter(Statistics.CR_Date_To==CR_Date_To).filter(Statistics.User_Id==User_Id).filter(Statistics.Cus_Id==Cus_Id).filter(Statistics.CC_Id==CC_Id).filter(Statistics.CI_Id==CI_Id).filter(Statistics.CU_Id==CU_Id).filter(Statistics.Typ_Code==Typ_Code).filter(Statistics.Period==Period).filter(Statistics.Agregation==Agregation).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Statistics.search_key(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s): Exception: %s'%(CR_Date_From,CR_Date_To,User_Id,Cus_Id,CC_Id,CI_Id,CU_Id,Typ_Code,Period,Agregation,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Statistics.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Statistics log function """
        if self.logger is not None:
            self.logger.log(level,message)

  Statistics_Class.__name__ = 'Statistics_%s'%(table_name_suffix)
  x = Statistics_Class
  return x

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_trace.py
import sqlalchemy
class Trace(Base):
    __tablename__ = 'Trace'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Trace_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    ID   = Column( Integer, primary_key=True, autoincrement=True )
    LINE = Column( String(128) )
    
    def __init__(self, ID=0, LINE='None',engine=None,logger=None):
        """ Initiates a Trace class record """
        self.engine=engine
        self.logger=logger
        self.ID   = ID
        self.LINE = LINE

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Trace representation function """
        return "<Trace( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

    def get_list(self):
        """ Gets Trace record in list format """
        __list = [ self.ID, self.LINE]
        return __list

    def get_tuple(self):
        """ Gets Trace record in tuple format """
        __tuple = ( self.ID, self.LINE)
        return __tuple

    def get_dict(self):
        """ Gets Trace record in dict format """
        __dict={'ID':self.ID,'LINE':self.LINE}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Trace record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Trace record column full details list """
        __list=[{'field': 'ID', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'ID', 'is_time': False}, {'field': 'LINE', 'type': 'varchar(128)', 'type_flask': 'db.String(128)', 'type_sqlalchemy': 'String(128)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'LINE', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Trace record column headers list """
        __list=['ID', 'LINE']

        return __list

    def get_column_types(self):
        """ Gets Trace record column data types list """
        __list=['Integer', 'String(128)']

        return __list

    def get_column_meta(self):
        """ Gets Trace record column data meta list """
        __list=[('ID', 'Integer'), ('LINE', 'String(128)')]

        return __list

    def search_key(self,ID):
        """ Search for an unique Trace record using all key fields (ID) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Trace).filter(Trace.ID==ID).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Trace.search_key(%s): Exception: %s'%(ID,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Trace.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Trace log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_user_resumes.py
import sqlalchemy
class User_Resumes(Base):
    __tablename__ = 'User_Resumes'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='User_Resumes_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    User_Id                = Column( Integer, primary_key=True )
    Cus_Id                 = Column( Integer )
    CR_Date_From           = Column( Date, primary_key=True )
    CR_Date_To             = Column( Date, primary_key=True )
    CIT_Status             = Column( Integer, primary_key=True )
    Cur_Code               = Column( String(3), primary_key=True )
    CIT_Count              = Column( Integer )
    CIT_Quantity           = Column( Numeric(20,12) )
    CIT_Generation         = Column( Integer )
    CU_Id                  = Column( Integer, primary_key=True )
    CI_CC_Id               = Column( Integer )
    CU_Operation           = Column( String(10) )
    Typ_Code               = Column( String(10) )
    CC_Cur_Code            = Column( String(3) )
    CI_Id                  = Column( Integer, primary_key=True )
    Rat_Id                 = Column( Integer )
    Rat_Price              = Column( Numeric(20,12) )
    Rat_MU_Code            = Column( String(3) )
    Rat_Cur_Code           = Column( String(3) )
    Rat_Period             = Column( Integer )
    Rat_Hourly             = Column( Numeric(20,12) )
    Rat_Daily              = Column( Numeric(20,12) )
    Rat_Monthly            = Column( Numeric(20,12) )
    CR_Quantity            = Column( Numeric(20,12) )
    CR_Quantity_at_Rate    = Column( Numeric(20,12) )
    CC_XR                  = Column( Numeric(20,12) )
    CR_Cur_XR              = Column( Numeric(20,12) )
    CR_ST_at_Rate_Cur      = Column( Numeric(20,12) )
    CR_ST_at_CC_Cur        = Column( Numeric(20,12) )
    CR_ST_at_Cur           = Column( Numeric(20,12) )
    Cus_Name               = Column( String(255) )
    CI_Name                = Column( String(255) )
    CU_Description         = Column( String(255) )
    CC_Description         = Column( String(255) )
    Rat_Period_Description = Column( String(10) )
    CC_Code                = Column( String(45) )
    Pla_Id                 = Column( Integer )
    Pla_Name               = Column( String(255) )
    
    def __init__(self, User_Id=None, Cus_Id=None, CR_Date_From=None, CR_Date_To=None, CIT_Status=None, Cur_Code='None', CIT_Count=None, CIT_Quantity=None, CIT_Generation=1, CU_Id=None, CI_CC_Id=None, CU_Operation='None', Typ_Code='None', CC_Cur_Code='None', CI_Id=None, Rat_Id=None, Rat_Price=None, Rat_MU_Code='None', Rat_Cur_Code='None', Rat_Period=None, Rat_Hourly=None, Rat_Daily=None, Rat_Monthly=None, CR_Quantity=None, CR_Quantity_at_Rate=None, CC_XR=None, CR_Cur_XR=None, CR_ST_at_Rate_Cur=None, CR_ST_at_CC_Cur=None, CR_ST_at_Cur=None, Cus_Name='None', CI_Name='None', CU_Description='None', CC_Description='None', Rat_Period_Description='None', CC_Code='None', Pla_Id=None, Pla_Name='None',engine=None,logger=None):
        """ Initiates a User_Resumes class record """
        self.engine=engine
        self.logger=logger
        self.User_Id                = User_Id
        self.Cus_Id                 = Cus_Id
        self.CR_Date_From           = CR_Date_From
        self.CR_Date_To             = CR_Date_To
        self.CIT_Status             = CIT_Status
        self.Cur_Code               = Cur_Code
        self.CIT_Count              = CIT_Count
        self.CIT_Quantity           = CIT_Quantity
        self.CIT_Generation         = CIT_Generation
        self.CU_Id                  = CU_Id
        self.CI_CC_Id               = CI_CC_Id
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CC_Cur_Code            = CC_Cur_Code
        self.CI_Id                  = CI_Id
        self.Rat_Id                 = Rat_Id
        self.Rat_Price              = Rat_Price
        self.Rat_MU_Code            = Rat_MU_Code
        self.Rat_Cur_Code           = Rat_Cur_Code
        self.Rat_Period             = Rat_Period
        self.Rat_Hourly             = Rat_Hourly
        self.Rat_Daily              = Rat_Daily
        self.Rat_Monthly            = Rat_Monthly
        self.CR_Quantity            = CR_Quantity
        self.CR_Quantity_at_Rate    = CR_Quantity_at_Rate
        self.CC_XR                  = CC_XR
        self.CR_Cur_XR              = CR_Cur_XR
        self.CR_ST_at_Rate_Cur      = CR_ST_at_Rate_Cur
        self.CR_ST_at_CC_Cur        = CR_ST_at_CC_Cur
        self.CR_ST_at_Cur           = CR_ST_at_Cur
        self.Cus_Name               = Cus_Name
        self.CI_Name                = CI_Name
        self.CU_Description         = CU_Description
        self.CC_Description         = CC_Description
        self.Rat_Period_Description = Rat_Period_Description
        self.CC_Code                = CC_Code
        self.Pla_Id                 = Pla_Id
        self.Pla_Name               = Pla_Name

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class User_Resumes representation function """
        return "<User_Resumes( User_Id='%s', Cus_Id='%s', CR_Date_From='%s', CR_Date_To='%s', CIT_Status='%s', Cur_Code='%s', CIT_Count='%s', CIT_Quantity='%s', CIT_Generation='%s', CU_Id='%s', CI_CC_Id='%s', CU_Operation='%s', Typ_Code='%s', CC_Cur_Code='%s', CI_Id='%s', Rat_Id='%s', Rat_Price='%s', Rat_MU_Code='%s', Rat_Cur_Code='%s', Rat_Period='%s', Rat_Hourly='%s', Rat_Daily='%s', Rat_Monthly='%s', CR_Quantity='%s', CR_Quantity_at_Rate='%s', CC_XR='%s', CR_Cur_XR='%s', CR_ST_at_Rate_Cur='%s', CR_ST_at_CC_Cur='%s', CR_ST_at_Cur='%s', Cus_Name='%s', CI_Name='%s', CU_Description='%s', CC_Description='%s', Rat_Period_Description='%s', CC_Code='%s', Pla_Id='%s', Pla_Name='%s')>" % \
                ( self.User_Id, self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CU_Id, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.CC_Code, self.Pla_Id, self.Pla_Name)

    def get_list(self):
        """ Gets User_Resumes record in list format """
        __list = [ self.User_Id, self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CU_Id, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.CC_Code, self.Pla_Id, self.Pla_Name]
        return __list

    def get_tuple(self):
        """ Gets User_Resumes record in tuple format """
        __tuple = ( self.User_Id, self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CU_Id, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.CC_Code, self.Pla_Id, self.Pla_Name)
        return __tuple

    def get_dict(self):
        """ Gets User_Resumes record in dict format """
        __dict={'User_Id':self.User_Id,'Cus_Id':self.Cus_Id,'CR_Date_From':self.CR_Date_From,'CR_Date_To':self.CR_Date_To,'CIT_Status':self.CIT_Status,'Cur_Code':self.Cur_Code,'CIT_Count':self.CIT_Count,'CIT_Quantity':self.CIT_Quantity,'CIT_Generation':self.CIT_Generation,'CU_Id':self.CU_Id,'CI_CC_Id':self.CI_CC_Id,'CU_Operation':self.CU_Operation,'Typ_Code':self.Typ_Code,'CC_Cur_Code':self.CC_Cur_Code,'CI_Id':self.CI_Id,'Rat_Id':self.Rat_Id,'Rat_Price':self.Rat_Price,'Rat_MU_Code':self.Rat_MU_Code,'Rat_Cur_Code':self.Rat_Cur_Code,'Rat_Period':self.Rat_Period,'Rat_Hourly':self.Rat_Hourly,'Rat_Daily':self.Rat_Daily,'Rat_Monthly':self.Rat_Monthly,'CR_Quantity':self.CR_Quantity,'CR_Quantity_at_Rate':self.CR_Quantity_at_Rate,'CC_XR':self.CC_XR,'CR_Cur_XR':self.CR_Cur_XR,'CR_ST_at_Rate_Cur':self.CR_ST_at_Rate_Cur,'CR_ST_at_CC_Cur':self.CR_ST_at_CC_Cur,'CR_ST_at_Cur':self.CR_ST_at_Cur,'Cus_Name':self.Cus_Name,'CI_Name':self.CI_Name,'CU_Description':self.CU_Description,'CC_Description':self.CC_Description,'Rat_Period_Description':self.Rat_Period_Description,'CC_Code':self.CC_Code,'Pla_Id':self.Pla_Id,'Pla_Name':self.Pla_Name}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets User_Resumes record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets User_Resumes record column full details list """
        __list=[{'field': 'User_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'User_Id', 'is_time': False}, {'field': 'Cus_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Cus_Id', 'is_time': False}, {'field': 'CR_Date_From', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'CR_Date_From', 'is_time': False}, {'field': 'CR_Date_To', 'type': 'date', 'type_flask': 'db.Date', 'type_sqlalchemy': 'Date', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'DateField', 'is_id': False, 'header': 'CR_Date_To', 'is_time': False}, {'field': 'CIT_Status', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Status', 'is_time': False}, {'field': 'Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Cur_Code', 'is_time': False}, {'field': 'CIT_Count', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Count', 'is_time': False}, {'field': 'CIT_Quantity', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CIT_Quantity', 'is_time': False}, {'field': 'CIT_Generation', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CIT_Generation', 'is_time': False}, {'field': 'CU_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CU_Id', 'is_time': False}, {'field': 'CI_CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 11, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CI_CC_Id', 'is_time': False}, {'field': 'CU_Operation', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 12, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CU_Operation', 'is_time': False}, {'field': 'Typ_Code', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 13, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Typ_Code', 'is_time': False}, {'field': 'CC_Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 14, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CC_Cur_Code', 'is_time': False}, {'field': 'CI_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 15, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'CI_Id', 'is_time': False}, {'field': 'Rat_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 16, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Rat_Id', 'is_time': False}, {'field': 'Rat_Price', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 17, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Rat_Price', 'is_time': False}, {'field': 'Rat_MU_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 18, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Rat_MU_Code', 'is_time': False}, {'field': 'Rat_Cur_Code', 'type': 'varchar(3)', 'type_flask': 'db.String(3)', 'type_sqlalchemy': 'String(3)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 19, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Rat_Cur_Code', 'is_time': False}, {'field': 'Rat_Period', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 20, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Rat_Period', 'is_time': False}, {'field': 'Rat_Hourly', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 21, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Rat_Hourly', 'is_time': False}, {'field': 'Rat_Daily', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 22, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Rat_Daily', 'is_time': False}, {'field': 'Rat_Monthly', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 23, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'Rat_Monthly', 'is_time': False}, {'field': 'CR_Quantity', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 24, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Quantity', 'is_time': False}, {'field': 'CR_Quantity_at_Rate', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 25, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Quantity_at_Rate', 'is_time': False}, {'field': 'CC_XR', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 26, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CC_XR', 'is_time': False}, {'field': 'CR_Cur_XR', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 27, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_Cur_XR', 'is_time': False}, {'field': 'CR_ST_at_Rate_Cur', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 28, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_ST_at_Rate_Cur', 'is_time': False}, {'field': 'CR_ST_at_CC_Cur', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 29, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_ST_at_CC_Cur', 'is_time': False}, {'field': 'CR_ST_at_Cur', 'type': 'decimal(20,12)', 'type_flask': 'db.Numeric(20,12)', 'type_sqlalchemy': 'Numeric(20,12)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 30, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': True, 'form_type': 'DecimalField', 'is_id': False, 'header': 'CR_ST_at_Cur', 'is_time': False}, {'field': 'Cus_Name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 31, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Cus_Name', 'is_time': False}, {'field': 'CI_Name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 32, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CI_Name', 'is_time': False}, {'field': 'CU_Description', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 33, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CU_Description', 'is_time': False}, {'field': 'CC_Description', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 34, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CC_Description', 'is_time': False}, {'field': 'Rat_Period_Description', 'type': 'varchar(10)', 'type_flask': 'db.String(10)', 'type_sqlalchemy': 'String(10)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 35, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Rat_Period_Description', 'is_time': False}, {'field': 'CC_Code', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 36, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'CC_Code', 'is_time': False}, {'field': 'Pla_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 37, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'Pla_Id', 'is_time': False}, {'field': 'Pla_Name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 38, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'Pla_Name', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets User_Resumes record column headers list """
        __list=['User_Id', 'Cus_Id', 'CR_Date_From', 'CR_Date_To', 'CIT_Status', 'Cur_Code', 'CIT_Count', 'CIT_Quantity', 'CIT_Generation', 'CU_Id', 'CI_CC_Id', 'CU_Operation', 'Typ_Code', 'CC_Cur_Code', 'CI_Id', 'Rat_Id', 'Rat_Price', 'Rat_MU_Code', 'Rat_Cur_Code', 'Rat_Period', 'Rat_Hourly', 'Rat_Daily', 'Rat_Monthly', 'CR_Quantity', 'CR_Quantity_at_Rate', 'CC_XR', 'CR_Cur_XR', 'CR_ST_at_Rate_Cur', 'CR_ST_at_CC_Cur', 'CR_ST_at_Cur', 'Cus_Name', 'CI_Name', 'CU_Description', 'CC_Description', 'Rat_Period_Description', 'CC_Code', 'Pla_Id', 'Pla_Name']

        return __list

    def get_column_types(self):
        """ Gets User_Resumes record column data types list """
        __list=['Integer', 'Integer', 'Date', 'Date', 'Integer', 'String(3)', 'Integer', 'Numeric(20,12)', 'Integer', 'Integer', 'Integer', 'String(10)', 'String(10)', 'String(3)', 'Integer', 'Integer', 'Numeric(20,12)', 'String(3)', 'String(3)', 'Integer', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'Numeric(20,12)', 'String(255)', 'String(255)', 'String(255)', 'String(255)', 'String(10)', 'String(45)', 'Integer', 'String(255)']

        return __list

    def get_column_meta(self):
        """ Gets User_Resumes record column data meta list """
        __list=[('User_Id', 'Integer'), ('Cus_Id', 'Integer'), ('CR_Date_From', 'Date'), ('CR_Date_To', 'Date'), ('CIT_Status', 'Integer'), ('Cur_Code', 'String(3)'), ('CIT_Count', 'Integer'), ('CIT_Quantity', 'Numeric(20,12)'), ('CIT_Generation', 'Integer'), ('CU_Id', 'Integer'), ('CI_CC_Id', 'Integer'), ('CU_Operation', 'String(10)'), ('Typ_Code', 'String(10)'), ('CC_Cur_Code', 'String(3)'), ('CI_Id', 'Integer'), ('Rat_Id', 'Integer'), ('Rat_Price', 'Numeric(20,12)'), ('Rat_MU_Code', 'String(3)'), ('Rat_Cur_Code', 'String(3)'), ('Rat_Period', 'Integer'), ('Rat_Hourly', 'Numeric(20,12)'), ('Rat_Daily', 'Numeric(20,12)'), ('Rat_Monthly', 'Numeric(20,12)'), ('CR_Quantity', 'Numeric(20,12)'), ('CR_Quantity_at_Rate', 'Numeric(20,12)'), ('CC_XR', 'Numeric(20,12)'), ('CR_Cur_XR', 'Numeric(20,12)'), ('CR_ST_at_Rate_Cur', 'Numeric(20,12)'), ('CR_ST_at_CC_Cur', 'Numeric(20,12)'), ('CR_ST_at_Cur', 'Numeric(20,12)'), ('Cus_Name', 'String(255)'), ('CI_Name', 'String(255)'), ('CU_Description', 'String(255)'), ('CC_Description', 'String(255)'), ('Rat_Period_Description', 'String(10)'), ('CC_Code', 'String(45)'), ('Pla_Id', 'Integer'), ('Pla_Name', 'String(255)')]

        return __list

    def search_key(self,User_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id,CI_Id):
        """ Search for an unique User_Resumes record using all key fields (User_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id,CI_Id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(User_Resumes).filter(User_Resumes.User_Id==User_Id).filter(User_Resumes.CR_Date_From==CR_Date_From).filter(User_Resumes.CR_Date_To==CR_Date_To).filter(User_Resumes.CIT_Status==CIT_Status).filter(User_Resumes.Cur_Code==Cur_Code).filter(User_Resumes.CU_Id==CU_Id).filter(User_Resumes.CI_Id==CI_Id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='User_Resumes.search_key(%s,%s,%s,%s,%s,%s,%s): Exception: %s'%(User_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id,CI_Id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='User_Resumes.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class User_Resumes log function """
        if self.logger is not None:
            self.logger.log(level,message)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# GV gen_model_flask.py:418 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/orm_users.py
import sqlalchemy
class Users(Base):
    __tablename__ = 'Users'
    engine        = None
    logger        = None

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if sqlalchemy.__version__ >= '1.4':
                   inspector = sqlalchemy.inspect(engine)
                   table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
               else:
                   table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
               if not table_exists:
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if sqlalchemy.__version__ >= '1.4':
                       inspector = sqlalchemy.inspect(engine)
                       table_exists = inspector.has_table(__class__.__tablename__,schema='collector')
                   else:
                       table_exists = engine.dialect.has_table(engine, __class__.__tablename__)
                   if not table_exists:
                       print('460 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       pass # GV print('462 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('464 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'gen/gen_model_flask.py: 466 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Users_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    id            = Column( Integer, primary_key=True, autoincrement=True )
    username      = Column( String(64) )
    name          = Column( String(255) )
    role_id       = Column( Integer, ForeignKey('Roles.id') )
    email         = Column( String(64) )
    password_hash = Column( String(128) )
    confirmed     = Column( Boolean )
    CC_Id         = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    roles         = Column( String(255) )
    ldap          = Column( Boolean )
    ldap_method   = Column( String(45) )
    ldap_user     = Column( String(45) )
    ldap_common   = Column( String(45) )
    ldap_host     = Column( String(45) )
    ldap_port     = Column( Integer )
    ldap_domain   = Column( String(45) )
    vars          = Column( String(255) )
    
    def __init__(self, id=0, username='None', name='None', role_id=None, email='None', password_hash='None', confirmed=0, CC_Id=1, roles='None', ldap=0, ldap_method='None', ldap_user='None', ldap_common='None', ldap_host='None', ldap_port=0, ldap_domain='None', vars='None',engine=None,logger=None):
        """ Initiates a Users class record """
        self.engine=engine
        self.logger=logger
        self.id            = id
        self.username      = username
        self.name          = name
        self.role_id       = role_id
        self.email         = email
        self.password_hash = password_hash
        self.confirmed     = confirmed
        self.CC_Id         = CC_Id
        self.roles         = roles
        self.ldap          = ldap
        self.ldap_method   = ldap_method
        self.ldap_user     = ldap_user
        self.ldap_common   = ldap_common
        self.ldap_host     = ldap_host
        self.ldap_port     = ldap_port
        self.ldap_domain   = ldap_domain
        self.vars          = vars

        self.log('Created %s'%self)
    def __repr__(self):
        """ default class Users representation function """
        return "<Users( id='%s', username='%s', name='%s', role_id='%s', email='%s', password_hash='%s', confirmed='%s', CC_Id='%s', roles='%s', ldap='%s', ldap_method='%s', ldap_user='%s', ldap_common='%s', ldap_host='%s', ldap_port='%s', ldap_domain='%s', vars='%s')>" % \
                ( self.id, self.username, self.name, self.role_id, self.email, self.password_hash, self.confirmed, self.CC_Id, self.roles, self.ldap, self.ldap_method, self.ldap_user, self.ldap_common, self.ldap_host, self.ldap_port, self.ldap_domain, self.vars)

    def get_list(self):
        """ Gets Users record in list format """
        __list = [ self.id, self.username, self.name, self.role_id, self.email, self.password_hash, self.confirmed, self.CC_Id, self.roles, self.ldap, self.ldap_method, self.ldap_user, self.ldap_common, self.ldap_host, self.ldap_port, self.ldap_domain, self.vars]
        return __list

    def get_tuple(self):
        """ Gets Users record in tuple format """
        __tuple = ( self.id, self.username, self.name, self.role_id, self.email, self.password_hash, self.confirmed, self.CC_Id, self.roles, self.ldap, self.ldap_method, self.ldap_user, self.ldap_common, self.ldap_host, self.ldap_port, self.ldap_domain, self.vars)
        return __tuple

    def get_dict(self):
        """ Gets Users record in dict format """
        __dict={'id':self.id,'username':self.username,'name':self.name,'role_id':self.role_id,'email':self.email,'password_hash':self.password_hash,'confirmed':self.confirmed,'CC_Id':self.CC_Id,'roles':self.roles,'ldap':self.ldap,'ldap_method':self.ldap_method,'ldap_user':self.ldap_user,'ldap_common':self.ldap_common,'ldap_host':self.ldap_host,'ldap_port':self.ldap_port,'ldap_domain':self.ldap_domain,'vars':self.vars}

        return __dict

    def get_json_dict(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return __dict

    def get_json(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        __dict = self.get_dict()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for key in __dict.keys():
            if   'datetime.datetime' in str(type(__dict[key])): __dict[key]=__dict[key].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(dateformat)
            elif 'datetime.time'     in str(type(__dict[key])): __dict[key]=__dict[key].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__dict[key])): __dict[key]=float(__dict[key])
        return json.dumps(__dict)

    def post(self):
       return self

    def patch(self,**kwargs):
       for field in self.get_column_headers():
           if field in kwargs.keys():
               setattr(self,field,kwargs[field])
       return self

    def delete(self):
       return True

    def get_json_array(self,dateformat='%Y-%m-%d',timeformat='%H:%M:%S',datetimeformat=None):
        """ Gets Users record in JSON array format """
        __list = self.get_list()
        if datetimeformat is None: 
            datetimeformat='%s %s'%(dateformat,timeformat)
        for field in range(len(__list)):
            if   'datetime.datetime' in str(type(__list[field])): __list[field]=__list[field].strftime(datetimeformat)
            elif 'datetime.date'     in str(type(__list[field])): __list[field]=__list[field].strftime(dateformat)
            elif 'datetime.time'     in str(type(__list[field])): __list[field]=__list[field].strftime(timeformat)
            elif 'decimal.Decimal'   in str(type(__list[field])): __list[field]=float(__list[field])
        return __list

    def get_columns(self):
        """ Gets Users record column full details list """
        __list=[{'field': 'id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'PRI', 'default': None, 'extra': 'auto_increment', 'is_form_editable': True, 'format': None, 'order': 1, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': True, 'header': 'Id', 'is_time': False}, {'field': 'username', 'type': 'varchar(64)', 'type_flask': 'db.String(64)', 'type_sqlalchemy': 'String(64)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 2, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'username', 'is_time': False}, {'field': 'name', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 3, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'name', 'is_time': False}, {'field': 'role_id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 4, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'id', 'referenced_table': 'Roles', 'referenced_class': 'Role', 'foreign_key': 'id', 'foreign_value': 'name', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'role_id', 'is_time': False}, {'field': 'email', 'type': 'varchar(64)', 'type_flask': 'db.String(64)', 'type_sqlalchemy': 'String(64)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 5, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'email', 'is_time': False}, {'field': 'password_hash', 'type': 'varchar(128)', 'type_flask': 'db.String(128)', 'type_sqlalchemy': 'String(128)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 6, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'password_hash', 'is_time': False}, {'field': 'confirmed', 'type': 'tinyint', 'type_flask': 'db.Boolean', 'type_sqlalchemy': 'Boolean', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 7, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'BooleanField', 'is_id': False, 'header': 'confirmed', 'is_time': False}, {'field': 'CC_Id', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'NO', 'key': 'MUL', 'default': '1', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 8, 'is_searchable': True, 'is_fk': True, 'foreign_field': 'CC_Id', 'referenced_table': 'Cost_Centers', 'referenced_class': 'cost_center', 'foreign_key': 'CC_Id', 'foreign_value': 'CC_Description', 'is_numeric': False, 'form_type': 'SelectField', 'is_id': False, 'header': 'CC_Id', 'is_time': False}, {'field': 'roles', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 9, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'roles', 'is_time': False}, {'field': 'ldap', 'type': 'tinyint', 'type_flask': 'db.Boolean', 'type_sqlalchemy': 'Boolean', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 10, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'BooleanField', 'is_id': False, 'header': 'ldap', 'is_time': False}, {'field': 'ldap_method', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 11, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'ldap_method', 'is_time': False}, {'field': 'ldap_user', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 12, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'ldap_user', 'is_time': False}, {'field': 'ldap_common', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 13, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'ldap_common', 'is_time': False}, {'field': 'ldap_host', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 14, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'ldap_host', 'is_time': False}, {'field': 'ldap_port', 'type': 'int', 'type_flask': 'db.Integer', 'type_sqlalchemy': 'Integer', 'null': 'YES', 'key': '', 'default': '0', 'extra': '', 'is_form_editable': True, 'format': None, 'order': 15, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'IntegerField', 'is_id': False, 'header': 'ldap_port', 'is_time': False}, {'field': 'ldap_domain', 'type': 'varchar(45)', 'type_flask': 'db.String(45)', 'type_sqlalchemy': 'String(45)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 16, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'ldap_domain', 'is_time': False}, {'field': 'vars', 'type': 'varchar(255)', 'type_flask': 'db.String(255)', 'type_sqlalchemy': 'String(255)', 'null': 'YES', 'key': '', 'default': None, 'extra': '', 'is_form_editable': True, 'format': None, 'order': 17, 'is_searchable': True, 'is_fk': False, 'foreign_field': None, 'is_numeric': False, 'form_type': 'StringField', 'is_id': False, 'header': 'vars', 'is_time': False}]

        return __list

    def get_column_headers(self):
        """ Gets Users record column headers list """
        __list=['id', 'username', 'name', 'role_id', 'email', 'password_hash', 'confirmed', 'CC_Id', 'roles', 'ldap', 'ldap_method', 'ldap_user', 'ldap_common', 'ldap_host', 'ldap_port', 'ldap_domain', 'vars']

        return __list

    def get_column_types(self):
        """ Gets Users record column data types list """
        __list=['Integer', 'String(64)', 'String(255)', 'Integer', 'String(64)', 'String(128)', 'Boolean', 'Integer', 'String(255)', 'Boolean', 'String(45)', 'String(45)', 'String(45)', 'String(45)', 'Integer', 'String(45)', 'String(255)']

        return __list

    def get_column_meta(self):
        """ Gets Users record column data meta list """
        __list=[('id', 'Integer'), ('username', 'String(64)'), ('name', 'String(255)'), ('role_id', 'Integer'), ('email', 'String(64)'), ('password_hash', 'String(128)'), ('confirmed', 'Boolean'), ('CC_Id', 'Integer'), ('roles', 'String(255)'), ('ldap', 'Boolean'), ('ldap_method', 'String(45)'), ('ldap_user', 'String(45)'), ('ldap_common', 'String(45)'), ('ldap_host', 'String(45)'), ('ldap_port', 'Integer'), ('ldap_domain', 'String(45)'), ('vars', 'String(255)')]

        return __list

    def search_key(self,id):
        """ Search for an unique Users record using all key fields (id) """
        try:
            if self.engine is not None:
                Session=sessionmaker(bind=self.engine)
                session=Session()
                record = session.query(Users).filter(Users.id==id).one_or_none()
                session.flush()
            else:
                session.rollback()
                record = None
        except Exception as e:
            detail='Users.search_key(%s): Exception: %s'%(id,e)
            emtec_handle_general_exception(e,detail=detail,module=__name__,function='Users.search_key()',logger=self.logger)
            record = None
        return record

    def log(self,message,level=logging.DEBUG):
        """ Class Users log function """
        if self.logger is not None:
            self.logger.log(level,message)


