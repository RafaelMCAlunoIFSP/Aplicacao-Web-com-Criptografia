from flask import render_template, session, Blueprint
from models.Estabelecimento import EstabelecimentoModel

estabelecimento_model = EstabelecimentoModel()
bp = Blueprint('usuario', __name__)


def init():
    session['logado'] = False
    return session['logado']

@bp.route('/')
def bares():
    print(EstabelecimentoModel.get_all_decrypted())
    return render_template('estabelecimentos.html', lista_de_estabelecimentos = EstabelecimentoModel.get_all_decrypted())