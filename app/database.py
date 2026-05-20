from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

# ── Engine ────────────────────────────────────────────────────────────────────
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,       # verifica la conexión antes de usarla
    pool_size=10,             # conexiones simultáneas en el pool
    max_overflow=20,          # conexiones extra permitidas bajo carga
)

# ── Sesión ────────────────────────────────────────────────────────────────────
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

# ── Base declarativa — todos los modelos la heredan ───────────────────────────
Base = declarative_base()


# ── Dependency para FastAPI ───────────────────────────────────────────────────
# Usala en los routers con: db: Session = Depends(get_db)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
