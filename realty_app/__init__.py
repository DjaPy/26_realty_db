import os
from flask import Flask
from realty_app.models import db


app = Flask(__name__)
app.config.from_object('config')
db.app = app
db.init_app(app)

if not os.path.exists('real_estate.db'):
    db.create_all()

from realty_app import views