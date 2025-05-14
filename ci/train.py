import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv("ci/data/cars_dataset.csv")
X = df[["year", "mileage", "engine_size", "horsepower", "brand_score"]]
y = df["sold_price"]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")
print("Model trained on 67% data and saved as model.pkl")
