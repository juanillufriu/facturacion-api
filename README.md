# facturacion-api

### 📋 Project Data

<p align="left">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Role-Backend%20Developer-darkblue?style=for-the-badge" alt="Role">
  <img src="https://img.shields.io/badge/Author-Juan%20Ignacio%20Llufriu-lightblue?style=for-the-badge" alt="Author">
</p>

### 🛠️ Tech Stack

<p align="left">
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
<img src="https://img.shields.io/badge/FastAPI-109989?style=for-the-badge&logo=FASTAPI&logoColor=white" />
<img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=Pydantic&logoColor=white" />
<img src="https://img.shields.io/badge/PyTest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/SQLAlchemy-FFFFFF?style=for-the-badge&logo=sqlalchemy&logoColor=CA2727" />
<img src="https://img.shields.io/badge/Alembic-000000?style=for-the-badge&logo=Alembic&logoColor=FFFFFF" />
</p>

API RESTful para la gestión de facturación, desarrollada con **Python y FastAPI** como proyecto de laboratorio orientado al desarrollo backend.

El proyecto se encuentra actualmente en **fase de desarrollo inicial**. La primera etapa se centra en establecer la arquitectura de la aplicación, la configuración del entorno, la conexión con PostgreSQL mediante SQLAlchemy y el diseño del modelo de datos para usuarios, clientes, productos y facturas.

En etapas posteriores se incorporarán autenticación mediante JWT, operaciones CRUD, validación mediante Pydantic, lógica de negocio para el cálculo de facturas, generación de documentos PDF, migraciones con Alembic y una suite de pruebas automatizadas.

---

## 🎯 Objetivos del proyecto

El objetivo principal es desarrollar una API backend completa para administrar un sistema de facturación, aplicando buenas prácticas de desarrollo y una arquitectura modular.

Entre los objetivos se encuentran:

* Implementar una API REST utilizando **FastAPI**.
* Diseñar un modelo de datos relacional utilizando **SQLAlchemy**.
* Utilizar **PostgreSQL** como sistema gestor de base de datos.
* Implementar autenticación y autorización mediante **JWT**.
* Validar y serializar los datos mediante **Pydantic**.
* Implementar operaciones CRUD para clientes, productos y facturas.
* Calcular automáticamente subtotales, IVA y totales de las facturas.
* Generar documentos PDF de las facturas utilizando **ReportLab**.
* Gestionar las modificaciones del esquema de base de datos mediante **Alembic**.
* Contenerizar la API y PostgreSQL utilizando **Docker Compose**.
* Implementar pruebas unitarias y de integración mediante **pytest**.
* Aplicar una separación clara entre modelos, esquemas, routers y lógica de negocio.

---

## 🚦 Estado actual

El proyecto se encuentra en una **fase inicial de desarrollo**.

### ✅ Implementado actualmente

* Configuración inicial de FastAPI.
* Configuración mediante variables de entorno.
* Conexión con PostgreSQL.
* Configuración de SQLAlchemy.
* Creación inicial de tablas mediante `Base.metadata.create_all()`.
* Modelo relacional inicial.
* Entidades `User`, `Client`, `Product`, `Invoice` e `InvoiceItem`.
* Relaciones entre las entidades mediante SQLAlchemy.
* Estados de factura mediante `Enum`.
* Configuración de CORS.
* Manejo global de excepciones.
* Endpoint raíz de la API.
* Endpoint de health check.
* Configuración inicial de Docker y Docker Compose.
* Dependencias preparadas para autenticación, migraciones, generación de PDF y testing.

### 🚧 En desarrollo

* Arquitectura modular de routers.
* Esquemas Pydantic.
* Servicios y lógica de negocio.
* Sistema de autenticación.
* CRUD de clientes.
* CRUD de productos.
* CRUD de facturas.
* Cálculo automático de importes.
* Validaciones específicas del dominio.
* Pruebas automatizadas.

### 📌 Planificado

* Autenticación y autorización mediante JWT.
* Gestión de usuarios.
* Generación de PDFs.
* Migraciones mediante Alembic.
* Documentación completa de endpoints.
* Mejoras de seguridad y configuración para producción.
* Optimización de consultas y acceso a datos.
* Despliegue de la API.

---

## 🛠️ Tecnologías y dependencias

