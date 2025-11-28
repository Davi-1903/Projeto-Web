from flask import Flask, render_template
from controllers.auth import auth_bp
from controllers.sugestao import sugestoes_bp
from controllers.user import user_bp
from config import config_app


app = Flask(__name__)
config_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(sugestoes_bp)
app.register_blueprint(user_bp)


@app.route('/')
def index():
    return render_template('index.html')