from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/etudiants", tags=["Étudiants"])


@router.post("", response_model=schemas.EtudiantOut)
def creer_etudiant(etudiant: schemas.Etudiant, db: Session = Depends(get_db)):
    return crud.create_etudiant(db, etudiant)


@router.get("", response_model=list[schemas.EtudiantOut])
def lister_etudiants(db: Session = Depends(get_db)):
    return crud.get_etudiants(db)


@router.get("/{id}", response_model=schemas.EtudiantOut)
def obtenir_etudiant(id: int, db: Session = Depends(get_db)):
    etudiant = crud.get_etudiant(db, id)
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    return etudiant


@router.put("/{id}", response_model=schemas.EtudiantOut)
def modifier_etudiant(id: int, etudiant_maj: schemas.EtudiantUpdate, db: Session = Depends(get_db)):
    etudiant = crud.update_etudiant(db, id, etudiant_maj)
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    return etudiant


@router.delete("/{id}")
def supprimer_etudiant(id: int, db: Session = Depends(get_db)):
    etudiant = crud.delete_etudiant(db, id)
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    return {"message": f"Étudiant {id} supprimé avec succès"}