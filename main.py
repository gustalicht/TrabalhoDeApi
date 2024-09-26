from fastapi import FastAPI
from controllers.pokemon_controller import router as pokemon_router
from data.database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(pokemon_router, prefix="/api/v1")
