#print("**** app.main.__init__.py ***")
# 7-4 app/main/__init__.py Blueprint creation (package constructor)

from flask import Blueprint

#print("        app/main/__init__.py: main = Blueprint( 'main', __name__ =",__name__,')')

#print("**** app.main.__init__.py *** main = Blueprint('main', __name__)",__name__)
main = Blueprint('main', __name__)
#print("**** app.main.__init__.py *** main = ",main)

#print("        app/main/__init__.py: main is =",main)

# These imports need to be at the bottom of the constructor to avoid curcular references
# since the modules need to import main blueprint

#print("        app/main/__init__.py: Importing views ...")
#from . import views
#print("**** app.main.__init__.py *** from emtec.collector import views ...")
from . import views
#print("        app/main/__init__.py: Views importing compĺeted ...")

#print("        app/main/__init__.py: Importing errors ...")
from . import errors
#print("        app/main/__init__.py: Errors importing compĺeted ...")

#print("        app/main/__init__.py: Importing plugins ...")
from . import plugins
#print("        app/main/__init__.py: Plugins importing compĺeted ...")

#print("        app/main/__init__.py: Blueprint Compĺeted ...")

# GV 20190816 from ..models import Permission
from emtec.collector.db.flask_models import Permission

# Context processors make variables globally available to all templates.
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
