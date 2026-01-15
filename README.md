# Enterprise AI Project Optimizer

## Overview

Enterprise AI Project Optimizer is a full-stack AI system that predicts **project duration, cost, and delay risk**
based on **historical enterprise project data** using machine learning.

---

## Tech Stack

- **ML API:** Python, FastAPI, scikit-learn
- **Backend:** Java, Spring Boot
- **Frontend:** React (Vite)
- **Database:** SQLite
- **DevOps:** Docker, Docker Compose

---

## Architecture

Frontend (React)
↓
Spring Backend (Java)
↓
ML API (FastAPI)
↓
ML Models + SQLite

---

## Run with Docker

### Prerequisites
- Docker
- Docker Compose

### Start all services
From the project root:
```bash
docker-compose up --build
```

Services

Frontend: http://localhost:5173

Spring Backend: http://localhost:8080

ML API Docs: http://localhost:8000/docs


## Main Endpoints

### ML API Endpoints

Method | Endpoint                | Description
-------|------------------------|-------------
POST   | /predict_duration       | Predict project duration based on `team_size` and `issues`
POST   | /predict_cost           | Predict project cost based on `team_size` and `issues`
POST   | /predict_delay          | Predict if project will be delayed
POST   | /predict_full           | Predict duration, cost, and delay in one request
GET    | /projects               | Retrieve all stored project predictions

**Example JSON for `/predict_full`:**

```json
{
  "team_size": 5,
  "issues": 2
}
```
---

### Spring Backend Endpoints

Spring backend wraps the ML API and provides these endpoints:

Method | Endpoint           | Description
-------|------------------|-------------
GET   | /predict           | Predict project duration, cost, and delay via JSON
GET   | /projects           | return all projects

---

## Notes

* Trained ML models (*.pkl) are included.
* projects.db is generated automatically and ignored in GitHub.
* All services communicate via Docker network.

