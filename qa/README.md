# QA Documentation – Enterprise AI Project Optimizer

This document describes all testing layers implemented in the project,
how to run them, and what each test validates.

--------------------------------------------------
1. Project Architecture (High Level)
--------------------------------------------------

Frontend (React)
   ↓
Spring Boot Backend
   ↓
FastAPI ML Service
   ↓
SQLite Database

--------------------------------------------------
2. Testing Types Covered
--------------------------------------------------

✔ Manual Testing
✔ API Testing
✔ Integration Testing
✔ Basic Automation
✔ Frontend Component Testing
✔ ML API Testing

--------------------------------------------------
3. ML API Tests (FastAPI)
--------------------------------------------------

Location:
ml/tests/test_ml_api.py

What is tested:
- POST /predict_full
- GET /projects
- Response structure
- HTTP status codes

How to run:
1. Start ML API:
   docker-compose up ai-api

2. Run tests:
   pytest ml/tests/

--------------------------------------------------
4. Spring Boot Backend Tests
--------------------------------------------------

Location:
spring-backend/src/test/

What is tested:
- Backend context loads
- Endpoints work correctly
- Communication with ML API

How to run:
cd spring-backend
mvn test

--------------------------------------------------
5. Frontend Tests (React)
--------------------------------------------------

Location:
frontend/src/App.test.jsx

What is tested:
- UI renders correctly
- Predict button exists
- API calls are mocked
- Prediction results are displayed

How to run:
cd frontend
npm test

--------------------------------------------------
6. Integration Testing
--------------------------------------------------

Test Flow:
React → Spring Boot → FastAPI → Database

Validated:
- Data flows correctly across services
- Predictions are persisted
- Services communicate through Docker network

Documentation:
qa/INTEGRATION_TESTS.md

--------------------------------------------------
7. Postman API Testing
--------------------------------------------------

Location:
qa/postman/

Tested APIs:
- /predict_full
- /projects

Validated:
- Status codes
- Required response fields
- Data consistency

--------------------------------------------------
8. Known Issues & Bug Tracking
--------------------------------------------------

Documented in:
qa/BUG_REPORTS.md

Includes:
- Docker networking issues
- Port conflicts
- API connection errors
- Environment configuration problems

--------------------------------------------------
9. Conclusion
--------------------------------------------------

This project demonstrates a full QA mindset:
- Clear documentation
- Realistic bugs
- Automation where needed
- End-to-end validation