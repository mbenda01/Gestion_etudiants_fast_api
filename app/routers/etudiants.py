from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/etudiants", tags=["Étudiants"])


# Partie 3 — Ajouter un étudiant (Create)
@router.post(
    "",
    response_model=schemas.EtudiantOut,
    summary="Créer un étudiant",
    description="Ajoute un nouvel étudiant en base de données. L'id est généré automatiquement par PostgreSQL.",
)
def creer_etudiant(etudiant: schemas.Etudiant, db: Session = Depends(get_db)):
    return crud.create_etudiant(db, etudiant)


# Partie 3 — Lister tous les étudiants (Read)
@router.get(
    "",
    response_model=list[schemas.EtudiantOut],
    summary="Lister les étudiants",
    description="Retourne la liste complète des étudiants enregistrés en base.",
)
def lister_etudiants(db: Session = Depends(get_db)):
    return crud.get_etudiants(db)


# Partie 3 — Rechercher un étudiant par id (Read)
@router.get(
    "/{id}",
    response_model=schemas.EtudiantOut,
    summary="Obtenir un étudiant",
    description="Recherche un étudiant par son identifiant. Retourne 404 si l'étudiant n'existe pas.",
)
def obtenir_etudiant(
    id: int = Path(..., gt=0, description="Identifiant de l'étudiant (entier positif)"),
    db: Session = Depends(get_db),
):
    etudiant = crud.get_etudiant(db, id)
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    return etudiant


# Partie 3 — Modifier un étudiant (Update)
@router.put(
    "/{id}",
    response_model=schemas.EtudiantOut,
    summary="Modifier un étudiant",
    description="Met à jour l'ensemble des champs d'un étudiant existant. Retourne 404 si l'étudiant n'existe pas.",
)
def modifier_etudiant(
    etudiant_maj: schemas.EtudiantUpdate,
    id: int = Path(..., gt=0, description="Identifiant de l'étudiant (entier positif)"),
    db: Session = Depends(get_db),
):
    etudiant = crud.update_etudiant(db, id, etudiant_maj)
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    return etudiant


# Partie 3 — Supprimer un étudiant (Delete)
@router.delete(
    "/{id}",
    summary="Supprimer un étudiant",
    description="Supprime un étudiant existant. Retourne 404 si l'étudiant n'existe pas.",
)
def supprimer_etudiant(
    id: int = Path(..., gt=0, description="Identifiant de l'étudiant (entier positif)"),
    db: Session = Depends(get_db),
):
    etudiant = crud.delete_etudiant(db, id)
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    return {"message": f"Étudiant {id} supprimé avec succès"}