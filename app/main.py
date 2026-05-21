# Point d'entrée principal de l'application FastAPI — Tortiki
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Instanciation de l'application avec métadonnées pour Swagger
app = FastAPI(
    title="Tortiki API",
    description="Marketplace P2P de plats cuisinés maison — Projet CDA 2026",
    version="0.1.0",
    docs_url="/docs",    # Interface Swagger UI
    redoc_url="/redoc",  # Interface ReDoc alternative
)

# Middleware CORS : autorise les requêtes cross-origin depuis le navigateur
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Système"])
def health_check():
    """
    Point de contrôle de l'API.
    Utilisé par Docker et les outils de monitoring pour vérifier
    que l'application est opérationnelle.
    """
    return {"status": "ok", "service": "Tortiki API", "version": "0.1.0"}