from flask import Flask
from .database import init_db
from .routes import bp

from .init_fetch import fetch_initial_pokemons


def create_app(testing=False):
    app = Flask(__name__)
    init_db()
    if not testing:
        fetch_initial_pokemons()
    app.register_blueprint(bp)
    return app
