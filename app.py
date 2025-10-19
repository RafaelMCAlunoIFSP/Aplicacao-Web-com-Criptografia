from flask import Flask

#from controllers.usuario import usuario_bp

from setup.db_configs import * # aqui ta a instancia do bdd criado com o sql alchemy ( por favor ler a docstring do arquivo db.py)
from setup.loaders.load_models import load_models
from setup.loaders.database import init_db
from setup.loaders.load_controllers import load_controllers

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = TRACK_MODIFICATIONS

    # inicializando em ordem!
    init_db(app)
    load_models("models")
    
    load_controllers(app,"controllers")

    return app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)