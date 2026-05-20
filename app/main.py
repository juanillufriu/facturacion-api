from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.database import Base, engine


# ── Lifespan: se ejecuta al arrancar y al cerrar la app ──────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: crear tablas si no existen (en dev está bien, en prod usá Alembic)
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown: acá iría el cierre de conexiones si fuera necesario


# ── Instancia principal ───────────────────────────────────────────────────────
app = FastAPI(
    title="Sistema de Facturación API",
    description="API REST para gestión de clientes, productos y facturas con generación de PDF.",
    version="1.0.0",
    contact={
        "name": "Juan Ignacio Llufriu",
        "url": "https://github.com/juanillufriu",
    },
    lifespan=lifespan,
)


# ── CORS ─────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # En producción reemplazá con tu dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Manejo global de errores ──────────────────────────────────────────────────
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Error interno del servidor.",
            "type": type(exc).__name__,
        },
    )


# ── Routers (los vas agregando a medida que los creás) ───────────────────────
# from app.routers import auth, clients, products, invoices
# app.include_router(auth.router,     prefix="/api/auth",     tags=["Auth"])
# app.include_router(clients.router,  prefix="/api/clients",  tags=["Clients"])
# app.include_router(products.router, prefix="/api/products", tags=["Products"])
# app.include_router(invoices.router, prefix="/api/invoices", tags=["Invoices"])


# ── Endpoints base ────────────────────────────────────────────────────────────
@app.get("/", tags=["Health"])
def root():
    return {
        "status": "online",
        "app": "Sistema de Facturación API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
