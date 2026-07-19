from sqlalchemy.orm import Session

from app import models, schemas


def get_etudiant(db: Session, etudiant_id: int):
    return db.query(models.Etudiant).filter(models.Etudiant.id == etudiant_id).first()


def get_etudiants(db: Session):
    return db.query(models.Etudiant).all()


def create_etudiant(db: Session, etudiant: schemas.Etudiant):
    nouvel_etudiant = models.Etudiant(**etudiant.model_dump())
    db.add(nouvel_etudiant)
    db.commit()
    db.refresh(nouvel_etudiant)
    return nouvel_etudiant


def update_etudiant(db: Session, etudiant_id: int, etudiant_maj: schemas.EtudiantUpdate):
    etudiant_existant = get_etudiant(db, etudiant_id)
    if etudiant_existant is None:
        return None

    for champ, valeur in etudiant_maj.model_dump().items():
        setattr(etudiant_existant, champ, valeur)

    db.commit()
    db.refresh(etudiant_existant)
    return etudiant_existant


def delete_etudiant(db: Session, etudiant_id: int):
    etudiant_existant = get_etudiant(db, etudiant_id)
    if etudiant_existant is None:
        return None

    db.delete(etudiant_existant)
    db.commit()
    return etudiant_existant