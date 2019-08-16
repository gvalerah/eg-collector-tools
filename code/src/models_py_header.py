# =============================================================================
# Models File
# Static Header File. 
# GLVH 2019-08-16
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