| Tecnología        | Versión   |
| ----------------- | --------- |
| Python            | 3.11      |
| FastAPI           | 0.111.0   |
| Uvicorn           | 0.29.0    |
| SQLAlchemy        | 2.0.30    |
| Alembic           | 1.13.1    |
| psycopg2-binary   | 2.9.9     |
| Pydantic          | 2.7.1     |
| Pydantic Settings | 2.2.1     |
| python-jose       | 3.3.0     |
| Passlib           | 1.7.4     |
| ReportLab         | 4.2.0     |
| python-dotenv     | 1.0.1     |
| pytest            | 8.2.0     |
| pytest-asyncio    | 0.23.6    |
| httpx             | 0.27.0    |
| PostgreSQL        | 15 Alpine |
| Docker            | —         |
| Docker Compose    | —         |

> Algunas dependencias, como `python-jose`, `Passlib`, `ReportLab` y `Alembic`, ya se encuentran incorporadas al proyecto pero serán utilizadas principalmente en etapas posteriores de desarrollo.

---

## 📁 Estructura actual del proyecto

```text
facturacion-api/
├── app/
│   ├── __init__.py
│   ├── config.py              # Configuración y variables de entorno
│   ├── database.py            # Engine, sesión y Base de SQLAlchemy
│   ├── models.py              # Modelos y relaciones de la base de datos
│   └── main.py                # Punto de entrada de FastAPI
├── tests/
│   └── test_auth.py           # Base inicial para pruebas de autenticación
├── .env.example               # Ejemplo de variables de entorno
├── docker-compose.yml         # Servicios de API y PostgreSQL
├── Dockerfile                 # Imagen de la API
├── requirements.txt           # Dependencias del proyecto
└── README.md
```

### Estructura prevista

A medida que avance el desarrollo, la estructura será reorganizada para separar las diferentes responsabilidades de la aplicación:

```text
facturacion-api/
├── alembic/
│   └── versions/              # Migraciones de base de datos
├── app/
│   ├── models/                # Modelos SQLAlchemy
│   ├── routers/               # Endpoints de la API
│   ├── schemas/               # Esquemas Pydantic
│   ├── services/              # Lógica de negocio
│   ├── dependencies/          # Dependencias y autenticación
│   ├── config.py              # Configuración
│   ├── database.py            # Conexión a la base de datos
│   └── main.py                # Punto de entrada
├── tests/
│   ├── unit/                  # Pruebas unitarias
│   └── integration/           # Pruebas de integración
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🗄️ Modelo de datos

Actualmente se encuentran definidos cinco modelos principales mediante SQLAlchemy.

### User

Representa a los usuarios del sistema.

Principales atributos:

* `id`
* `email`
* `hashed_password`
* `full_name`
* `is_active`
* `created_at`
* `updated_at`

Un usuario puede tener múltiples clientes, productos y facturas.

### Client

Representa a los clientes a los que se les realizan facturas.

Principales atributos:

* `id`
* `name`
* `email`
* `phone`
* `address`
* `cuit`
* `is_active`
* `user_id`
* `created_at`
* `updated_at`

El campo `cuit` está contemplado específicamente para información fiscal utilizada en Argentina.

### Product

Representa productos o servicios que pueden incluirse en una factura.

Principales atributos:

* `id`
* `name`
* `description`
* `price`
* `stock`
* `is_active`
* `user_id`
* `created_at`
* `updated_at`

### Invoice

Representa una factura.

Principales atributos:

* `id`
* `number`
* `status`
* `subtotal`
* `tax`
* `total`
* `notes`
* `client_id`
* `user_id`
* `created_at`
* `updated_at`

Los estados contemplados actualmente son:

```text
pending
paid
cancelled
```

Los campos `subtotal`, `tax` y `total` están preparados para implementar posteriormente el cálculo automático de los importes de la factura.

### InvoiceItem

Representa cada línea de detalle de una factura.

Principales atributos:

* `id`
* `quantity`
* `unit_price`
* `subtotal`
* `invoice_id`
* `product_id`

El `unit_price` se almacena independientemente del precio actual del producto para conservar el precio utilizado en el momento de la facturación.

### Relaciones

El modelo relacional actual sigue aproximadamente la siguiente estructura:

```text
User
 ├── Clients
 ├── Products
 └── Invoices
       │
       ├── Client
       │
       └── InvoiceItems
              │
              └── Product
