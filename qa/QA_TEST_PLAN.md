# QA Test Plan – Enterprise AI Project Optimizer

## 1. ML API Tests
Service: FastAPI (Python)

- Endpoint: POST /predict_full
- Endpoint: GET /projects
- Validations:
  - predicted_duration exists
  - predicted_cost exists
  - delay_risk exists
- Tool: pytest + requests

## 2. Spring Backend Tests
Service: Spring Boot (Java)

- Endpoint: GET /predict/{teamSize}/{issues}
- Endpoint: GET /projects
- Validations:
  - HTTP status codes
  - JSON response structure
- Tool: JUnit / Spring Boot Test

## 3. Frontend Tests
Service: React (Vite)

- Render prediction form
- Button interaction (Predict)
- API calls mocked
- Tool: Vitest + React Testing Library

## 4. Integration Testing
End-to-End Flow:

React → Spring Boot → FastAPI → SQLite

- Validate prediction flow
- Validate data persistence
- Validate error handling between services
