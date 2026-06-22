# Gestion des Étudiants — API (Sprint 1)

API de découverte construite avec **FastAPI** dans le cadre du Sprint 1 (Découverte de FastAPI).

## Objectif

Première prise en main de FastAPI : création d'une application, de routes simples et dynamiques, et test via Swagger.

## Technologies

- FastAPI
- Uvicorn

## Installation

```bash
# Créer l'environnement virtuel
python -m venv env

# Activer l'environnement
# Windows :
env\Scripts\activate
# Linux / Mac :
source env/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## Lancement

```bash
uvicorn main:app --reload
```

L'API est ensuite accessible sur http://127.0.0.1:8000

## Routes disponibles

| Méthode | Route | Description | Exemple |
|---------|-------|-------------|---------|
| GET | `/` | Message de bienvenue | http://127.0.0.1:8000/ |
| GET | `/bonjour` | Salutation simple | http://127.0.0.1:8000/bonjour |
| GET | `/bonjour/{nom}` | Salutation personnalisée | http://127.0.0.1:8000/bonjour/Ali |
| GET | `/addition/{a}/{b}` | Addition de deux entiers | http://127.0.0.1:8000/addition/10/20 |

## Documentation interactive (Swagger)

Disponible automatiquement sur http://127.0.0.1:8000/docs