```

---

## 🌐 API

### Endpoints disponibles actualmente

La API actualmente cuenta con los siguientes endpoints:

| Método | Endpoint           | Descripción                                                   |
| ------ | ------------------ | ------------------------------------------------------------- |
| GET    | `/`                | Información básica de la API                                  |
| GET    | `/health`          | Health check de la aplicación                                 |
| PUT    | `/items/{item_id}` | Endpoint temporal utilizado para pruebas iniciales de FastAPI |

El endpoint `/items/{item_id}` forma parte de las pruebas iniciales del framework y será reemplazado por los routers específicos del sistema de facturación.

### Documentación automática

FastAPI genera automáticamente documentación interactiva de la API.

Una vez iniciada la aplicación, estará disponible en:

```text
http://localhost:8000/docs
```

También se dispone de la documentación alternativa:

```text
http://localhost:8000/redoc
```

---

# 🔐 Autenticación y autorización

### Estado actual

La autenticación todavía **no está implementada**.

Sin embargo, el proyecto ya cuenta con las dependencias y variables de configuración necesarias para incorporar autenticación mediante **JWT**.

### Implementación prevista

Se desarrollará un sistema de autenticación basado en:

* Registro de usuarios.
* Inicio de sesión.
* Contraseñas almacenadas mediante hash.
* Tokens JWT.
* Expiración de tokens.
* Protección de endpoints mediante `Bearer Token`.
* Asociación de recursos con el usuario autenticado.
* Autorización para impedir el acceso a recursos pertenecientes a otros usuarios.

Los endpoints previstos son:

```text
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/me
```

El token será enviado mediante:

```http
Authorization: Bearer <token>
```

---

# 👥 Gestión de clientes

### Estado actual

El modelo `Client` ya se encuentra implementado y relacionado con `User` e `Invoice`.

Los endpoints todavía no están implementados.

### Endpoints previstos

| Método | Endpoint            | Descripción                             |
| ------ | ------------------- | --------------------------------------- |
| GET    | `/api/clients/`     | Listar clientes del usuario autenticado |
| POST   | `/api/clients/`     | Crear un cliente                        |
| GET    | `/api/clients/{id}` | Obtener un cliente                      |
| PUT    | `/api/clients/{id}` | Actualizar un cliente                   |
| DELETE | `/api/clients/{id}` | Eliminar un cliente                     |

Se incorporarán validaciones para los datos del cliente, incluyendo la información fiscal correspondiente.

---

# 📦 Gestión de productos

### Estado actual

El modelo `Product` ya se encuentra implementado y relacionado con `User` e `InvoiceItem`.

Los endpoints todavía no están implementados.

### Endpoints previstos

| Método | Endpoint             | Descripción            |
| ------ | -------------------- | ---------------------- |
| GET    | `/api/products/`     | Listar productos       |
| POST   | `/api/products/`     | Crear un producto      |
| GET    | `/api/products/{id}` | Obtener un producto    |
| PUT    | `/api/products/{id}` | Actualizar un producto |
| DELETE | `/api/products/{id}` | Eliminar un producto   |

También se incorporarán validaciones para precios, stock y disponibilidad de productos.

---

# 🧾 Gestión de facturas

### Estado actual

Los modelos `Invoice` e `InvoiceItem` ya se encuentran implementados junto con sus relaciones.

La lógica de creación y cálculo de facturas todavía no está implementada.

### Endpoints previstos

| Método | Endpoint                 | Descripción                |
| ------ | ------------------------ | -------------------------- |
| GET    | `/api/invoices/`         | Listar facturas            |
| POST   | `/api/invoices/`         | Crear una factura          |
| GET    | `/api/invoices/{id}`     | Obtener una factura        |
| PUT    | `/api/invoices/{id}`     | Actualizar una factura     |
| DELETE | `/api/invoices/{id}`     | Eliminar una factura       |
| GET    | `/api/invoices/{id}/pdf` | Generar y descargar el PDF |

---

# 🧮 Cálculo de facturas

Una de las funcionalidades principales previstas será el cálculo automático de los importes de cada factura.

Para cada `InvoiceItem` se calculará:

```text
subtotal_item = cantidad × precio_unitario
```

El subtotal de la factura será:

```text
subtotal = Σ subtotal_item
```

Posteriormente se calculará el IVA:

```text
IVA = subtotal × 0.21
```

Y finalmente:

```text
total = subtotal + IVA
```

El cálculo será realizado mediante la lógica de negocio de la aplicación y no deberá depender de valores enviados directamente por el cliente.

> Esta funcionalidad está planificada y todavía no se encuentra implementada en la versión actual.

---

# 📄 Generación de PDF

Se utilizará **ReportLab** para generar documentos PDF correspondientes a las facturas.

La funcionalidad prevista permitirá:

* Generar un PDF a partir de una factura.
* Incluir los datos del emisor.
* Incluir los datos del cliente.
* Mostrar los productos o servicios facturados.
* Mostrar cantidades y precios.
* Mostrar subtotal.
* Mostrar IVA.
* Mostrar total.
* Mostrar número y estado de la factura.
* Permitir la descarga del documento mediante la API.

Endpoint previsto:

```text
GET /api/invoices/{id}/pdf
```

La dependencia `ReportLab` ya se encuentra incluida en el proyecto, pero la generación de PDF todavía no está implementada.

---

# 🗃️ Base de datos y migraciones

Actualmente la aplicación utiliza **SQLAlchemy** para definir el modelo de datos y crea las tablas automáticamente durante el inicio de la aplicación mediante:

```python
Base.metadata.create_all(bind=engine)
```

Este comportamiento resulta adecuado para la etapa inicial de desarrollo.

Como parte de la evolución del proyecto, se implementará **Alembic** para gestionar las migraciones de la base de datos.

El objetivo será reemplazar la creación automática de tablas por un flujo de migraciones controlado:

```text
Modelo SQLAlchemy
       ↓
