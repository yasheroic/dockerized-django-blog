# Dockerized Django Blog Application

This project demonstrates how to **Dockerize a full-stack web application** using Django and PostgreSQL.  
The application is containerized using **Docker**, orchestrated with **Docker Compose**, and the application image is published on **Docker Hub**.

This project was built as part of the **#90DaysOfDevOps challenge (Day 36)**.

---

# Application Overview

This is a simple **Django Blog application** that allows users to create and view blog posts.

Features:
- Django backend
- PostgreSQL database
- Admin panel for managing posts
- Gunicorn as the production WSGI server
- Docker multi-stage build
- Non-root container execution
- Docker Compose orchestration
- Persistent PostgreSQL storage

Architecture:

Browser  
↓  
Gunicorn  
↓  
Django Application  
↓  
PostgreSQL Database

---

# Project Structure

```

.
├── blog/                # Django blog app
├── config/              # Django project settings
├── templates/           # HTML templates
├── Dockerfile.multistage
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── .env
└── README.md

````

---

# Running the Application with Docker Compose

## 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <project-folder>
````

---

## 2️⃣ Create a `.env` file

Example:

```
DEBUG=True
SECRET_KEY=changeme

DB_NAME=django_db
DB_USER=django_user
DB_PASSWORD=django_pass
DB_HOST=db
DB_PORT=5432

POSTGRES_DB=django_db
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_pass
```

---

## 3️⃣ Start the application

Run:

```bash
docker compose up
```

Docker Compose will:

1. Pull the Django image from Docker Hub
2. Start the PostgreSQL container
3. Create the network and volumes
4. Start the Django application container

---

## 4️⃣ Access the application

Open your browser:

```
http://localhost:8000
```

---

# Running the Admin Panel

Create an admin user:

```bash
docker compose exec django-app python manage.py createsuperuser
```

Then visit:

```
http://localhost:8000/admin
```

---

# Environment Variables

The application uses the following environment variables.

| Variable          | Description                    |
| ----------------- | ------------------------------ |
| DEBUG             | Enable/disable debug mode      |
| SECRET_KEY        | Django secret key              |
| DB_NAME           | PostgreSQL database name       |
| DB_USER           | PostgreSQL username            |
| DB_PASSWORD       | PostgreSQL password            |
| DB_HOST           | Database hostname (db service) |
| DB_PORT           | Database port                  |
| POSTGRES_DB       | PostgreSQL database            |
| POSTGRES_USER     | PostgreSQL user                |
| POSTGRES_PASSWORD | PostgreSQL password            |

---

# Docker Hub Image

Docker image for the application:

```
yasheroic/django-app:latest
```

To pull manually:

```bash
docker pull yasheroic/django-app:latest
```

---

# Stopping the Application

```bash
docker compose down
```

To remove volumes as well:

```bash
docker compose down -v
```

---

# Technologies Used

* Python
* Django
* PostgreSQL
* Docker
* Docker Compose
* Gunicorn

---

# Author

Built as part of the **#90DaysOfDevOps** learning challenge.

