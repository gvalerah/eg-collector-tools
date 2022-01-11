# GV =============================================================================
# GV Models File
# GV Static Header File. 
# GV source: models_py_header.py
# GV GLVH 2019-08-16
# GV GLVH 2020-01-30 JSON Serializing code added
# GV =============================================================================
from app                    import db
from app                    import login_manager

from datetime               import datetime

from sqlalchemy             import Column, String, Integer, Numeric, Date, Time, Boolean, DateTime
from sqlalchemy             import ForeignKey

from flask_sqlalchemy       import SQLAlchemy
from copy                   import copy, deepcopy

# GV Required form Authorization subsystem
from werkzeug.security      import generate_password_hash, check_password_hash
from itsdangerous           import TimedJSONWebSignatureSerializer as Serializer
from flask                  import current_app
from flask_login            import UserMixin, AnonymousUserMixin

# GV JSON Serializing enabling code
from sqlalchemy.inspection import inspect


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

# GV 20200224 GV force import of the whole emtec db library ---------------
from emtec.collector.db.orm_model       import *
from emtec.collector.db.flask_models    import *
# GV ----------------------------------------------------------------------
