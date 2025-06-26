from sqlalchemy import Column, Integer, String
from .database import Base


class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    height = Column(Integer)
    weight = Column(Integer)
    base_experience = Column(Integer)
    types = Column(String)
    abilities = Column(String)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    special_attack = Column(Integer)
    special_defense = Column(Integer)
    speed = Column(Integer)
