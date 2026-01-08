from fastapi import FastAPI
import joblib

app = FastAPI(title="Project Duration Prediction API")

# Load the duration prediction model
model = joblib.load("duration_model.pkl")

@app.post("/predict")
def predict(team_size: int, issues: int):
    """
    Predict project duration based on team size and number of issues
    """
    duration = model.predict([[team_size, issues]])[0]
    return {
        "team_size": team_size,
        "issues": issues,
        "predicted_duration_days": round(duration, 2)
    }

# Load the delay prediction model
delay_model = joblib.load("delay_model.pkl")

@app.post("/predict_delay")
def predict_delay(team_size: int, issues: int):
    """
    Predict if a project will be delayed
    """
    delay = delay_model.predict([[team_size, issues]])[0]
    return {
        "team_size": team_size,
        "issues": issues,
        "delay_risk": bool(delay)
    }

# Load the cost prediction model
cost_model = joblib.load("cost_model.pkl")

@app.post("/predict_cost")
def predict_cost(team_size: int, issues: int):
    """
    Predict project cost based on team size and number of issues
    """
    cost = cost_model.predict([[team_size, issues]])[0]
    return {
        "team_size": team_size,
        "issues": issues,
        "predicted_cost": round(cost, 2)
    }

