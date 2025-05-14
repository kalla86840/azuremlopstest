import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

df = pd.read_csv("ci/data/cars_dataset.csv")
X = df[["year", "mileage", "engine_size", "horsepower", "brand_score"]]
y = df["sold_price"]

model = joblib.load("model.pkl")
predictions = model.predict(X)

rmse = mean_squared_error(y, predictions, squared=False)
r2 = r2_score(y, predictions)

print(f"RMSE: {rmse:.2f}")
print(f"R^2 Score: {r2:.2f}")
