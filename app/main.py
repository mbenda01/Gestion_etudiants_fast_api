from fastapi import FastAPI

from app.routers import etudiants

app = FastAPI(
    title="Gestion des Étudiants API",
    description=(
        "API REST permettant de gérer des étudiants (création, consultation, "
        "modification, suppression), construite avec FastAPI, Pydantic, "
        "SQLAlchemy et PostgreSQL, avec des migrations gérées par Alembic."
    ),
    version="1.0.0",
)


# --- Sprint 1 : routes GET ---

# Partie 3 — Route racine
@app.get("/", summary="Message de bienvenue", description="Route de test renvoyant un message de bienvenue.")
def racine():
    return {"message": "Bienvenue dans mon API"}


# Partie 4 — Deuxième route
@app.get("/bonjour", summary="Salutation simple", description="Route de test renvoyant une salutation générique.")
def bonjour():
    return {"message": "Bonjour à tous"}


# Partie 5 — Route dynamique avec un paramètre
@app.get("/bonjour/{nom}", summary="Salutation personnalisée", description="Renvoie une salutation personnalisée avec le nom passé en paramètre.")
def bonjour_nom(nom: str):
    return {"message": f"Bonjour {nom}"}


# Partie 6 — Route avec plusieurs paramètres
@app.get("/addition/{a}/{b}", summary="Addition de deux entiers", description="Route de test additionnant deux entiers passés en paramètres.")
def addition(a: int, b: int):
    return {"resultat": a + b}


# --- Sprint 4 à 8 : CRUD sur PostgreSQL (via SQLAlchemy), schéma géré par Alembic ---
app.include_router(etudiants.router)