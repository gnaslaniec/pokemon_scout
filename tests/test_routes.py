def test_scout_new_pokemon(client):
    res = client.post("/scout/pikachu")
    assert res.status_code == 200
    assert res.json["status"] in ["added", "already_exists"]


def test_get_existing_pokemon(client):
    client.post("/scout/pikachu")
    res = client.get("/pokemon/pikachu")
    assert res.status_code == 200
    assert res.json["name"] == "pikachu"
    assert "speed" in res.json


def test_get_nonexistent_pokemon(client):
    res = client.get("/pokemon/missingno")
    assert res.status_code == 404
    assert res.json["error"] == "Pokémon 'missingno' not found"
