# 🎫 Ticket Management System (FastAPI)

## 📌 Project Overview

This is a backend API for a Ticket Management System built using FastAPI.
It allows users to create, manage, and track tickets with authentication and role-based access.

---

## 🚀 Features

### 🔐 Authentication

* User Registration
* User Login (JWT आधारित authentication)
* Password hashing (bcrypt)

### 🔒 Authorization

* Protected routes using JWT
* Role-based access (User / Admin)

### 🎫 Ticket Management

* Create Ticket
* Get All Tickets (with filters)
* Get Ticket by ID
* Update Ticket
* Update Ticket Status
* Delete Ticket

### 📊 Admin Features

* View ticket statistics:

  * Total tickets
  * Open tickets
  * Closed tickets

---

## 🛠 Tech Stack

* FastAPI
* Python
* SQLite
* SQLAlchemy
* JWT (Authentication)
* Passlib (Password hashing)

---

## 📂 Project Structure

```
app/
 ├── core/        # Security & auth logic
 ├── models/      # Database models
 ├── routes/      # API routes
 ├── schemas/     # Pydantic schemas
 ├── database.py  # DB connection
 ├── main.py      # Entry point
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone <your-repo-link>
cd ticket-system
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run server

```
uvicorn app.main:app --reload
```

---

## 📘 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🔑 Sample APIs

### Register

POST `/auth/register`

### Login

POST `/auth/login`

### Create Ticket

POST `/tickets/`

### Get Tickets

GET `/tickets/`

### Admin Stats

GET `/admin/stats`

---

## 📌 Author

Aman Singh

