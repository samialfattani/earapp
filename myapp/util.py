
import os
import secrets
# from PIL import Image

from flask import url_for, redirect, request
from myapp import app
from functools import wraps
from myapp.config import *

SHORT_DATE_FORMAT = '%Y-%m-%d'

def add(x=0,y=0):
    return x+y

def rename_picture(obj, form_picture):
    print(obj.id)
    _, f_ext = os.path.splitext(form_picture.filename)
    
    random_hex = secrets.token_hex(8)    
    picFname = random_hex + f_ext

    return picFname

def create_image_file_if_missing(img_file, img_data):
    p = os.path.join(app.config['PUBLIC_HTML_PATH'], f"{img_file}")
    if img_file and img_data and not os.path.exists(p):
        f = open(p, 'wb')
        f.write(img_data)
        f.close()            

from functools import wraps
agree = True


def agree_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.agreed:
            return redirect(url_for('users.agreement', next=request.full_path))
        return f(*args, **kwargs)
    return wrapper


def current_user_or_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.agreed:
            return redirect(url_for('users.agreement', next=request.full_path))
        return f(*args, **kwargs)
    return wrapper



