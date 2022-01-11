from flask import render_template
from . import main

""" Application decorators for routes """
""" Decorators specify main routes to be handled by Collector Solution """

@main.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


"""
# GV 7-6 Blueprint with error handlers
# GV from flask import render_template
# GV from . import main

# GV @main.app_errorhandler(404)
# GV def page_not_found(e):
# GV     return render_template('404.html'), 404

# GV @main.app_errorhandler(500)
# GV def internal_server_error(e):
# GV     return render_template('500.html'), 500
"""
