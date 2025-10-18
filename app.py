from flask import Flask
from controllers.usuario import usuario_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bunda'
app.register_blueprint(usuario_bp, url_prefix = "")

if __name__ == '__main__':
    app.run(debug=True)