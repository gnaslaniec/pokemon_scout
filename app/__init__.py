from flask import Flask
from .database import init_db
from .routes import bp
from .init_fetch import fetch_initial_pokemons


def create_app():
    app = Flask(__name__)
    init_db()
    fetch_initial_pokemons()
    app.register_blueprint(bp)
    return app
