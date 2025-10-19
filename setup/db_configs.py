"""
 explicando a URI pra configurar depois se necessário ( baseado no exemplo abaixo):
 
 Exemplo:   mysql+pymysql://root@localhost:3306/bares

 mysql é o tipo do banco, pymysql é a bilbioteca py que faz a conexão ( o sqlalchemy não faz a conexão, o driver que faz!)
 root - nome do usuario que ta acessando o banco ( nesse caso root é o usuario admin por padrão)
 @localhost - indica qual é o host que ta querendo acessar o banco ( nesse caso como o host é o meu proprio pc, uso localhost
 3306 - a porta em que ta sendo acessado
 /bares - esquema do bdd que to acessando )
"""
DATABASE_URI = "mysql+pymysql://root@localhost:3306/bares" 
TRACK_MODIFICATIONS = False
