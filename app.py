import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))

if project_root not in sys.path:
    sys.path.append(project_root)

from flask import Flask

from setup.db_configs import *
from setup.loaders.load_models import load_models
from setup.loaders.database import init_db, db
from setup.loaders.load_controllers import load_controllers

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = TRACK_MODIFICATIONS

    # inicializando em ordem!
    init_db(app)
    load_models("models")
    load_controllers(app,"controllers")

    with app.app_context():
        db.create_all()

    return app

app = create_app()

app.config['SECRET_KEY'] = 'bunda'

if __name__ == '__main__':
    app.run(debug=True)