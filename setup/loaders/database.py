from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """Inicializa o banco e reflete tabelas existentes."""
    db.init_app(app)
    with app.app_context():
        db.reflect()
