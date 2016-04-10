from flask import Flask

import os
from flask.ext.login import LoginManager
from config import basedir
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)

from app import views, models
