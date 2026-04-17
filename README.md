# School Management System - Django REST API

A simple and clean **CRUD** REST API built with Django and Django REST Framework for managing Teachers, Groups, and Students.

## 📋 Models

- **Teacher (Ustoz)**
  - First Name, Last Name, Subject
- **Group (Guruh)**
  - Name, Teacher (ForeignKey)
- **Student (Talaba)**
  - First Name, Last Name, Birth Date, Grade, Group (ForeignKey)

## 🛠 Technologies

- Django
- Django REST Framework
- SQLite (for development)

## ✨ Features

- Full CRUD operations for Teachers, Groups, and Students
- Proper ForeignKey relationships
  - One teacher can have multiple groups
  - One group can have multiple students
- Ordering by last name and first name where applicable

## 📌 Main API Endpoints

| Method | Endpoint              | Description                    |
|--------|-----------------------|--------------------------------|
| GET    | `/api/teachers/`      | List all teachers              |
| POST   | `/api/teachers/`      | Create a new teacher           |
| GET    | `/api/groups/`        | List all groups                |
| GET    | `/api/students/`      | List all students              |

> Full list of endpoints is defined in `urls.py`

## 🗄 Database Relationships

- **Teacher → Group**: One-to-Many (optional)
- **Group → Student**: One-to-Many (required)
- When a group is deleted, all related students are also deleted (`CASCADE`)

## 📂 Project Structure (Main files)

- `models.py` — Database models
- `serializers.py` — DRF serializers
- `views.py` — API views
- `urls.py` — API routes

---

**Fully functional CRUD API** ✅

Good luck with your project! 🚀
