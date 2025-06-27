# Pokémon Scout

A lightweight Flask-based scouting tool that fetches Pokémon data from the [PokeAPI](https://pokeapi.co/), sanitizes it according to scouting logic, and stores it in a local SQLite database.

## Features

- Retrieve Pokémon data via PokeAPI
- Sanitize and format key scouting attributes (type, abilities, base stats, etc.)
- Store results in a local SQLite database using SQLAlchemy
- REST API with Flask to trigger scouting and fetch stored Pokémon
- Supports initial list and dynamic additions via POST

## Main Libraries Used

| Library        | Purpose                                        |
| -------------- | ---------------------------------------------- |
| **Flask**      | Web framework for building the API             |
| **SQLAlchemy** | ORM for managing SQLite database interactions  |
| **Pydantic**   | Data validation and parsing (for Pokémon data) |
| **Requests**   | HTTP client to interact with the PokeAPI       |
| **Pytest**     | Test framework for writing and running tests   |


## Installation

1. **Clone the repo**

```bash
git clone https://github.com/gnaslaniec/pokemon_scout.git
cd pokemon_scout
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
make install
```

4. **Run the app**

```bash
make run
```

App runs on `http://localhost:5000`

---

## Running Tests

```bash
make test
```

All tests use a in-memory SQLite database.

---

## API Endpoints

### `POST /scout/<name>`

Fetch and store Pokémon data by name.

- **Example:** `POST /scout/pikachu`
- **Returns:**
```json
{ "status": "added" }
```

If the Pokémon is already in the DB:
```json
{ "status": "already_exists" }
```

---

### `GET /pokemon/<name>`

Retrieve a Pokémon’s stored data from the local DB.

- **Example:** `GET /pokemon/charizard`
- **Returns:**
```json
{
  "abilities": "blaze, solar-power",
  "attack": 84,
  "base_experience": 240,
  "defense": 78,
  "height": 17,
  "hp": 78,
  "name": "charizard",
  "special_attack": 109,
  "special_defense": 85,
  "speed": 100,
  "types": "fire, flying",
  "weight": 905
}
```

---

### `GET /pokemons`

Retrieve all Pokémon’s stored on the local DB.

- **Example:** `GET /pokemons`
- **Returns:**
```json
[
    {
        "name": "charizard",
        "types": ["fire", "flying"],
        "abilities": ["blaze"],
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "special_attack": 109,
        "special_defense": 85,
        "speed": 100
    },
    {
        "abilities": "static, lightning-rod",
        "attack": 55,
        "base_experience": 112,
        "defense": 40,
        "height": 4,
        "hp": 35,
        "name": "pikachu",
        "special_attack": 50,
        "special_defense": 50,
        "speed": 90,
        "types": "electric",
        "weight": 60
    }
]
```

If not found:
```json
{ "error": "Pokémon 'missigno' not found" }
```

---

## How to Add New Pokémon

You can dynamically scout any new Pokémon using the POST endpoint:

```bash
curl -X POST http://localhost:5000/scout/gengar
```

Alternatively, you can add a Pokémon to the default scouting list located in data/default_pokemons.json. These Pokémon are automatically fetched and stored in the database when the application initializes.