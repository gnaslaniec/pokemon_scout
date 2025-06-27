from .database import SessionLocal
from .models import Pokemon
from . import pokeapi, processor
from config import DEFAULT_POKEMONS


def fetch_initial_pokemons():
    session = SessionLocal()
    for name in DEFAULT_POKEMONS:
        name = name.lower()
        if session.query(Pokemon).filter_by(name=name).first():
            continue
        try:
            data = pokeapi.fetch_pokemon_data(name)
            cleaned = processor.sanitize_pokemon_data(data)
            pokemon = Pokemon(**cleaned)
            session.add(pokemon)
        except Exception as e:
            print(f"[Init Fetch] Failed to fetch {name}: {e}")
    session.commit()
    session.close()
