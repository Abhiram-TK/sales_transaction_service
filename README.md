# Sales Transaction Service

## Overview

Sales Transaction Service is a FastAPI-based backend microservice responsible for creating and managing sales transactions.

The service integrates with the Authentication Service for JWT-based authentication and permission-based authorization, and with the Inventory Dispatch System to retrieve product information and reserve inventory after a transaction is created.

This project demonstrates backend service development using FastAPI, PostgreSQL, SQLAlchemy, Celery, Redis, and REST API integration.

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Celery
- Redis
- JWT Authentication
- Permission-Based Authorization (RBAC)
- Swagger UI

---

## System Architecture

```text
                Authentication Service
                        │
                 JWT Authentication
                        │
                        ▼
              Sales Transaction Service
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
 Product Service API            Inventory Events
        │                               │
        ▼                               ▼
Inventory Dispatch System     Reservation Processing
```

---

## Transaction Workflow

```text
Client
    │
    ▼
POST /transactions
    │
    ▼
Validate JWT
    │
    ▼
Check Permissions
    │
    ▼
Retrieve Product Details
    │
    ▼
Generate Invoice Number
    │
    ▼
Calculate Amount
    │
    ▼
Store Transaction
    │
    ▼
Emit TRANSACTION_CREATED Event
    │
    ▼
Inventory Dispatch System
    │
    ▼
Reserve Inventory
```

---

## Features

### Transaction Management

- Create sales transaction
- View all transactions
- View transaction by ID
- Update transaction

### Product Integration

- Proxy product catalog from Inventory Dispatch System
- Automatic product price retrieval

### Automatic Processing

- Automatic invoice generation
- Automatic transaction amount calculation
- Inventory reservation event emission

### Security

- JWT Authentication
- Permission-based Authorization
- Request validation
- Idempotency support
- Basic rate limiting

### Background Processing

- Celery worker
- Asynchronous transaction validation

### Documentation

- Interactive Swagger UI

---

## Project Structure

```text
sales_transaction_service/

├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── events/
│   ├── middleware/
│   ├── models/
│   ├── operations/
│   ├── schemas/
│   ├── services/
│   ├── workers/
│   └── main.py
│
├── logs/
├── requirements.txt
├── .env.example
└── README.md
```

---

## API Endpoints

### System

| Method | Endpoint | Description          |
| ------ | -------- | -------------------- |
| GET    | /health  | Service health check |

### Products

| Method | Endpoint  | Description                 |
| ------ | --------- | --------------------------- |
| GET    | /products | Retrieve available products |

### Transactions

| Method | Endpoint           | Description          |
| ------ | ------------------ | -------------------- |
| POST   | /transactions      | Create transaction   |
| GET    | /transactions      | List transactions    |
| GET    | /transactions/{id} | Retrieve transaction |
| PUT    | /transactions/{id} | Update transaction   |

---

## Example Transaction Request

```json
{
  "customer_name": "ABC Corporation",
  "product_id": 1,
  "quantity": 5
}
```

---

## Example Transaction Response

```json
{
  "transaction_id": 1,
  "customer_name": "ABC Corporation",
  "product_id": 1,
  "quantity": 5,
  "invoice_number": "INV-2026-000001",
  "amount": 360000,
  "status": "VALIDATED",
  "reservation_status": "RESERVED"
}
```

---

## Security Model

Every protected endpoint requires:

- Valid JWT access token
- Permission-based authorization
- Request validation

Example permissions include:

- create_transactions
- view_transactions
- update_transactions
- view_products

---

## Running the Project

### Clone Repository

```bash
git clone <https://github.com/Abhiram-TK/sales_transaction_service>
```

### Enter Project

```bash
cd sales_transaction_service
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file using `.env.example`.

### Start API

```bash
uvicorn app.main:app --reload --port 8001
```

### Start Celery Worker

```bash
celery -A app.workers.celery_app worker --pool=solo --loglevel=info
```

---

## Swagger UI

```
http://127.0.0.1:8001/docs
```

Swagger provides:

- Interactive endpoint testing
- Request validation
- Response schemas
- Authentication support

---

## Related Projects

This project is designed to work with:

- Authentication Service
- Inventory Dispatch System

Together these services demonstrate a simple event-driven backend architecture using multiple FastAPI services.

---

## Current Status

Implemented

- Sales transaction management
- JWT authentication
- Permission-based authorization
- Product integration
- Automatic invoice generation
- Automatic amount calculation
- Event-driven inventory reservation
- Reservation tracking
- Celery background validation
- Swagger documentation

Next Phase

- Docker containerization
- Docker Compose deployment
