# Configuration centralisée — lecture des variables d'environnement via Pydantic
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Paramètres de l'application lus automatiquement depuis le fichier .env.
    Si une variable obligatoire est absente, l'application refuse de démarrer.
    """

    # Connexion base de données
    database_url: str

    # Authentification JWT
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15

    class Config:
        env_file = ".env"


# Instance unique partagée dans toute l'application (pattern Singleton)
settings = Settings()