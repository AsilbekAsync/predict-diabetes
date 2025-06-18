import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer
from imblearn.over_sampling import SMOTE
import joblib
import os

os.makedirs('model', exist_ok=True)
df = pd.read_csv('data/data.csv')

ZERO_COLS = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for col in ZERO_COLS:
    df[col] = df[col].astype(float)

df[ZERO_COLS] = df[ZERO_COLS].replace(0, np.nan)

imputer = KNNImputer(n_neighbors=5)
df[ZERO_COLS] = imputer.fit_transform(df[ZERO_COLS])

X = df.drop(columns=['Outcome'])
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_resampled, y_resampled)

cv_scores = cross_val_score(model, X_resampled, y_resampled, cv=5)
print(f"Cross-validation accuracy: {cv_scores.mean():.4f}")

test_score = model.score(X_test_scaled, y_test)
print(f"Test set accuracy: {test_score:.4f}")

joblib.dump(scaler, 'model/scaler.joblib')
joblib.dump(imputer, 'model/imputer.joblib')
joblib.dump(model, 'model/model.joblib')
