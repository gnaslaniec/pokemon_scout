import json
import os
from app.processor import sanitize_pokemon_data


def test_sanitize_valid_pokemon():
    test_path = os.path.join(os.path.dirname(__file__), "sample_pikachu.json")
    with open(test_path, "r") as f:
        raw_data = json.load(f)

    result = sanitize_pokemon_data(raw_data)

    assert result["name"] == "pikachu"
    assert "electric" in result["types"]
    assert result["hp"] > 0
    assert isinstance(result["attack"], int)
    assert isinstance(result["special_attack"], int)
    assert "static" in result["abilities"]
