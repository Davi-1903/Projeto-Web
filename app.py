from flask import Flask, render_template
from controllers.auth import auth_bp
from config import config_app


app = Flask(__name__)
config_app(app)

app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return render_template('index.html')