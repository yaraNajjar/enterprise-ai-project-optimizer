# Test Cases – Enterprise AI Project Optimizer

| ID     | Feature                | Steps | Expected Result | Test Type |
|--------|-----------------------|-------|-----------------|-----------|
| TC-01  | Predict project        | Open frontend → Enter values → Predict | Prediction returned | Manual / E2E |
| TC-02  | Invalid input          | Enter negative team size | Validation error | Manual |
| TC-03  | Projects list          | Call /projects API | JSON list returned | API |
| TC-04  | Frontend rendering     | Open frontend | UI renders correctly | UI |
| TC-05  | API fetch (mocked)     | Mock API with Vitest | Correct data received | Unit |
| TC-06  | Integration end-to-end | Full system flow | Data saved & returned | Integration |
