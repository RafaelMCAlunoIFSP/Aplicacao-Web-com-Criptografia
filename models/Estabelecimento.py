from setup.loaders.database import db
from sqlalchemy import inspect, text

DB_PASSPHRASE = "senha-secreta" 

class EstabelecimentoModel(db.Model):
    __table_args__ = {'extend_existing': True} 

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
    
    @classmethod
    def get_by_id_decrypted(cls, estabelecimento_id: int):
        
        sql_command = text("CALL sp_get_estab_by_id(:id_param, :passphrase_param)")
        
        params = {
            "id_param": estabelecimento_id,
            "passphrase_param": DB_PASSPHRASE 
        }

        try:
            # Executa a procedure
            resultado = db.session.execute(sql_command, params).mappings().one_or_none()
            db.session.close() 
            return resultado

        except Exception as e:
            print(f"ERRO: Falha ao executar a SP sp_get_estab_by_id: {e}")
            db.session.rollback()
            return None

    @classmethod
    def get_all_decrypted(cls):
        sql_command = text("CALL sp_get_all_estab(:passphrase_param)")
        params = {"passphrase_param": DB_PASSPHRASE}
        
        try:
            resultados = db.session.execute(sql_command, params).mappings().all()
            db.session.close()
            return resultados
            
        except Exception as e:
            print(f"ERRO: Falha ao executar a SP sp_get_all_estab: {e}")
            db.session.rollback()
            return []
