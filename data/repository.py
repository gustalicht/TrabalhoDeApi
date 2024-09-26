from sqlalchemy.orm import Session
from models.pokemon import Pokemon

def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pokemon).offset(skip).limit(limit).all()

def create_pokemon(db: Session, pokemon: Pokemon):
    db.add(pokemon)
    db.commit()
    db.refresh(pokemon)
    return pokemon
