from pydantic import BaseModel
from typing import Optional


class Etudiant(BaseModel):
    nom: str
    prenom: str
    age: int
    email: str
    telephone: Optional[str] = None