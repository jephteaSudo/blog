from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)


app.config['SECRET_KEY']='6c41aaf85aa2238a5f3a8efb383f9e99'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'

db=SQLAlchemy(app)

from flaskblog import routes