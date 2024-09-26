import requests
from sqlalchemy.orm import Session
from models.pokemon import Pokemon
from data.repository import create_pokemon

POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_pokemon_from_api(pokemon_name: str):
    response = requests.get(f"{POKEMON_API_URL}/{pokemon_name}")
    return response.json()

def save_pokemon(db: Session, pokemon_data: dict):
    pokemon = Pokemon(
        name=pokemon_data.get("name"),
        height=pokemon_data.get("height"),
        weight=pokemon_data.get("weight"),
        base_experience=pokemon_data.get("base_experience")
    )
    create_pokemon(db, pokemon)
