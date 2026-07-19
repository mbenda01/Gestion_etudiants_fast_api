# Gestion des Étudiants — API

API REST permettant de gérer des étudiants (création, consultation, modification, suppression), construite avec **FastAPI**, **Pydantic**, **SQLAlchemy** et **PostgreSQL**, avec des migrations gérées par **Alembic**.

## Objectifs du projet

Ce projet a été développé de façon progressive, sprint après sprint, avec pour objectifs :

- construire une API REST complète avec FastAPI (routes GET, POST, PUT, DELETE) ;
- valider rigoureusement les données reçues avec Pydantic (formats, contraintes) ;
- persister les données dans une vraie base de données relationnelle (PostgreSQL) via l'ORM SQLAlchemy ;
- gérer l'évolution du schéma de la base de données de façon versionnée avec Alembic ;
- organiser le code selon une architecture professionnelle en couches (routes / logique métier / modèles / schémas) ;
- documenter et livrer une API prête à être utilisée par une autre équipe.

## Technologies utilisées

| Technologie | Rôle |
|---|---|
| **FastAPI** | Framework web pour construire l'API et ses routes |
| **Pydantic** | Validation et sérialisation des données échangées |
| **SQLAlchemy** | ORM pour manipuler PostgreSQL sans écrire de SQL à la main |
| **PostgreSQL** | Base de données relationnelle (exécutée dans Docker) |
| **Alembic** | Gestion versionnée des migrations du schéma |
| **Docker** | Conteneurisation de PostgreSQL (installé via WSL, sans Docker Desktop) |
| **Uvicorn** | Serveur ASGI exécutant l'application |

## Structure du projet