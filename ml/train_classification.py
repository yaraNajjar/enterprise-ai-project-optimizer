import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Reading the data
data = pd.read_csv("projects.csv")

# Select features (inputs)
X = data[["team_size", "issues"]]

# Select target (output)
y = data["delay"]

# Split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

# Test the accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Classification Accuracy: {accuracy*100:.2f}%")

# Save the model
joblib.dump(model, "delay_model.pkl")
print("Delay classification model saved")
