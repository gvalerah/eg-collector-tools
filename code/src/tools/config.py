import os
import  configparser
from    configparser        import ConfigParser, ExtendedInterpolation
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    print("OS COLLECTOR_CONFIG_FILE=%s" % os.environ.get('COLLECTOR_CONFIG_FILE'))
    SECRET_KEY                      = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN   = os.environ.get('SQLALCHEMY_COMMIT_ON_TEARDOWN') or True
    SQLALCHEMY_TRACK_MODIFICATIONS  = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False
    MAIL_SERVER                     = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT                       = os.environ.get('MAIL_PORT') or 25
    MAIL_USE_TLS                    = os.environ.get('MAIL_USE_TLS') or False
    MAIL_USE_SSL                    = os.environ.get('MAIL_USE_SSL') or False
    MAIL_USERNAME                   = os.environ.get('MAIL_USERNAME') or ''
    MAIL_PASSWORD                   = os.environ.get('MAIL_PASSWORD') or ''
    COLLECTOR_MAIL_SUBJECT_PREFIX   = os.environ.get('COLLECTOR_MAIL_SUBJECT_PREFIX') or '[Collector]'
    COLLECTOR_MAIL_SENDER           = os.environ.get('COLLECTOR_MAIL_SUBJECT_PREFIX') or 'Collector Admin <gvalera@emtecgroup.net>'
    COLLECTOR_ADMIN                 = os.environ.get('COLLECTOR_ADMIN') or 'collector'
    COLLECTOR_CONFIG_FILE           = os.environ.get('COLLECTOR_CONFIG_FILE') or '%s/collector.ini'%basedir
    if os.environ.get('LINES_PER_PAGE') is not None:
        LINES_PER_PAGE                  = int(os.environ.get('LINES_PER_PAGE')) or 5
    else:
        LINES_PER_PAGE                  = 5


    if COLLECTOR_CONFIG_FILE is not None and os.path.isfile(COLLECTOR_CONFIG_FILE):
                print("config.py.__init__app: reading %s"%COLLECTOR_CONFIG_FILE)
                config_ini = configparser.ConfigParser(interpolation=ExtendedInterpolation())
                config_ini.read( COLLECTOR_CONFIG_FILE )
                
                # Forced production environment configuration
                # from config_ini file
                SQLALCHEMY_COMMIT_ON_TEARDOWN  = config_ini.getboolean('General','SQLALCHEMY_COMMIT_ON_TEARDOWN',fallback=True)
                SQLALCHEMY_TRACK_MODIFICATIONS = config_ini.getboolean('General','SQLALCHEMY_TRACK_MODIFICATIONS',fallback=False)
                MAIL_SERVER                    = config_ini.get       ('General','MAIL_SERVER',fallback='localhost')
                #......
                #AQUI ME QUEDE ....
                #.......        
                DATABASE_URL = "%s://%s:%s@%s:%s/%s"%(
                    config_ini.get('DB','driver'),
                    config_ini.get('DB','user'),
                    config_ini.get('DB','password'),
                    config_ini.get('DB','host'),
                    config_ini.get('DB','port'),
                    config_ini.get('DB','schema')
                    )
                os.environ['DATABASE_URL']          = DATABASE_URL
    else:
                print("config.py.__init__app: no environment configuration file evaluated.")

    if True:
        print(SECRET_KEY)
        print(SQLALCHEMY_COMMIT_ON_TEARDOWN)
        print(SQLALCHEMY_TRACK_MODIFICATIONS)
        print(MAIL_SERVER                    )
        print(MAIL_PORT                       )
        print(MAIL_USE_TLS                    )
        print(MAIL_USE_SSL                    )
        print(MAIL_USERNAME                   )
        print(MAIL_PASSWORD                   )
        print(COLLECTOR_MAIL_SUBJECT_PREFIX   )
        print(COLLECTOR_MAIL_SENDER           )
        print(COLLECTOR_ADMIN                 )
        print(COLLECTOR_CONFIG_FILE           )
        print(LINES_PER_PAGE                  )

        
    @staticmethod
    def init_app(app):
        print("*******************************************************")
        print("%s: Config.init_app (idle/pass function). Configuration oportunity here."%__name__)
        print("*******************************************************")
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class ToolsConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TOOLS_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-tools.sqlite')

config = {
    'development'   : DevelopmentConfig,
    'testing'       : TestingConfig,
    'production'    : ProductionConfig,
    'tools'         : ToolsConfig,

    'default'       : DevelopmentConfig
}
