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


# Flask REST API

A REST API built using Flask and SQLAlchemy following the MVC architecture.

## Features

- REST API using Flask
- SQLAlchemy ORM
- CRUD Operations
- Image Upload
- JSON Responses
- MVC Project Structure
- MySQL Database

---

## Project Structure

```
Flask/
│
├── controllers/
├── models/
├── schema/
├── uploads/
├── app.py
├── extensions.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/flask-rest-api.git
```

Move into the project

```bash
cd flask-rest-api
```

Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate Virtual Environment

Git Bash

```bash
source venv/Scripts/activate
```

Command Prompt

```cmd
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python app.py
```

or

```bash
flask run
```

Server

```
http://127.0.0.1:5000
```

---

## API Endpoints

### Users

| Method | Endpoint |
|---------|----------|
| GET | /users |
| POST | /users |

### Products

| Method | Endpoint |
|---------|----------|
| GET | /products |
| POST | /products |

---

## Technologies Used

- Python
- Flask
- SQLAlchemy
- MySQL
- REST API

---

## Ignore Files

The following files are ignored by Git.

- venv/
- __pycache__/
- uploads/
- .env

---

## Author

Shubham Verma