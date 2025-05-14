import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv('data/cars.csv')
X = df.drop('sale_price', axis=1)._get_numeric_data()
y = df['sale_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
joblib.dump(model, 'outputs/model.pkl')
