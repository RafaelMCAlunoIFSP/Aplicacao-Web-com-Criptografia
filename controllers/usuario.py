from flask import render_template, request, redirect, url_for, session, Blueprint
from models.usuario import UsuarioModel

usuario_bp = Blueprint('usuario', __name__)

usuario_model = UsuarioModel()

def init():
    session['logado'] = False
    return session['logado']

@usuario_bp.route('/')
def homepage():
    if not session.get('logado'):
        init()
    if session['logado'] == False:
        return redirect(url_for('usuario.login'))
    else:
        return render_template('homepage.html')
    
@usuario_bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        for usuario in usuario_model._usuarios:
            print(usuario)
            if nome == usuario['nome'] and email == usuario['email'] and senha == usuario['senha']:
                session['logado'] = True
                return redirect(url_for('usuario.homepage'))
            
@usuario_bp.route('/usuarios')
def listar_usuarios():
    # 1. Controle pede os dados ao Modelo.
    # 2. Modelo retorna a lista de usuários.
    # 3. Controle entrega a lista para a Visão renderizar.

    usuarios = usuario_model.get_todos()
    return render_template('usuarios.html', lista_de_usuarios = usuarios)

@usuario_bp.route('/usuarios/novo', methods=['POST'])
def adicionar_usuario():
    # 1. Controle recebe os dados do formulário (enviados pela Visão);
    # 2. Controle pede para o Modelo salvar os novos dados.
    # 3. Controle redireciona o usuário para a página principal.

    nome = request.form['nome']
    email = request.form['email']
    usuario_model.salvar(nome, email)
    return redirect(url_for('usuario.listar_usuarios'))