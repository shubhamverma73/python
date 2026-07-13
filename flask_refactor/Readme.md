<!--
source ./venv/Scripts/activate
flask run
python app.py
-->

<!-- 
Client
↓
Routes
↓
Controller
↓
Service
↓
Model
↓
Database
-->


<!--
utils/logger.py → Logging is configured.
middleware/error_handler.py → Configure error handling.
-->

<!--
For save dependencies:
    pip freeze > requirements.txt
-->


# Flask Production Architecture (Beginner Friendly)

A beginner-friendly Flask backend project built with a production-style architecture. The goal of this project is to learn how real-world Flask applications are structured without introducing unnecessary complexity.

This project follows a clean architecture using Blueprints, Controllers, Services, SQLAlchemy ORM, JWT Authentication, Logging, Global Error Handling, Pagination, Image Upload, and other production-ready practices.

---

# Features

* Production-style Flask architecture
* Blueprints
* Controller Layer
* Service Layer
* SQLAlchemy ORM
* JWT Authentication
* Password Hashing (Flask-Bcrypt)
* User Login
* Current Logged-in User
* JWT Logout (Token Revocation)
* JWT Custom Error Handlers
* Global Error Handling
* Image Upload
* Logging
* Pagination
* Standard API Response Format
* Environment Configuration
* SQLite/MySQL support (depending on configuration)

---

# Project Structure

```text
project/
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── .env
│
├── controllers/
│   └── auth_controller.py
│   └── user_controller.py
│
├── services/
│   └── auth_service.py
│   └── user_service.py
│
├── models/
│   └── user_model.py
│
├── routes/
│   └── auth_routes.py
│   └── user_routes.py
│
├── middleware/
│
├── utils/
│   ├── response.py
│   ├── logger.py
│   ├── token_blocklist.py
│   └── helpers.py
│
├── uploads/
│
└── logs/
```

---

# Architecture

```
Client

↓

Routes

↓

Controllers

↓

Services

↓

Models (SQLAlchemy ORM)

↓

Database
```

### Responsibilities

### Routes

* Define API endpoints
* Apply middleware
* Forward request to controllers

### Controllers

* Receive request
* Validate input
* Call service methods
* Return response

### Services

* Business Logic
* Database operations
* Authentication
* File Upload Logic

### Models

* Database Tables
* SQLAlchemy ORM

### Utils

* Common Helpers
* Response Formatter
* Logger
* JWT Blocklist

---

# Tech Stack

Backend

* Python
* Flask

Database

* SQLAlchemy ORM

Authentication

* Flask-JWT-Extended
* Flask-Bcrypt

Others

* Flask-CORS
* Logging
* Pagination

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd project-folder
```

Create virtual environment

Windows

```bash
python -m venv venv
```

Linux / macOS

```bash
python3 -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

Example

```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret

DATABASE_URL=sqlite:///database.db

UPLOAD_FOLDER=uploads

MAX_CONTENT_LENGTH=5242880
```

---

# Run Project

```bash
python app.py
```

Server

```
http://127.0.0.1:5000
```

---

# Authentication

Implemented using JWT.

Flow

```
Login

↓

Access Token

↓

Protected Routes

↓

Logout

↓

Token Revoked
```

Implemented Features

* Login
* Protected APIs
* Current Logged-in User
* JWT Error Handlers
* Logout
* Token Revocation (Blocklist)

---

# API Endpoints

## Authentication

| Method | Endpoint             | Description            |
| ------ | -------------------- | ---------------------- |
| POST   | /api/v1/auth/login   | Login User             |
| GET    | /api/v1/auth/profile | Current Logged-in User |
| POST   | /api/v1/auth/logout  | Logout User            |

## Users

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | /api/v1/users      |
| GET    | /api/v1/users/<id> |
| POST   | /api/v1/users      |
| PUT    | /api/v1/users/<id> |
| DELETE | /api/v1/users/<id> |

Supports Pagination

Example

```
GET /api/v1/users?page=1&per_page=5
```

---

# API Response Format

Success

```json
{
    "status": "success",
    "message": "Request successful",
    "data": {}
}
```

Error

```json
{
    "status": "error",
    "message": "Something went wrong",
    "data": null
}
```

---

# Testing

The following scenarios have been tested.

* Login Success
* Wrong Password
* User Not Found
* Missing Token
* Invalid Token
* Expired Token
* Logout
* Revoked Token
* Pagination
* Image Upload
* Invalid JSON
* Validation Errors

---

# Current Learning Scope

This project intentionally avoids advanced patterns such as:

* Repository Pattern
* Generic CRUD
* Dependency Injection
* Base Service

The objective is to keep the architecture beginner-friendly while following production practices.

---

# Future Improvements

* Refresh Token Authentication
* Role Based Authorization (RBAC)
* Email Verification
* Forgot Password
* Password Reset
* Database Migrations (Alembic)
* SQLAlchemy Relationships
* Redis Blocklist
* Docker
* Unit Testing
* CI/CD

---

# License

This project is created for learning purposes.

---

# Author

Developed as part of a journey to become an AI Engineer and Full Stack Developer while learning production-ready backend development with Flask.
