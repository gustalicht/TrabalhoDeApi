from sqlalchemy import Column, Integer, String
from data.database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    height = Column(Integer)
    weight = Column(Integer)
    base_experience = Column(Integer)
