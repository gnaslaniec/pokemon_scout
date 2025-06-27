import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
POKEMON_LIST_PATH = BASE_DIR / "data" / "default_pokemons.json"

try:
    with open(POKEMON_LIST_PATH, "r") as f:
        DEFAULT_POKEMONS = json.load(f)
except Exception as e:
    print(f"[Config] Failed to load default pokemons: {e}")
    DEFAULT_POKEMONS = []
