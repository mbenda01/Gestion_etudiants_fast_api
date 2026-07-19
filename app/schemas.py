from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Etudiant(BaseModel):
    """Schéma utilisé pour la création (POST) : pas d'id, il est généré par la base."""
    nom: str = Field(..., min_length=2, description="Nom de l'étudiant (2 caractères minimum)")
    prenom: str = Field(..., min_length=2, description="Prénom de l'étudiant (2 caractères minimum)")
    age: int = Field(..., gt=0, description="Âge de l'étudiant (doit être strictement positif)")
    email: EmailStr = Field(..., description="Adresse email valide de l'étudiant")
    telephone: Optional[str] = Field(None, description="Numéro de téléphone (facultatif)")


class EtudiantUpdate(BaseModel):
    """Schéma utilisé pour la modification (PUT) : mêmes champs que Etudiant."""
    nom: str = Field(..., min_length=2, description="Nom de l'étudiant (2 caractères minimum)")
    prenom: str = Field(..., min_length=2, description="Prénom de l'étudiant (2 caractères minimum)")
    age: int = Field(..., gt=0, description="Âge de l'étudiant (doit être strictement positif)")
    email: EmailStr = Field(..., description="Adresse email valide de l'étudiant")
    telephone: Optional[str] = Field(None, description="Numéro de téléphone (facultatif)")


class EtudiantOut(Etudiant):
    """Schéma retourné au client : Etudiant + l'id généré par la base."""
    id: int = Field(..., description="Identifiant unique généré par PostgreSQL")

    class Config:
        from_attributes = True