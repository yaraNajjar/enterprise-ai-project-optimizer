import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the CSV data
data = pd.read_csv("projects.csv")

# Select features (inputs)
X = data[["team_size", "issues"]]

# Select target (output)
y = data["cost"]

# Create the regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Print model coefficients for inspection
print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)

# Save the trained model
joblib.dump(model, "cost_model.pkl")
print("Cost prediction model saved successfully")
