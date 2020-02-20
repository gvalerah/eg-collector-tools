""" Import System modules """
import sys
import os
import getpass

""" Import Framework and Extentions """

import simplejson as json
import pprint
import datetime

from time                       import strftime
from datetime                   import datetime

# Flask Framework imports
from flask                      import Flask
# Flask DB Required follows
from flask_sqlalchemy           import SQLAlchemy

from flask                      import render_template
from flask_script               import Manager

from flask                      import request
from flask import               current_app

from flask_bootstrap            import Bootstrap
from flask_moment               import Moment

from flask                      import session
from flask                      import redirect
from flask                      import url_for

# Import Flask Form functions
from flask_wtf                  import Form
from wtforms                    import StringField, SubmitField
from wtforms.validators         import Required

# SQL Alchemy imports should be eliminated onece replaced by Flask Wrapper
# Import sqlalchemy functions
from sqlalchemy                 import create_engine
from sqlalchemy                 import text
from sqlalchemy                 import exc
from sqlalchemy                 import inspect

# Import sqlalchemy ORM functions
from sqlalchemy.orm             import sessionmaker

""" Import App specfic modules """

from common.context             import Context

""" Application Globals """

C = None

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    password = StringField('What is your password?', validators=[Required()])
    submit = SubmitField('Submit')


""" Creates Application Objects """

app         = Flask(__name__)

# Global Object Instances are defined here

basedir     = os.path.abspath(os.path.dirname(__file__))
manager     = Manager   (app)
bootstrap   = Bootstrap (app)
moment      = Moment    (app)
db          = SQLAlchemy(app)

# Configuration Defaults

app.config['SECRET_KEY'] = 'hard to guess string'   # Check chapter 7 for more secure method of Key generation instead of hard codding
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, '%s.sqlite'%(__name__))
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# Should be moved to app_functions.py
def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
            
""" Main Code Starts here """

if __name__ == '__main__':
    AC = app.app_context()
    AC.push()
    config_file = "collector.ini"
    if C is None:
        C = Context("Collector Server",config_file)    
    if (C):
        logger = C.logger
        logger.info("****** Collector Server *****************")
        logger.info("%s: as '%s' Using configuration: '%s'"%(sys.argv[0],getpass.getuser(),config_file))
        logger.info("*****************************************")

    manager.run()

