from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import Etudiant, EtudiantUpdate, EtudiantOut
from database import engine, get_db, Base
import models

# Crée la table "etudiants" dans PostgreSQL,
# à partir du modèle SQLAlchemy défini dans models.py.
Base.metadata.create_all(bind=engine)

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


# --- Sprint 4/5 : CRUD sur PostgreSQL (via SQLAlchemy) sur /etudiants ---

# Partie 3 — Ajouter un étudiant (Create)
@app.post("/etudiants", response_model=EtudiantOut)
def creer_etudiant(etudiant: Etudiant, db: Session = Depends(get_db)):
    nouvel_etudiant = models.Etudiant(**etudiant.model_dump())
    db.add(nouvel_etudiant)
    db.commit()
    db.refresh(nouvel_etudiant)
    return nouvel_etudiant


# Partie 4 — Lister tous les étudiants (Read)
@app.get("/etudiants", response_model=list[EtudiantOut])
def lister_etudiants(db: Session = Depends(get_db)):
    return db.query(models.Etudiant).all()


# Partie 5 — Rechercher un étudiant par id (Read)
@app.get("/etudiants/{id}", response_model=EtudiantOut)
def obtenir_etudiant(id: int, db: Session = Depends(get_db)):
    etudiant = db.query(models.Etudiant).filter(models.Etudiant.id == id).first()
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    return etudiant


# Partie 6 — Modifier un étudiant (Update)
@app.put("/etudiants/{id}", response_model=EtudiantOut)
def modifier_etudiant(id: int, etudiant_maj: EtudiantUpdate, db: Session = Depends(get_db)):
    etudiant = db.query(models.Etudiant).filter(models.Etudiant.id == id).first()
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    etudiant.nom = etudiant_maj.nom
    etudiant.prenom = etudiant_maj.prenom
    etudiant.age = etudiant_maj.age
    etudiant.email = etudiant_maj.email
    etudiant.telephone = etudiant_maj.telephone
    db.commit()
    db.refresh(etudiant)
    return etudiant


# Partie 7 — Supprimer un étudiant (Delete)
@app.delete("/etudiants/{id}")
def supprimer_etudiant(id: int, db: Session = Depends(get_db)):
    etudiant = db.query(models.Etudiant).filter(models.Etudiant.id == id).first()
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    db.delete(etudiant)
    db.commit()
    return {"message": f"Étudiant {id} supprimé avec succès"}