from unittest.mock import patch

sample_pikachu = {
    "name": "pikachu",
    "height": 4,
    "weight": 60,
    "base_experience": 112,
    "types": [{"slot": 1, "type": {"name": "electric"}}],
    "abilities": [
        {"ability": {"name": "static"}, "is_hidden": False, "slot": 1},
        {"ability": {"name": "lightning-rod"}, "is_hidden": True, "slot": 3},
    ],
    "stats": [
        {"base_stat": 35, "effort": 0, "stat": {"name": "hp"}},
        {"base_stat": 55, "effort": 0, "stat": {"name": "attack"}},
        {"base_stat": 40, "effort": 0, "stat": {"name": "defense"}},
        {"base_stat": 50, "effort": 0, "stat": {"name": "special-attack"}},
        {"base_stat": 50, "effort": 0, "stat": {"name": "special-defense"}},
        {"base_stat": 90, "effort": 2, "stat": {"name": "speed"}},
    ],
}


@patch("app.routes.pokeapi.fetch_pokemon_data")
def test_scout_adds_new_pokemon(mock_fetch, client):
    mock_fetch.return_value = sample_pikachu
    res = client.post("/scout/pikachu")
    assert res.status_code == 201
    assert res.json["status"] == "added"


@patch("app.routes.pokeapi.fetch_pokemon_data")
def test_scout_duplicate_pokemon(mock_fetch, client):
    mock_fetch.return_value = sample_pikachu
    client.post("/scout/pikachu")
    res = client.post("/scout/pikachu")
    assert res.status_code == 200
    assert res.json["status"] == "already_exists"


@patch("app.routes.pokeapi.fetch_pokemon_data")
def test_get_existing_pokemon(mock_fetch, client):
    mock_fetch.return_value = sample_pikachu
    client.post("/scout/pikachu")
    res = client.get("/pokemon/pikachu")
    assert res.status_code == 200
    assert res.json["name"] == "pikachu"
    assert res.json["types"] == "electric"
    assert res.json["abilities"] == "static, lightning-rod"
    assert res.json["speed"] == 90


def test_get_nonexistent_pokemon(client):
    res = client.get("/pokemon/missingno")
    assert res.status_code == 404
    assert res.json["error"] == "Pokémon 'missingno' not found"
