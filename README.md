# 🎫 Ticket Management System API (FastAPI)

## 📌 Overview

This project is a backend Ticket Management System built using FastAPI.
It provides secure authentication, role-based access control, and full ticket lifecycle management.

Additionally, it includes a **natural language query feature** that allows users to search tickets using simple English queries.

---

## 🚀 Features

### 🔐 Authentication & Security

* User Registration
* User Login (OAuth2 + JWT)
* Password hashing using bcrypt
* Secure token-based authentication

---

### 🔒 Authorization

* Protected APIs using JWT
* Role-based access control:

  * **User** → Manage own tickets
  * **Admin** → Access all tickets + stats

---

### 🎫 Ticket Management (CRUD)

* Create Ticket
* Get All Tickets (with filters)
* Get Ticket by ID
* Update Ticket
* Update Ticket Status
* Delete Ticket

---

### 🔍 Advanced Query Features

* Filter by status (`open`, `closed`)
* Filter by priority (`high`, `medium`, `low`)
* Pagination using `skip` and `limit`
* Search using keywords (title + description)

---

### 🤖 AI-like Natural Language Search (Bonus Feature)

* Users can query tickets using simple sentences

#### Examples:

```id="ex1"
show high priority tickets
```

```id="ex2"
show open tickets
```

```id="ex3"
show closed tickets
```

👉 The system extracts keywords and applies filters dynamically.

---

### 📊 Admin Dashboard API

* Total tickets
* Open tickets
* Closed tickets

---

## 🛠 Tech Stack

* FastAPI
* Python
* SQLAlchemy
* SQLite
* JWT (Authentication)
* Passlib (bcrypt hashing)

---

## 📂 Project Structure

```id="tree"
app/
 ├── core/        # Auth, security, dependencies
 ├── models/      # Database models
 ├── routes/      # API routes (auth, tickets, admin, ai)
 ├── schemas/     # Request/response validation
 ├── database.py  # Database connection
 ├── main.py      # App entry point
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```id="clone"
git clone <your-repo-link>
cd ticket-system
```

### 2. Create Virtual Environment

```id="venv"
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```id="install"
pip install -r requirements.txt
```

### 4. Run Server

```id="run"
uvicorn app.main:app --reload
```

---

## 📘 API Documentation

Swagger UI:

```id="docs"
http://127.0.0.1:8000/docs
```

---

## 🔑 Key APIs

### Authentication

* `POST /auth/register`
* `POST /auth/login`
* `GET /auth/me`

### Tickets

* `POST /tickets/`
* `GET /tickets/`
* `GET /tickets/{id}`
* `PUT /tickets/{id}`
* `PATCH /tickets/{id}/status`
* `DELETE /tickets/{id}`

### Admin

* `GET /admin/stats`

### AI Feature

* `GET /ai/query?q=your_query`

---

## 🧠 Design Highlights

* Dependency Injection (FastAPI Depends)
* JWT-based authentication flow
* Role-based authorization
* Dynamic query filtering
* Clean modular structure
* AI-like query interpretation (rule-based NLP)

---

## 📌 Author

Aman Singh

---

## ⭐ Notes

This project demonstrates backend development skills including API design, authentication, database handling, and basic NLP-based enhancements.
