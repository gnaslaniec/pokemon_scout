from pydantic import BaseModel
from typing import List, Dict


class Ability(BaseModel):
    ability: Dict[str, str]


class Type(BaseModel):
    type: Dict[str, str]


class Stat(BaseModel):
    base_stat: int
    stat: Dict[str, str]


class RawPokemon(BaseModel):
    name: str
    height: int
    weight: int
    base_experience: int
    types: List[Type]
    abilities: List[Ability]
    stats: List[Stat]


class SanitizedPokemon(BaseModel):
    name: str
    height: int
    weight: int
    base_experience: int
    types: str
    abilities: str
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


def sanitize_pokemon_data(raw_json: dict) -> dict:
    raw = RawPokemon.model_validate(raw_json)

    stats_map = {s.stat["name"]: s.base_stat for s in raw.stats}

    return SanitizedPokemon(
        name=raw.name.lower(),
        height=raw.height,
        weight=raw.weight,
        base_experience=raw.base_experience,
        types=", ".join(t.type["name"] for t in raw.types),
        abilities=", ".join(a.ability["name"] for a in raw.abilities),
        hp=stats_map.get("hp", 0),
        attack=stats_map.get("attack", 0),
        defense=stats_map.get("defense", 0),
        special_attack=stats_map.get("special-attack", 0),
        special_defense=stats_map.get("special-defense", 0),
        speed=stats_map.get("speed", 0),
    ).model_dump()
