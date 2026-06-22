from fastapi import FastAPI

# Création de l'application FastAPI
app = FastAPI()


# Partie 3 — Route racine
# GET /  -> message de bienvenue
@app.get("/")
def racine():
    return {"message": "Bienvenue dans mon API"}


# Partie 4 — Deuxième route
# GET /bonjour -> message fixe
@app.get("/bonjour")
def bonjour():
    return {"message": "Bonjour à tous"}


# Partie 5 — Route dynamique avec un paramètre
# GET /bonjour/{nom} -> /bonjour/Ali renvoie "Bonjour Ali"
@app.get("/bonjour/{nom}")
def bonjour_nom(nom: str):
    return {"message": f"Bonjour {nom}"}


# Partie 6 — Route avec plusieurs paramètres (typés en int)
# GET /addition/{a}/{b} -> /addition/10/20 renvoie 30
@app.get("/addition/{a}/{b}")
def addition(a: int, b: int):
    return {"resultat": a + b}