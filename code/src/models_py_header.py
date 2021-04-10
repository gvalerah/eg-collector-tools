# =============================================================================
# Models File
# Static Header File. 
# source: models_py_header.py
# GLVH 2019-08-16
# GLVH 2020-01-30 JSON Serializing code added
# =============================================================================
from app                    import db
from app                    import login_manager

from datetime               import datetime

from sqlalchemy             import Column, String, Integer, Numeric, Date, Time, Boolean, DateTime
from sqlalchemy             import ForeignKey

from flask_sqlalchemy       import SQLAlchemy
from copy                   import copy, deepcopy

# Required form Authorization subsystem
from werkzeug.security      import generate_password_hash, check_password_hash
from itsdangerous           import TimedJSONWebSignatureSerializer as Serializer
from flask                  import current_app
from flask_login            import UserMixin, AnonymousUserMixin

# JSON Serializing enabling code
from sqlalchemy.inspection import inspect


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

# 20200224 GV force import of the whole emtec db library ---------------
from emtec.collector.db.orm_model       import *
from emtec.collector.db.flask_models    import *
# ----------------------------------------------------------------------
