from setup.loaders.database import db
from sqlalchemy.orm import Mapped, mapped_column # Mapped aparentemente é um tipo que é usada puramente pra deixar o codigo mais pythonico, e mapped_column é pra relacionar 
from sqlalchemy import inspect


#from app import app

"""with app.app_context():
    db.reflect(bind_key= "bares") # reflete os dados do bdd pra mapear pras classes bind key é qual schema do bdd eu quero refletir
"""
class UsuarioModel:
    # Simula um 'banco de dados' em memória e a lógica de negócio.
    # Em um projeto real, aqui estariam as chamadas ao SQLAlchemy, etc.

    # Dados em memória para simplificar

    _usuarios = [
    {'id': 1, 'nome': 'Rafael Morales', 'email': 'morales@gmail.com', 'senha': '1234', 'admin': True},
    {'id': 2, 'nome': 'Rafael Moreira', 'email': 'moreira@gmail.com', 'senha': '12', 'admin': True},
    {'id': 3, 'nome': 'Julia Calixto', 'email': 'calixto@gmail.com', 'senha': '12', 'admin': True},
    {'id': 4, 'nome': 'Luis Henrique', 'email': 'luis@gmail.com', 'senha': '12', 'admin': True}
    ]
    _next_id = 5

    def get_todos(self):
        # Retorna todos os usuários
        return self._usuarios
    
    def get_um(self, user_id):
        # Retorna um único usuário pelo ID.
        for user in self._usuarios:
            if user['id'] == user_id:
                return user
        return None
    
    def salvar(self, nome, email, senha, admin):

        # Salva um novo usuário e retorna ele.

        novo_usuario = {'id': self._next_id, 'nome': nome, 'email': email, 'senha': senha, 'admin': admin}
        self._usuarios.append(novo_usuario)
        self._next_id += 1
        return novo_usuario


class EstabelecimentoModel(db.Model):
    print(db.metadata.tables.keys())
    __table__ = db.metadata.tables["estabelecimento"]
    @classmethod
    def get_all(classe):
        query = db.select(classe)
        return db.session.execute(query).scalars().all()
    @classmethod
    def get_estabelecimento(id_estabelecimento: int):
        return db.Query.get(id_estabelecimento)
    
    @classmethod
    def get_db_info():
        inspector = inspect(db.engine)
        tables = inspector.get_table_names(schema="nome_do_banco")
        print(tables)
