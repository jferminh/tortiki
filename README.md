# Tortiki 🍲
🍜 Marketplace P2P de plats faits maison — Projet CDA 2026

## Stack technique

| Couche | Technologie |
|--------|------------|
| Backend | Python 3.11 / FastAPI |
| Base de données | MySQL 8 + SQLAlchemy 2 + Alembic |
| Authentification | JWT + bcrypt |
| Déploiement | Docker + Render/Railway |

## Lancer le projet en local

```bash
docker-compose up --build
```

## Accès Swagger (documentation API)

http://localhost:8000/docs