
from myapp import app
from flask import  request, redirect, url_for, session, make_response

from flask_admin import Admin, expose 
from flask_admin.contrib.sqla import  ModelView
from flask_admin.base import AdminIndexView, BaseView

from jinja2.utils  import markupsafe
import os

import subprocess


class MyAdminIndexView(AdminIndexView):

    def is_visible(self):
        return False

    @expose('/') # /admin/
    def change_theme(self):
        cookThme = request.cookies.get('theme')
        appTheme = app.config['FLASK_ADMIN_SWATCH']
        t = request.args.get('theme', cookThme if cookThme else  appTheme ) 
        
        app.config['FLASK_ADMIN_SWATCH'] = t

        keys = app.config.keys()
        ignored_keys=['SQLALCHEMY_DATABASE_URI']
        environs = { k:v for (k,v) in os.environ.items() if k in keys and k not in ignored_keys}
        for k,v in environs.items():
            if 'PASSWORD' in k:
                environs[k] = '******'
        
        resp = make_response( self.render(
                'admin/index.html', 
                theme = t, 
                environs = environs
            )
        )

        resp.set_cookie('theme', t, max_age=1*60*60*1000)
        
        return resp 

def date_format(view, value):
    return markupsafe.Markup(f""" 
        <div style="white-space: nowrap;">{value.strftime('%Y-%m-%d %H:%M')}</div>
    """)


from flask_admin.model import typefmt
from datetime import date
MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({
    date: date_format
})

# see beautifull options :)
# https://flask-admin.readthedocs.io/en/latest/api/mod_model/
class myModelView(ModelView):
    page_size = 50
    can_set_page_size = True
    # can_export = True
    # can_view_details = True
    column_type_formatters = MY_DEFAULT_FORMATTERS

    # redirect to login page if user doesn't have access
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('user.login', next=request.url))





class ConfigView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/config.html', os=os)



from flask_admin.contrib.fileadmin import FileAdmin

def configure_admin(app):
    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'united'

    # Add administrative views here
    admin = Admin(app, 
        name='ADMIN', 
        template_mode='bootstrap3',
        base_template='admin/my_master.html',
        index_view=MyAdminIndexView()
        )

    
    admin.add_view( ConfigView(name='Config', endpoint='config') )
    
    
    # https://flask-admin.readthedocs.io/en/latest/api/mod_contrib_fileadmin/
    
    import os.path as op
    path = op.join(op.dirname(__file__), '../static')
    fa = FileAdmin(base_path=path, name='Static Files')
    fa.can_mkdir = True
    fa.can_download = True
    admin.add_view( fa )
    
    
