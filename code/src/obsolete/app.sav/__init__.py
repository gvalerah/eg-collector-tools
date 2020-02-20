#print("**** app.__init__.py ***")
# Application package constructor
# ---------------
# app.__init__.py
# ---------------
import  logging
from    config                             import config

from    flask                              import Flask, render_template
from    flask_bootstrap                    import Bootstrap
from    flask_mail                         import Mail
from    flask_moment                       import Moment
from    flask_sqlalchemy                   import SQLAlchemy
from    flask_login                        import LoginManager

from    emtec.common.functions             import *
from    emtec.collector.common.context     import Context
from    emtec.collector.db.orm             import *

bootstrap                           = Bootstrap()
mail                                = Mail()
moment                              = Moment()
db                                  = Collector_ORM_DB()
login_manager                       = LoginManager()

# Setup Login manager
login_manager.session_protection    = 'strong'
login_manager.login_view            = 'auth.login'

# create logger logger
add_Logging_Levels()
logger  = logging.getLogger('Collector')

def create_app(config_name,C):
    app = Flask(__name__,root_path='%s/app'%C.app_folder)
    # Calls configuration Manager 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Inititializes applications (incomplete by now)
    bootstrap.init_app      (app)
    mail.init_app           (app)
    moment.init_app         (app)
    db.init_app             (app)
    login_manager.init_app  (app)
    # Collector's modules
    
    # attach routes and custom error pages here
    from app.main   import main as main_blueprint          # NOTE: Example talks on main here .main was required . (Why?)
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
    
