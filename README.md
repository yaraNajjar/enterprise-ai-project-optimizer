# Enterprise AI Project Optimizer

## Overview

Enterprise AI Project Optimizer is a full-stack AI system that predicts **project duration, cost, and delay risk**
based on **historical enterprise project data** using machine learning.
It includes a full QA setup to ensure reliability across ML API, Backend, Frontend, and Integration layers.

---

## Tech Stack

- **ML API:** Python, FastAPI, scikit-learn
- **Backend:** Java, Spring Boot
- **Frontend:** React (Vite)
- **Database:** SQLite
- **DevOps:** Docker, Docker Compose
- **QA / Testing:** pytest, Vitest, Postman, Manual & Integration Testing
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
GET   | /projects           | Retrieves all previously predicted projects from the database

---
## QA & Testing

This project has a complete QA setup to validate all layers:

### 1. ML API Tests

* **Location:** ml/tests/test_ml_api.py

* **What is tested:** POST /predict_full, GET /projects, response structure, status codes

* **How to run:**
```bash
docker-compose up ai-api
pytest ml/tests/
```

### 2. Spring Backend Tests

* **Location:** spring-backend/src/test/

* **What is tested:** Backend context loads, endpoints work, communication with ML API

* **How to run:**
```bash
cd spring-backend
mvn test
```

### 3. Frontend Tests (React)

* **Location:** frontend/src/App.test.jsx

* **What is tested:** UI rendering, Predict button, mocked API calls, display of prediction results

* **How to run:**
```bash
cd frontend
npm test
```
### 4. Integration Testing

* **Flow:** React → Spring Boot → FastAPI → Database

* **Validated:** Data flows correctly, predictions persisted, Docker networking works

* **Documentation:** qa/INTEGRATION_TESTS.md

### 5. Postman API Testing

* **Location:** qa/postman/Enterprise_AI_Project_Optimizer.postman_collection.json

* **Tested APIs:** /predict_full, /projects

* **Validated:** Status codes, response fields, data consistency

* **How to run:**

1. Import collection in Postman

2. Run collection or use Newman for CLI automation

### 6. Test Cases

* **Location:** qa/TEST_CASES.md

* **Description:** Lists all features, steps, and expected results

### 7. Bug Tracking

* **Location:** qa/BUG_REPORTS.md

* **Description:** Documented realistic bugs, steps to reproduce, and fixes
---

## Notes

* Trained ML models (*.pkl) are included.
* projects.db is generated automatically and ignored in GitHub.
* All services communicate via Docker network.
* QA demonstrates a **full QA mindset:** documentation, realistic bugs, automation, and end-to-end validation
