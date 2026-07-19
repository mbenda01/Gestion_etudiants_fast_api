from fastapi import FastAPI

from app.routers import etudiants

app = FastAPI()


@app.get("/")
def racine():
    return {"message": "Bienvenue dans mon API"}


@app.get("/bonjour")
def bonjour():
    return {"message": "Bonjour à tous"}


@app.get("/bonjour/{nom}")
def bonjour_nom(nom: str):
    return {"message": f"Bonjour {nom}"}


@app.get("/addition/{a}/{b}")
def addition(a: int, b: int):
    return {"resultat": a + b}


app.include_router(etudiants.router)