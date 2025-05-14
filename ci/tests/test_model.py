import pandas as pd
from sklearn.linear_model import LinearRegression

def test_model_training():
    df = pd.read_csv("ci/data/cars_dataset.csv")
    X = df[["year", "mileage", "engine_size", "horsepower", "brand_score"]]
    y = df["sold_price"]
    model = LinearRegression()
    model.fit(X, y)
    assert model.coef_ is not None
