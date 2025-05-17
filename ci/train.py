import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

df = pd.read_csv('dataset/cars.csv')
X = df.drop(columns='price')
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

os.makedirs('outputs', exist_ok=True)
joblib.dump(value=model, filename='outputs/linear_model.pkl')
