from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(401)
def err_401(error):
   return render_template( 'errors/401.html', error=error), 401

@errors.app_errorhandler(403)
def err_403(error):
   return render_template( 'errors/403.html' , error=error), 403

@errors.app_errorhandler(404)
def err_404(error):
   return render_template( 'errors/404.html' , error=error), 404

@errors.app_errorhandler(500)
def err_500(error):
   return render_template( 'errors/500.html' , error=error), 500