Alembic revision
       ↓
Migration
       ↓
PostgreSQL
```

Esto permitirá mantener un historial de cambios del esquema y facilitar el despliegue de nuevas versiones.

---

# 🐳 Docker

El proyecto incluye soporte para Docker mediante:

```text
Dockerfile
docker-compose.yml
```

Docker Compose define dos servicios principales:

```text
┌──────────────────────────┐
│          API             │
│       FastAPI            │
│       Port 8000          │
└────────────┬─────────────┘
             │
             │ SQLAlchemy
             ▼
┌──────────────────────────┐
│       PostgreSQL         │
│        Database          │
└──────────────────────────┘
```

La API utiliza el servicio `db` como host de PostgreSQL dentro de la red de Docker Compose.

La aplicación está configurada para esperar a que PostgreSQL se encuentre disponible mediante un `healthcheck`.

---

# ⚙️ Instalación y configuración

## Requisitos previos

Para ejecutar el proyecto localmente se recomienda disponer de:

* Python 3.11
* PostgreSQL 15 o compatible
* Docker
* Docker Compose
* Git

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/juanillufriu/facturacion-api.git
cd facturacion-api
```

---

## 2. Crear un entorno virtual

En Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

En Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Configurar variables de entorno

Crear el archivo `.env` a partir del ejemplo:

```bash
cp .env.example .env
```

En Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Las principales variables de configuración son:

| Variable                      | Descripción                  | Valor de desarrollo   |
| ----------------------------- | ---------------------------- | --------------------- |
| `POSTGRES_USER`               | Usuario de PostgreSQL        | `facturacion_user`    |
| `POSTGRES_PASSWORD`           | Contraseña de PostgreSQL     | `facturacion_pass`    |
| `POSTGRES_DB`                 | Nombre de la base de datos   | `facturacion_db`      |
| `DATABASE_URL`                | URL de conexión a PostgreSQL | Según configuración   |
| `SECRET_KEY`                  | Clave utilizada para JWT     | Cambiar en producción |
| `ALGORITHM`                   | Algoritmo JWT                | `HS256`               |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Duración del token           | `30`                  |
| `ENVIRONMENT`                 | Entorno de ejecución         | `development`         |

> El archivo `.env` contiene configuración específica del entorno y no debe publicarse en el repositorio. Utilizar `.env.example` para documentar las variables necesarias.

---

# ▶️ Ejecución local

Con el entorno virtual activo:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```text
http://localhost:8000
```

Documentación interactiva:

```text
http://localhost:8000/docs
```

Documentación alternativa:

```text
http://localhost:8000/redoc
```

---

# 🐳 Ejecución con Docker Compose

Para construir y ejecutar los servicios:

```bash
docker compose up --build
```

La API estará disponible en:

```text
http://localhost:8000
```

Para ejecutar los servicios en segundo plano:

```bash
docker compose up -d --build
```

Para detenerlos:

```bash
docker compose down
```

Los datos de PostgreSQL se almacenan en un volumen persistente de Docker.

---

# 🧪 Testing

El proyecto incluye **pytest**, `pytest-asyncio` y `httpx` como dependencias para implementar pruebas automatizadas.

Actualmente la estructura de testing se encuentra en una etapa inicial.

La estrategia prevista incluye:

### Pruebas unitarias

Se probarán componentes individuales de la aplicación, como:

* Validaciones.
* Cálculos de facturación.
* Lógica de negocio.
* Autenticación.
* Generación de documentos.

### Pruebas de integración

Se probará la interacción entre:

```text
API
 ↓
Services
 ↓
SQLAlchemy
 ↓
PostgreSQL
```

### Pruebas de endpoints

