import imp
from flask import render_template,request, Blueprint, send_from_directory, redirect
from myapp import app

main = Blueprint('main', __name__)

import os

@main.route("/")
@main.route("/home")
def home():

    page = request.args.get('page', 1, type=int)
   

    app_name = app.config['USER_APP_NAME']
    git_tag = ''
    return render_template('home.html', 
                    title='Home',
                    os=os,
                    app_name=app_name,
                    git_tag=git_tag
                    )


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/upload', methods=['GET', 'POST'])
def upload():

    for k, f in request.files.items():
        f.save(os.path.join(app.config['PUBLIC_HTML_PATH'], 'myapp/static', f.filename))

    return redirect('/')
