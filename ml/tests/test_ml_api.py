import requests

BASE_URL = "http://localhost:8000"

def test_predict_full():
    data = {"team_size": 5, "issues": 2}
    response = requests.post(f"{BASE_URL}/predict_full", json=data)
    assert response.status_code == 200
    result = response.json()
    assert "predicted_duration" in result
    assert "predicted_cost" in result
    assert "delay_risk" in result

def test_get_projects():
    response = requests.get(f"{BASE_URL}/projects")
    assert response.status_code == 200
    projects = response.json()
    assert isinstance(projects, list)
