QA Testing for Enterprise AI Project Optimizer

1. ML API Tests
   - /predict_full
   - /projects
   - Validate predicted_duration, predicted_cost, delay_risk

2. Spring Backend Tests
   - /predict/{teamSize}/{issues}
   - /projects
   - Validate JSON responses

3. Frontend Tests
   - Render prediction form
   - Button interactions
   - API calls (mocked)

4. Integration Testing
   - End-to-end scenario: React → Spring → ML API → DB
   - Validate predictions are persisted in DB
