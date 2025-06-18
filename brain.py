import pandas as pd
import joblib

scaler = joblib.load('model/scaler.joblib')
model = joblib.load('model/model.joblib')
median_values = joblib.load('model/imputer.joblib')

X_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 
             'DiabetesPedigreeFunction', 'Age']
ZERO_COLS = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

def get_result(arr):
    arr = arr.copy()
    for i, col in enumerate(X_columns):
        if col in ZERO_COLS and arr[i] == 0:
            arr[i] = median_values[col]

    input_df = pd.DataFrame([arr], columns=X_columns)
    input_scaled = scaler.transform(input_df)
    
    prediction = model.predict(input_scaled)[0]
    return {
        'prediction': bool(prediction)
    }
