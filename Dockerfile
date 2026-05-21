# ── Image de base : Python 3.11 allégée ──────────────────────────
FROM python:3.11-slim

# ── Répertoire de travail dans le conteneur ───────────────────────
WORKDIR /app

# ── Copier requirements en PREMIER (optimise le cache Docker) ─────
# Si le code change mais pas les dépendances, Docker ne réinstalle pas tout
COPY requirements.txt .

# ── Installer les dépendances sans cache (image plus légère) ──────
RUN pip install --no-cache-dir -r requirements.txt

# ── Copier tout le reste du code ──────────────────────────────────
COPY . .

# ── Port exposé par FastAPI ───────────────────────────────────────
EXPOSE 8000

# ── Commande de démarrage avec rechargement automatique ───────────
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]