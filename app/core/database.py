# Gestion de la connexion PostgreSQL via SQLAlchemy 2.x
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


# Moteur de connexion — echo=False en prod, mettre True pour déboguer les requêtes SQL
engine = create_engine(settings.database_url, echo=False)

# Fabrique de sessions : chaque requête HTTP obtient sa propre session indépendante
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Classe de base dont héritent tous les modèles SQLAlchemy."""
    pass


def get_db():
    """
    Dépendance FastAPI injectée dans les routes via Depends(get_db).
    Garantit que la session est toujours fermée après chaque requête,
    même en cas d'exception.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()