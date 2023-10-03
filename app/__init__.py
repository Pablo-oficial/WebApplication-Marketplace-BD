from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://professor:professor@database-1.c3tyn5siqwcx.us-east-1.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)

from app import models, views