Se verificarán casos como:

* Registro de usuarios.
* Login.
* Acceso autorizado/no autorizado.
* CRUD de clientes.
* CRUD de productos.
* Creación de facturas.
* Cálculo de importes.
* Generación de PDFs.

---

# 🗺️ Roadmap

El desarrollo previsto del proyecto se divide en las siguientes etapas:

### Fase 1 — Arquitectura y persistencia

* [x] Configuración inicial de FastAPI.
* [x] Configuración mediante variables de entorno.
* [x] Conexión con PostgreSQL.
* [x] Configuración de SQLAlchemy.
* [x] Definición de modelos.
* [x] Definición de relaciones.
* [x] Configuración inicial de Docker.
* [x] Endpoints básicos de health check.

### Fase 2 — Arquitectura modular

* [ ] Separar modelos en módulos.
* [ ] Crear schemas Pydantic.
* [ ] Crear routers.
* [ ] Crear services.
* [ ] Crear dependencias reutilizables.
* [ ] Mejorar la estructura general del proyecto.

### Fase 3 — Autenticación

* [ ] Registro de usuarios.
* [ ] Hash de contraseñas.
* [ ] Login.
* [ ] Generación de JWT.
* [ ] Validación de tokens.
* [ ] Protección de endpoints.
* [ ] Autorización por usuario.

### Fase 4 — Clientes y productos

* [ ] CRUD de clientes.
* [ ] Validación de datos de clientes.
* [ ] CRUD de productos.
* [ ] Validación de precios y stock.
* [ ] Filtrado por usuario autenticado.

### Fase 5 — Facturación

* [ ] Creación de facturas.
* [ ] Creación de ítems de factura.
* [ ] Cálculo de subtotales.
* [ ] Cálculo automático de IVA.
* [ ] Cálculo de totales.
* [ ] Gestión de estados.
* [ ] Validaciones de negocio.
* [ ] Control de stock.

### Fase 6 — PDF

* [ ] Implementación de ReportLab.
* [ ] Diseño del documento.
* [ ] Inclusión de información del cliente.
* [ ] Inclusión de detalle de productos.
* [ ] Inclusión de impuestos y totales.
* [ ] Endpoint de descarga de PDF.

### Fase 7 — Base de datos

* [ ] Configuración de Alembic.
* [ ] Primera migración.
* [ ] Migraciones incrementales.
* [ ] Eliminar dependencia de `create_all()` para producción.

### Fase 8 — Testing

* [ ] Tests unitarios.
* [ ] Tests de autenticación.
* [ ] Tests de CRUD.
* [ ] Tests de facturación.
* [ ] Tests de integración.
* [ ] Tests de generación de PDF.

### Fase 9 — Producción

* [ ] Configuración de CORS para dominios reales.
* [ ] Gestión segura de secretos.
* [ ] Configuración de entorno de producción.
* [ ] Optimización de Docker.
* [ ] Logging.
* [ ] Manejo de errores.
* [ ] Documentación final de la API.
* [ ] Despliegue.

---

# 🔒 Consideraciones de seguridad

Durante el desarrollo se utilizarán configuraciones simplificadas para facilitar las pruebas.

Antes de utilizar la aplicación en producción se deberán implementar, entre otras medidas:

* Secretos seguros mediante variables de entorno.
* Restricción de CORS.
* Hash seguro de contraseñas.
* Expiración y validación de JWT.
* Autorización por usuario.
* Validación estricta de entradas.
* Manejo adecuado de errores.
* Configuración segura de PostgreSQL.
* Separación de entornos de desarrollo y producción.

---

# 📚 Documentación de la API

FastAPI proporciona documentación automática mediante OpenAPI.

Una vez ejecutada la aplicación:

**Swagger UI**

```text
http://localhost:8000/docs
```

**ReDoc**

```text
http://localhost:8000/redoc
```

La documentación se irá ampliando a medida que se incorporen los diferentes routers y endpoints.

---

# 👨‍💻 Autor

**Juan Ignacio Llufriu**

Backend Developer en formación
Estudiante de Ingeniería en Sistemas de Información

GitHub:

https://github.com/juanillufriu

---

## 📌 Estado del proyecto

> **Este proyecto se encuentra actualmente en desarrollo.**
>
> La versión actual establece la base de la API, la conexión con PostgreSQL, la persistencia mediante SQLAlchemy y el modelo de datos principal. Las funcionalidades de autenticación, CRUD, cálculo de facturación, generación de PDF, migraciones y testing serán implementadas progresivamente de acuerdo con el roadmap definido anteriormente.
