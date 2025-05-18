
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

# Resolve path to cars.csv
script_dir = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(script_dir, '..', 'cars.csv'))

# Features and target
X = df.drop('sale_price', axis=1).select_dtypes(include=['number'])
y = df['sale_price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.joblib')

print("Training completed and model saved to 'model.joblib'")
