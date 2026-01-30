# Integration Testing – Enterprise AI Project Optimizer

## 1. System Architecture

Frontend (React)  
↓  
Spring Boot Backend  
↓  
FastAPI ML Service  
↓  
Prediction Response

---

## 2. Services & Ports

| Service   | Tech        | Port |
|-----------|------------|------|
| Frontend  | React/Vite | 5173 |
| Backend   | Spring Boot| 8080 |
| ML API    | FastAPI    | 8000 |

---

## 3. Integration Test Scenario

### Scenario: Predict Project Outcome

#### Preconditions
- Frontend running
- Spring Boot running
- ML API running

#### Steps
1. User enters team size and issues in frontend
2. Frontend sends request to Spring:
   ```
   /predict/{teamSize}/{issues}
   ```
3. Spring sends POST request to ML API:
   ```
   /predict_full
   ```
4. ML API returns prediction
5. Spring forwards response to frontend
6. Frontend displays prediction

#### Expected Result
- HTTP 200 OK
- JSON contains:
  - `predicted_duration`
  - `predicted_cost`
  - `delay_risk`

---

## 4. Known Integration Issues

### Issue 1: ML API Not Running
**Error:**
```
Connection refused: http://localhost:8000
```

**Cause:** FastAPI service not started  

**Solution:**
```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

---

### Issue 2: uvicorn Command Not Found (Windows)
**Cause:** uvicorn not installed or virtual environment not activated  

**Solution:**
```bash
pip install uvicorn fastapi
```
or
```bash
python -m uvicorn main:app --port 8000
```

---

### Issue 3: Docker Hostname Mismatch
**Symptom:** Spring uses:
```
http://ai-api:8000
```
while running locally

**Solution:** Use:
```
http://localhost:8000
```
for local development

---

## 5. Integration Test Status

| Component | Status |
|-----------|--------|
| Frontend  | ✅ Pass |
| Backend   | ✅ Pass |
| ML API    | ✅ Pass |
| Full Flow | ✅ Pass |
