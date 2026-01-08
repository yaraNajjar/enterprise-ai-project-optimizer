import joblib

model = joblib.load("duration_model.pkl")

team_size = 6
issues = 4

predicted_duration = model.predict([[team_size, issues]])

print(f"Predicted project duration: {predicted_duration[0]:.2f} days")
