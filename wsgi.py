# https://homecarde.herokuapp.com/
# Don't use this since PORT can't be taken from Env.
# $ waitress-serve --port=8080 wsgi:app

# Just use this
# python wsgi.py

# MUST BE BEFORE CREATING `app`
from dotenv import load_dotenv
load_dotenv('.env') 

# -------------------------------------
from myapp import app
import os

# This is production only, it won't reloaded when you edit the code.
# DON'T use Werkzeug, not worthy
print("---- PRODUCTION MODE WAITRESS >>>>>>>>")

p = os.environ.get('PORT')
p = p if p else '5044'

from waitress import serve

if __name__ == '__main__':
    # host='0.0.0.0' means all IP addresses on this host
    # url_scheme='https' to use https
    serve(app, host='0.0.0.0', port=p) 
    
