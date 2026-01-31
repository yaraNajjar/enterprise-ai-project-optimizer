from fastapi.testclient import TestClient
from unittest.mock import patch
from api import app

client = TestClient(app)

# ----------------------------
# predict_full
# ----------------------------
@patch("api.save_project")
@patch("api.model.predict")
@patch("api.cost_model.predict")
@patch("api.delay_model.predict")
def test_predict_full(mock_delay, mock_cost, mock_duration, mock_save):
    mock_duration.return_value = [10]
    mock_cost.return_value = [5000]
    mock_delay.return_value = [1]

    response = client.post("/predict_full", json={
        "team_size": 5,
        "issues": 2
    })

    assert response.status_code == 200

    data = response.json()
    assert data["predicted_duration"] == 10
    assert data["predicted_cost"] == 5000
    assert data["delay_risk"] is True

# ----------------------------
# predict_duration
# ----------------------------
@patch("api.model.predict")
def test_predict_duration(mock_predict):
    mock_predict.return_value = [7]

    response = client.post("/predict_duration?team_size=3&issues=1")

    assert response.status_code == 200
    assert response.json()["predicted_duration_days"] == 7

# ----------------------------
# predict_cost
# ----------------------------
@patch("api.cost_model.predict")
def test_predict_cost(mock_predict):
    mock_predict.return_value = [2000]

    response = client.post("/predict_cost?team_size=3&issues=1")

    assert response.status_code == 200
    assert response.json()["predicted_cost"] == 2000

# ----------------------------
# predict_delay
# ----------------------------
@patch("api.delay_model.predict")
def test_predict_delay(mock_predict):
    mock_predict.return_value = [0]

    response = client.post("/predict_delay?team_size=3&issues=1")

    assert response.status_code == 200
    assert response.json()["delay_risk"] is False
