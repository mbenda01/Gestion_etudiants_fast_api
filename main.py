from fastapi import FastAPI
from schemas import Etudiant

# Création de l'application FastAPI
app = FastAPI()


# --- Sprint 1 : routes GET ---

# Partie 3 — Route racine
@app.get("/")
def racine():
    return {"message": "Bienvenue dans mon API"}


# Partie 4 — Deuxième route
@app.get("/bonjour")
def bonjour():
    return {"message": "Bonjour à tous"}


# Partie 5 — Route dynamique avec un paramètre
@app.get("/bonjour/{nom}")
def bonjour_nom(nom: str):
    return {"message": f"Bonjour {nom}"}


# Partie 6 — Route avec plusieurs paramètres
@app.get("/addition/{a}/{b}")
def addition(a: int, b: int):
    return {"resultat": a + b}


# --- Sprint 2 : route POST ---

# Partie 4 du Sprint 2 — Créer un étudiant
@app.post("/etudiants")
def creer_etudiant(etudiant: Etudiant):
    return {
        "message": "Étudiant créé avec succès",
        "etudiant": etudiant
    }