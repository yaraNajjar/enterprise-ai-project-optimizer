from fastapi import FastAPI
import joblib
from db.database import SessionLocal
from db.models import Project
from pydantic import BaseModel
from db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project Predictor API")

class ProjectInput(BaseModel):
    team_size: int
    issues: int



# Load the duration prediction model
model = joblib.load("models/duration_model.pkl")

@app.post("/predict_duration")
def predict_duration(team_size: int, issues: int):
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
delay_model = joblib.load("models/delay_model.pkl")

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
cost_model = joblib.load("models/cost_model.pkl")

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

def save_project(team_size, issues, duration, cost, delay):
    db = SessionLocal()
    project = Project(
        team_size=team_size,
        issues=issues,
        predicted_duration=duration,
        predicted_cost=cost,
        delay_risk=delay
    )
    db.add(project)
    db.commit()
    db.close()

@app.post("/predict_full")
def predict_full(input: ProjectInput):
    team_size = input.team_size
    issues = input.issues

    duration = model.predict([[team_size, issues]])[0]
    cost = cost_model.predict([[team_size, issues]])[0]
    delay = delay_model.predict([[team_size, issues]])[0]

    save_project(team_size, issues, duration, cost, delay)

    return {
        "team_size": team_size,
        "issues": issues,
        "predicted_duration": round(duration, 2),
        "predicted_cost": round(cost, 2),
        "delay_risk": bool(delay)
    }


@app.get("/projects")
def get_projects():
    """
    Retrieve all stored project predictions from the database
    """
    db = SessionLocal()
    projects = db.query(Project).all()
    db.close()

    return [
        {
            "id": p.id,
            "team_size": p.team_size,
            "issues": p.issues,
            "predicted_duration": round(p.predicted_duration, 2),
            "predicted_cost": round(p.predicted_cost, 2),
            "delay_risk": bool(p.delay_risk)
        }
        for p in projects
    ]
