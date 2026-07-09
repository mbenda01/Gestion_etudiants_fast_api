from pydantic import BaseModel
from typing import Optional


class Etudiant(BaseModel):
    """Schéma utilisé pour la création (POST) : pas d'id, il est généré par le serveur."""
    nom: str
    prenom: str
    age: int
    email: str
    telephone: Optional[str] = None


class EtudiantUpdate(BaseModel):
    """Schéma utilisé pour la modification (PUT) : mêmes champs que Etudiant."""
    nom: str
    prenom: str
    age: int
    email: str
    telephone: Optional[str] = None


class EtudiantOut(Etudiant):
    """Schéma retourné au client : Etudiant + l'id généré par le serveur."""
    id: int