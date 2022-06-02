
from flask import Blueprint, flash, redirect, render_template


# 2 Factor Auhintication
# https://blog.miguelgrinberg.com/post/two-factor-authentication-with-flask

adminbp = Blueprint( 'adminbp', __name__ )


@adminbp.route("/admin/config", methods=['GET'] ) #
def admin_config( ):
    return render_template('/admin/config.html')


from myapp import app
import datetime

from io import BytesIO
import zipfile
import os
from flask import send_file
from myapp.config import *

@adminbp.route("/admin/backup-static", methods=['GET'] ) #
def backup_static():
    fileName = f"static-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"
    memory_file = BytesIO()

    file_path = os.path.join(app.config['PUBLIC_HTML_PATH'], 'myapp/static')
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED)as zipf:
        for root, dirs, files in os.walk(file_path):
            for file in files:
                zipf.write(os.path.join(root, file))

    memory_file.seek(0)
    return send_file(memory_file,
                     attachment_filename=fileName,
                     as_attachment=True)


