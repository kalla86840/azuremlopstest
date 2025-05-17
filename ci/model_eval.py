import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv('dataset/cars.csv')
X = df.drop(columns='price')
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = joblib.load('outputs/linear_model.pkl')
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')
