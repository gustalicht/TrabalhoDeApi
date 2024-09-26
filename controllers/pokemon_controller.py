from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data.database import SessionLocal, init_db
from services.pokemon_service import fetch_pokemon_from_api, save_pokemon
from data.repository import get_pokemons

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pokemons/")
def read_pokemons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pokemons = get_pokemons(db, skip=skip, limit=limit)
    return pokemons

@router.post("/pokemons/fetch/{pokemon_name}")
def fetch_and_save_pokemon(pokemon_name: str, db: Session = Depends(get_db)):
    pokemon_data = fetch_pokemon_from_api(pokemon_name)
    save_pokemon(db, pokemon_data)
    return {"message": f"Pokemon {pokemon_name} fetched and saved successfully"}
