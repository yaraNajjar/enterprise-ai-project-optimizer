# BUG_REPORTS.md
# Enterprise AI Project Optimizer - Bugs Log

| ID   | Component        | Description                                                      | Steps to Reproduce                                              | Status / Fix / Note                                    |
|------|-----------------|------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------|
| BUG-01 | Spring Backend   | `spring-boot:run` failed: No plugin found for prefix 'spring-boot' | Run `mvn spring-boot:run` without spring-boot plugin configured | Fixed by adding spring-boot-maven-plugin in pom.xml    |
| BUG-02 | Frontend / React | React tests failing after migrating jest → vitest                | Run `vitest` on `App.test.jsx`                                 | Fixed by updating `jest.fn()` → `vi.fn()` and imports  |
| BUG-03 | Spring → ML API  | `UnknownHostException: ai-api`                                   | Run Spring and call `/predict` API without ML running          | Fixed by running ML API on localhost and updating BASE_URL |
| BUG-04 | ML API / Python  | `uvicorn: command not found`                                      | Run `uvicorn main:app --port 8000`                             | Install uvicorn (`pip install uvicorn`)                |
| BUG-05 | Frontend / React | `getByLabelText` failing                                          | Render `<App />` and check `screen.getByLabelText(/Team Size/i)` | Fixed by adding `htmlFor="teamSize"` to `<label>`      |
| BUG-06 | Integration      | Spring POST to ML fails with Connection refused                  | Call `/predict` API while ML API not running                  | Start ML API on port 8000 before Spring               |
| BUG-07 | Spring Backend   | 500 Internal Server Error                                         | POST `/predict` when ML API down                               | Add error handling / alert user / log exception       |
