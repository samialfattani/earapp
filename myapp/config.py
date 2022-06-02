import os
import datetime

def str_to_bool(s):
   if not s:
      s = ''
   return True if s.lower() in ['true', 'yes', '1']  else False


BASE_URI = os.path.abspath( os.getenv('BASE_URI') )
ENV_SOURCE = os.path.abspath( os.getenv('ENV_SOURCE') )

# >>> import secrets
# >>> secrets.token_hex(16)
SECRET_KEY='fbd1eefad885bf835e1d5ea884244221'

PUBLIC_HTML_PATH = os.path.abspath( os.getenv('PUBLIC_HTML_PATH') )


# ----- FLASK USER -------------------------------------------
# Setup Flask-User and specify the User data-model
# https://flask-user.readthedocs.io/en/latest/configuring_settings.html
# 
USER_APP_NAME = os.getenv('USER_APP_NAME')

