from sklearn.metrics import accuracy_score
import pandas as pd
import joblib
import numpy as np

model = joblib.load('model/model.joblib')
scaler = joblib.load('model/scaler.joblib')
imputer = joblib.load('model/imputer.joblib')

df = pd.read_csv('data/data.csv')
X = df.drop(columns=['Outcome'])
y = df['Outcome']

ZERO_COLS = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
X[ZERO_COLS] = X[ZERO_COLS].replace(0, np.nan)
X_zero_cols_imputed = imputer.transform(X[ZERO_COLS])
X[ZERO_COLS] = X_zero_cols_imputed

X_scaled = scaler.transform(X)
y_pred = model.predict(X_scaled)
accuracy = accuracy_score(y, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
