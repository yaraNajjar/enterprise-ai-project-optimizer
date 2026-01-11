# Enterprise AI Project Optimizer

## Overview

AI system to optimize enterprise projects by predicting: project duration, cost, and delay.

## Quick Start with Docker

This project contains:

* **ML API** – Predicts project duration, cost, and delay.
* **Spring Backend** – Consumes ML API and exposes endpoints for integration.

---

## Run All Services

1. Make sure Docker is installed and running.

2. Build and start services:

```
docker-compose up --build

```

3. Services will run on:

* ML API: http://localhost:8000/docs (Swagger UI)
* Spring Backend: http://localhost:8080

Docker Compose handles networking between the ML API and Spring backend automatically.


## API Endpoints

The project has two servers: **ML API** and **Spring Backend**.

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
Send this JSON as a POST request to http://localhost:8000/predict_full.
---

### Spring Backend Endpoints

Spring backend wraps the ML API and provides these endpoints:

Method | Endpoint           | Description
-------|------------------|-------------
GET   | /predict           | Predict project duration, cost, and delay via JSON

**Example JSON for `/predict`:**

```json
{
  "team_size": 5,
  "issues": 2
}
```
Send this JSON as a GET request to http://localhost:8080/predict.

---

## Notes

* ML models (*.pkl) are already included in the repo for API usage.
* projects.db is generated automatically and ignored in GitHub.
* Make sure ports 8000 (ML API) and 8080 (Spring backend) are free before running.

