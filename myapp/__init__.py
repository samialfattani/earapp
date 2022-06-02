
from flask import Flask, request
from myapp.config import *
from flask import Flask

app = Flask(__name__)

# app.config will be filled automatically
app.config.from_pyfile('config.py')

print('')
print( f"{'PUBLIC_HTML_PATH':<25}=", app.config['PUBLIC_HTML_PATH'] )
print( f"{'ENV_SOURCE':<25}: { app.config['ENV_SOURCE'] }")
print( f"{'Root Path':<25}: { app.root_path }")

print('')
print(f"---- {__name__} package is Loading... ",  )


#  ------------ create Cryptor
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)


from myapp.admin.admin_conf import configure_admin
configure_admin(app)

from flask_dropzone import Dropzone
dropzone = Dropzone(app)

# Dropzone settings
# https://flask-dropzone.readthedocs.io/en/latest/configuration.html
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_PARALLEL_UPLOADS'] = 2
# app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
# app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
# app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings
# app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

@app.context_processor
def get_server_info():
  domain = request.headers['Host']

  server_info = {
      'domain' : domain, 
      'app_name': app.config['USER_APP_NAME']
  }

  return {"server_info": server_info}


from myapp.main.routes import main
from myapp.admin.routes import adminbp


from myapp.errors.handlers import errors
app.register_blueprint(main)
app.register_blueprint(errors)
app.register_blueprint(adminbp)

print(f"---- {__name__} is initiated ----------------||||")
