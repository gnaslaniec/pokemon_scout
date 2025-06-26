def test_scout_new_pokemon(client):
    res = client.post("/scout/pikachu")
    assert res.status_code == 200
    assert res.json["status"] == "added"


def test_scout_duplicate_pokemon(client):
    client.post("/scout/pikachu")
    res = client.post("/scout/pikachu")
    assert res.status_code == 200
    assert res.json["status"] == "already_exists"


def test_get_existing_pokemon(client):
    client.post("/scout/charizard")
    res = client.get("/pokemon/charizard")
    assert res.status_code == 200
    assert res.json["name"] == "charizard"


def test_get_nonexistent_pokemon(client):
    res = client.get("/pokemon/missingno")
    assert res.status_code == 404
    assert "not found" in res.json["error"]
