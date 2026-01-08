import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

#Load data
data = pd.read_csv("projects.csv")

X = data[["team_size", "issues"]]

y = data["duration"]

model = LinearRegression()

model.fit(X, y)

joblib.dump(model, "duration_model.pkl")

print("Model trained and saved successfully")
print("Coefficients:", model.coef_)
