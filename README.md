
# **Flask Blogger**
Groub dataset.

## Technology Used
* Python
* Flask, including admin, dropzone

### install Python Virtual Env.
```PS
> pip install virtualenv
> virtualenv env
> Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force 
> env\Scripts\activate.ps1
> python -m pip install --upgrade pip
```



### **Upload to Heroku**
In heroku we need the folder of `public_html` that contains which supposed to be out of our git folder, but in Heroku you have to include it so you can upload all files within one `push`.

```bash
$ heroku login
$ git commit -m 'final version'
$ git push heroku master
$ heroku logs --app earapp-dataset --tail
```

Here is the `Procfile` content.
```
web: python wsgi.py
```

All **Env** variables will be scannd from `.env` file. however, you can override some of them from Heroku.com > (yourapp) > `Settings...` > `Config Vars`. Change Vars as the following:
```
PUBLIC_HTML_PATH = /app/public_html
SQLALCHEMY_DATABASE_URI = sqlite:///../public_html/halim.db
TZ = Asia/Riyadh
```




## **Usage**
#### **Step1:** clone from git hub
```bash
$ git clone
```
#### **Step2:** Edite configuration information
* on Windows/Mac/Linux edit `.env` file.
```
SECRET_KEY=33f2a33b
```
### **Step3: execute the app**
```bash
# on local machaine:
$ python run.py

# on Heroku:
$ python  wsgi.py

# on alvoucher.com:
$ gunicorn -w 9 guni:app
```

dddddd