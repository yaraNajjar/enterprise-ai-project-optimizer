# QA Documentation – Enterprise AI Project Optimizer

This document summarizes all QA processes implemented in the project, including testing layers, how to run them, and what they validate.

--------------------------------------------------
## 1. Project Architecture

Frontend (React)
↓
Spring Boot Backend
↓
FastAPI ML Service
↓
SQLite Database

--------------------------------------------------
## 2. Testing Types Covered

- Manual Testing
- API Testing
- Integration Testing
- Basic Automation
- Frontend Component Testing
- ML API Testing
- Postman / Newman Automation

--------------------------------------------------
## 3. ML API Tests (FastAPI)

**Location:** `ml/tests/test_ml_api.py`

**What is tested:**
- POST `/predict_full`
- GET `/projects`
- Response structure
- HTTP status codes

**How to run:**
1. Start ML API: `docker-compose up ai-api`
2. Run tests: `pytest ml/tests/`

--------------------------------------------------
## 4. Spring Boot Backend Tests

**Location:** `spring-backend/src/test/`

**What is tested:**
- Backend context loads
- Endpoints work correctly
- Communication with ML API

**How to run:**
```bash
cd spring-backend
mvn test
```
--------------------------------------------------
## 5. Frontend Tests (React)

Location: frontend/src/App.test.jsx

**What is tested:**
- UI renders correctly
- Predict button exists
- API calls are mocked
- Prediction results are displayed

**How to run:**
```bash
cd frontend
npm test
```

--------------------------------------------------
## 6. Integration Testing

Test Flow: React → Spring Boot → FastAPI → Database

**Validated:**
- Data flows correctly across services
- Predictions are persisted
- Services communicate through Docker network

Documentation: qa/INTEGRATION_TESTS.md

--------------------------------------------------
## 7. Postman API Testing & Automation

Location: qa/postman/Enterprise_AI_Project_Optimizer.postman_collection.json

**Tested APIs:**
- POST /predict_full
- GET /projects

**Validated:**
- Status codes
- Required response fields
- Data consistency

**How to run manually:** Open the collection in Postman and click "Run".

**How to run automatically using Newman:**
1. Install Newman globally: 
```bash
npm install -g newman
```
2. Run tests: 
```bash
newman run qa/postman/Enterprise_AI_Project_Optimizer.postman_collection.json
```
3. **Expected Result:** All requests return HTTP 200 and all assertions pass successfully

--------------------------------------------------
## 8. Test Cases

**Documentation:** qa/TEST_CASES.md

Includes:
- TC-01 → Predict project
- TC-02 → Invalid input
- TC-03 → Projects list
- TC-04 → Frontend rendering
- TC-05 → API fetch (mocked)
- TC-06 → Integration end-to-end

--------------------------------------------------
## 9. Known Issues & Bug Tracking

**Documentation:** qa/BUG_REPORTS.md

Includes:
- Docker networking issues
- Port conflicts
- API connection errors
- Environment configuration problems
- Historical bugs with fixes (Spring, ML API, Frontend)

--------------------------------------------------
## 10. Conclusion

This project demonstrates a full QA mindset:
- Clear and detailed documentation
- Realistic bugs and resolutions
- Manual + Automated testing
- End-to-end integration validation
- Postman/Newman automation for continuous checks
