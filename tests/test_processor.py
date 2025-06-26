import json
from app.processor import sanitize_pokemon_data


def test_sanitize_valid_pokemon():
    with open("tests/sample_pikachu.json") as f:
        sample_data = json.load(f)

    result = sanitize_pokemon_data(sample_data)

    assert result["name"] == "pikachu"
    assert result["types"] == "electric"
    assert result["abilities"] == "static"
    assert result["hp"] == 35
    assert result["attack"] == 55
    assert result["defense"] == 40
    assert result["special_attack"] == 50
    assert result["special_defense"] == 50
    assert result["speed"] == 90
