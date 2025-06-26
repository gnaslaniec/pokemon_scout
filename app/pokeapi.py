import requests


def fetch_pokemon_data(name):
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name.lower()}",
    )
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch {name}")
    return response.json()
