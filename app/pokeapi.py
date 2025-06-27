import requests


def fetch_pokemon_data(name):
    try:
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{name.lower()}",
            timeout=5,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise ValueError(
            "Request to PokeAPI timed out. The service may be unavailable. Please try again later."
        )
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch '{name}' from PokeAPI: {str(e)}")
