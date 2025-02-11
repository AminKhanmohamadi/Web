# Weblog Project (Django + Celery + RabbitMQ + PostgreSQL)

## 📌 Overview
This project is a blogging system built with **Django**, **Django Rest Framework (DRF)**, **Celery**, **RabbitMQ**, and **PostgreSQL**. The system allows users to create articles and knowledge entries, with automated summarization of articles using **Celery tasks**.

---

## 🚀 Features
- **Article & Knowledge Management**
- **Many-to-Many Relationship** (Articles linked to Knowledge entries)
- **Role-based access control** (Superusers can see all articles, regular users only see published articles)
- **Automated article summarization** (Using Celery and RabbitMQ)
- **API Development** (Using Django Rest Framework)
- **Dockerized environment** (Runs with Docker & Docker Compose)

---

## 🛠️ Installation & Setup
### **1. Clone the Repository**
```sh
$ git clone https://github.com/AminKhanmohamadi/Web.git
$ cd weblog
```

### **2. Environment Variables**
Create a `.env` file in the root directory and configure your environment variables:
```env
OPENAI_API_KEY=api
```

### **3. Build & Run with Docker**
```sh
$ docker-compose up --build
$ docker-compose exec -it app manage.py migrate
```
This will start the **Django app, PostgreSQL, and RabbitMQ** inside Docker containers.

---

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|------------|------------------------------|
| **GET** | `/api/v1/knowledge/` | List all knowledge entries |
| **GET** | `/api/v1/article/` | List all articles (filtered by user role) |
| **GET** | `/api/v1/article/{id}/` | Retrieve article details |

---

## ⚙️ Celery & RabbitMQ
This project uses **Celery** and **RabbitMQ** to handle background tasks.
- **After creating an article**, Celery automatically generates a summary for it.
- To run the Celery worker:
```sh
$ docker-compose exec backend celery -A weblog worker --loglevel=info
```
- To run the Celery beat (for periodic tasks):
```sh
$ docker-compose exec backend celery -A weblog beat --loglevel=info
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🙌 Contributing
Feel free to submit a pull request or open an issue!

### **Author**: [amin khanmohammadi]

