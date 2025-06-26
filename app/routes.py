from flask import Blueprint, jsonify
from .database import SessionLocal
from .models import Pokemon
from . import pokeapi, processor

bp = Blueprint("main", __name__)


@bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200


@bp.route("/pokemon/<string:pokemon_name>", methods=["GET"])
def get_pokemon(pokemon_name):
    session = SessionLocal()
    name = pokemon_name.lower()
    pokemon = session.query(Pokemon).filter_by(name=name).first()
    session.close()

    if not pokemon:
        return jsonify({"error": f"Pokémon '{name}' not found"}), 404

    return jsonify(
        {
            "name": pokemon.name,
            "height": pokemon.height,
            "weight": pokemon.weight,
            "base_experience": pokemon.base_experience,
            "types": pokemon.types,
            "abilities": pokemon.abilities,
            "hp": pokemon.hp,
            "attack": pokemon.attack,
            "defense": pokemon.defense,
            "special_attack": pokemon.special_attack,
            "special_defense": pokemon.special_defense,
            "speed": pokemon.speed,
        }
    )


@bp.route("/pokemons", methods=["GET"])
def get_pokemons():
    session = SessionLocal()
    pokemons = session.query(Pokemon).all()
    data = [
        {
            "name": p.name,
            "height": p.height,
            "weight": p.weight,
            "base_experience": p.base_experience,
            "types": p.types,
            "abilities": p.abilities,
            "hp": p.hp,
            "attack": p.attack,
            "defense": p.defense,
            "special_attack": p.special_attack,
            "special_defense": p.special_defense,
            "speed": p.speed,
        }
        for p in pokemons
    ]
    session.close()
    return jsonify(data)


@bp.route("/scout/<string:pokemon_name>", methods=["POST"])
def scout_pokemon(pokemon_name):
    session = SessionLocal()
    name = pokemon_name.lower()

    if session.query(Pokemon).filter_by(name=name).first():
        session.close()
        return jsonify({"name": name, "status": "already_exists"}), 200

    try:
        data = pokeapi.fetch_pokemon_data(name)
        cleaned = processor.sanitize_pokemon_data(data)
        pokemon = Pokemon(**cleaned)
        session.add(pokemon)
        session.commit()
        session.close()
        return jsonify({"name": name, "status": "added"}), 201
    except Exception as e:
        session.rollback()
        session.close()
        return jsonify({"name": name, "status": f"error: {str(e)}"}), 400
