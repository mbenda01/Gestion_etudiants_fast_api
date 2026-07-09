from fastapi import FastAPI, HTTPException
from schemas import Etudiant, EtudiantUpdate, EtudiantOut
import data

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


# --- Sprint 3 : CRUD en mémoire sur /etudiants ---

# Partie 3 — Ajouter un étudiant (Create)
@app.post("/etudiants", response_model=EtudiantOut)
def creer_etudiant(etudiant: Etudiant):
    nouvel_etudiant = etudiant.model_dump()
    nouvel_etudiant["id"] = data.prochain_id
    data.etudiants.append(nouvel_etudiant)
    data.prochain_id += 1
    return nouvel_etudiant


# Partie 4 — Lister tous les étudiants (Read)
@app.get("/etudiants", response_model=list[EtudiantOut])
def lister_etudiants():
    return data.etudiants


# Partie 5 — Rechercher un étudiant par id (Read)
@app.get("/etudiants/{id}", response_model=EtudiantOut)
def obtenir_etudiant(id: int):
    for etudiant in data.etudiants:
        if etudiant["id"] == id:
            return etudiant
    raise HTTPException(status_code=404, detail="Étudiant introuvable")


# Partie 6 — Modifier un étudiant (Update)
@app.put("/etudiants/{id}", response_model=EtudiantOut)
def modifier_etudiant(id: int, etudiant_maj: EtudiantUpdate):
    for etudiant in data.etudiants:
        if etudiant["id"] == id:
            etudiant["nom"] = etudiant_maj.nom
            etudiant["prenom"] = etudiant_maj.prenom
            etudiant["age"] = etudiant_maj.age
            etudiant["email"] = etudiant_maj.email
            etudiant["telephone"] = etudiant_maj.telephone
            return etudiant
    raise HTTPException(status_code=404, detail="Étudiant introuvable")


# Partie 7 — Supprimer un étudiant (Delete)
@app.delete("/etudiants/{id}")
def supprimer_etudiant(id: int):
    for etudiant in data.etudiants:
        if etudiant["id"] == id:
            data.etudiants.remove(etudiant)
            return {"message": f"Étudiant {id} supprimé avec succès"}
    raise HTTPException(status_code=404, detail="Étudiant introuvable")