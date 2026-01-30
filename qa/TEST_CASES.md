# TEST_CASES.md
# Enterprise AI Project Optimizer - Test Cases

| ID     | Feature                 | Steps                                                                 | Expected Result                                  |
|--------|------------------------|----------------------------------------------------------------------|-------------------------------------------------|
| TC-01  | Predict project         | 1. Open frontend<br>2. Enter Team Size = 5<br>3. Enter Issues = 3<br>4. Click Predict | Prediction returned with duration, cost, delay |
| TC-02  | Invalid input           | Enter Team Size = -1, Issues = 2, Click Predict                       | Validation error shown / No API call made      |
| TC-03  | Projects list           | Call `/projects` API                                                  | Saved projects returned as a JSON list         |
| TC-04  | Frontend rendering      | Open frontend                                                          | Form fields "Team Size", "Issues", Predict button appear |
| TC-05  | API fetch (mocked)      | Mock API call with Vitest                                             | Component receives correct JSON data           |
| TC-06  | Integration end-to-end  | Enter inputs in frontend → Spring → ML API → DB                       | Prediction persisted in DB and returned to UI  |
