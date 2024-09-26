import sys
import os
import requests
from sqlalchemy.orm import Session

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from data.database import SessionLocal, init_db
from services.pokemon_service import save_pokemon



POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_pokemon_from_api(pokemon_id: int):
    response = requests.get(f"{POKEMON_API_URL}/{pokemon_id}")
    return response.json()

def populate_database(db: Session, num_pokemons: int):
    for pokemon_id in range(1, num_pokemons + 1):
        pokemon_data = fetch_pokemon_from_api(pokemon_id)
        save_pokemon(db, pokemon_data)
        print(f"Pokémon {pokemon_data['name']} (ID: {pokemon_id}) salvo com sucesso.")

if __name__ == "__main__":
    init_db()  # Inicializa o banco de dados
    db = SessionLocal()
    try:
        populate_database(db, 500)
    finally:
        db.close()
