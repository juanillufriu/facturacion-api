# facturacion-api

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /><img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white" /><img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=Pydantic&logoColor=white" /><img src="https://img.shields.io/badge/PyTest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" /><img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />

API RESTful para la gestión de facturación, desarrollada con **FastAPI** como proyecto de laboratorio. Este sistema permite administrar clientes, productos y facturas, con cálculos automáticos de subtotales, impuestos (IVA 21%) y totales, además de generar documentos PDF de las facturas utilizando **ReportLab**. Incluye autenticación JWT, migraciones con Alembic y despliegue con Docker.

## 🎯 Objetivos del laboratorio

- Implementar una API REST completa con FastAPI.
- Diseñar un modelo de datos relacional con SQLAlchemy (clientes, productos, facturas, ítems y usuarios).
- Aplicar autenticación y autorización mediante JWT.
- Calcular automáticamente subtotales, impuestos y totales en las facturas.
- Generar archivos PDF de facturas con ReportLab.
- Gestionar migraciones de base de datos con Alembic.
- Contenerizar la aplicación y la base de datos con Docker Compose.
- Escribir pruebas automatizadas con pytest.

## 🛠️ Tecnologías y dependencias

| Tecnología | Versión |
|------------|---------|
| Python | 3.9+ |
| FastAPI | 0.111.0 |
| Uvicorn | 0.29.0 |
| SQLAlchemy | 2.0.30 |
| Alembic | 1.13.1 |
| Pydantic | 2.7.1 |
| Pydantic‑Settings | 2.2.1 |
| python‑jose[cryptography] | 3.3.0 |
| passlib[bcrypt] | 1.7.4 |
| ReportLab | 4.2.0 |
| pytest | 8.2.0 |
| PostgreSQL (oficial) | 15 (Alpine) |

## 📁 Estructura del proyecto

```
facturacion-api/
├── alembic/                     # Migraciones de base de datos
│   └── versions/
├── app/
│   ├── models/                  # Modelos SQLAlchemy (User, Client, Product, Invoice, InvoiceItem)
│   ├── routers/                 # Endpoints organizados por recurso (auth, clients, products, invoices)
│   ├── schemas/                 # Esquemas Pydantic para validación y serialización
│   ├── services/                # Lógica de negocio (cálculos, generación de PDF, etc.)
│   ├── __init__.py
│   ├── database.py              # Conexión a la BD y sesión de SQLAlchemy
│   └── main.py                  # Punto de entrada de la aplicación
├── tests/                       # Pruebas unitarias y de integración
├── .env.example                 # Ejemplo de variables de entorno
├── docker-compose.yml           # Definición de servicios (PostgreSQL + API)
├── Dockerfile                   # Construcción de la imagen de la API
├── requirements.txt
└── README.md
```

> **Nota:** Los routers y servicios están en desarrollo; en `main.py` se encuentran importados pero comentados. A medida que avances, descoméntalos para habilitar los endpoints.

## 🗄️ Modelos de datos

La aplicación define cinco entidades principales:

- **User**: Usuario del sistema (email, contraseña hasheada, nombre completo). Cada usuario es dueño de sus clientes, productos y facturas.
- **Client**: Cliente (nombre, email, teléfono, dirección, CUIT). Pertenece a un usuario.
- **Product**: Producto o servicio (nombre, descripción, precio, stock). Pertenece a un usuario.
- **Invoice**: Factura (número único, estado: `pending`, `paid`, `cancelled`; subtotal, impuesto (21%), total, notas). Pertenece a un usuario y a un cliente.
- **InvoiceItem**: Línea de detalle de una factura (cantidad, precio unitario, subtotal). Relaciona una factura con un producto.

Las relaciones están definidas con SQLAlchemy y se reflejan en la base de datos PostgreSQL.

## 🔐 Autenticación

La API utiliza **JWT** para proteger los endpoints. La autenticación se implementa con `python-jose` y `passlib` (bcrypt). Los endpoints de autenticación permitirán:

- `POST /api/auth/register` – Crear un nuevo usuario.
- `POST /api/auth/login` – Obtener un token de acceso (Bearer).

El token debe incluirse en el header `Authorization: Bearer <token>` para acceder a recursos protegidos.

## 📄 Endpoints principales (en desarrollo)

Una vez habilitados los routers, la API ofrecerá los siguientes endpoints:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | `/`                    | Información de la API |
| GET    | `/health`              | Health check |
| POST   | `/api/auth/register`   | Registro de usuario |
| POST   | `/api/auth/login`      | Inicio de sesión |
| GET    | `/api/clients/`        | Listar clientes del usuario autenticado |
| POST   | `/api/clients/`        | Crear un nuevo cliente |
| GET    | `/api/clients/{id}`    | Obtener un cliente por ID |
| PUT    | `/api/clients/{id}`    | Actualizar un cliente |
| DELETE | `/api/clients/{id}`    | Eliminar un cliente |
| GET    | `/api/products/`       | Listar productos |
| POST   | `/api/products/`       | Crear un producto |
| GET    | `/api/products/{id}`   | Obtener un producto por ID |
| PUT    | `/api/products/{id}`   | Actualizar un producto |
| DELETE | `/api/products/{id}`   | Eliminar un producto |
| GET    | `/api/invoices/`       | Listar facturas |
| POST   | `/api/invoices/`       | Crear una factura (calcula subtotal, impuesto y total) |
| GET    | `/api/invoices/{id}`   | Obtener una factura por ID |
| PUT    | `/api/invoices/{id}`   | Actualizar una factura (cambiar estado o notas) |
| DELETE | `/api/invoices/{id}`   | Eliminar una factura |
| GET    | `/api/invoices/{id}/pdf` | Descargar el PDF de la factura (generado con ReportLab) |

## ⚙️ Instalación y configuración

### Requisitos previos

- Python 3.9 o superior
- PostgreSQL (si no usas Docker)
- Docker y Docker Compose (opcional, pero recomendado)

### 1. Clonar el repositorio

```bash
git clone https://github.com/juanillufriu/facturacion-api.git
cd facturacion-api
```

### 2. Configurar variables de entorno

Copia el archivo de ejemplo y ajusta los valores:

```bash
cp .env.example .env
```

Variables principales (todas tienen valores por defecto en el `docker-compose.yml`):

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `POSTGRES_USER` | Usuario de PostgreSQL | facturacion_user |
| `POSTGRES_PASSWORD` | Contraseña de PostgreSQL | facturacion_pass |
| `POSTGRES_DB` | Nombre de la base de datos | facturacion_db |
| `DATABASE_URL` | URL de conexión a la BD (se construye automáticamente en el contenedor) | – |
| `SECRET_KEY` | Clave secreta para firmar JWT | cámbiala siempre en producción |
| `ALGORITHM` | Algoritmo de cifrado | HS256 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Tiempo de expiración del token | 30 |
| `ENVIRONMENT` | Entorno (development / production) | development |
```