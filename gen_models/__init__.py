# Application package constructor
# ---------------
# app.__init__.py
# ---------------

from flask                  import Flask, render_template
from flask_bootstrap        import Bootstrap
from flask_mail             import Mail
from flask_moment           import Moment
from flask_sqlalchemy       import SQLAlchemy

from config                 import config

# Collector application required modules
from emtec.collector.common.context        import Context

bootstrap   = Bootstrap()
mail        = Mail()
moment      = Moment()
db          = SQLAlchemy()

C           = Context()

import logging

# create logger
logger = logging.getLogger('initial import logger')


def create_app(config_name):
    
    app = Flask(__name__)
    
    
    # Calls configuration Manager 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Inititializes applications (incomplete by now)
    bootstrap.init_app  (app)
    mail.init_app       (app)
    moment.init_app     (app)
    db.init_app         (app)
    # Collector's modules
    C.init_app          (app)
    logger=C.logger
    
    return app
