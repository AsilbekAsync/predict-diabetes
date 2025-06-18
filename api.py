from flask import Flask, request, render_template, jsonify
from brain import get_result
app = Flask(__name__)


@app.get('/')
def show_form():
    return render_template('form.html')

@app.post("/result")
def show_result():
    required_fields = [
        "pregnancies", "glucose", "bloodPressure", "skinThickness",
        "insulin", "bmi", "diabetesPedigree", "age"
    ]
    errors = {}

    for field in required_fields:
        if field not in request.form or request.form[field].strip() == "":
            errors[field] = "Bu maydon to`ldirilishi shart"

    try:
        preg = int(request.form["pregnancies"])
        if not (0 <= preg <= 20):
            errors["pregnancies"] = "0—20 oralig`ida bo`lishi kerak"
    except:
        errors["pregnancies"] = "Butun son bo`lishi kerak"

    try:
        glu = int(request.form["glucose"])
        if not (40 <= glu <= 200):
            errors["glucose"] = "40—200 oralig`ida bo`lishi kerak"
    except:
        errors["glucose"] = "Butun son bo`lishi kerak"

    try:
        bp = int(request.form["bloodPressure"])
        if not (40 <= bp <= 140):
            errors["bloodPressure"] = "40—140 oralig`ida bo`lishi kerak"
    except:
        errors["bloodPressure"] = "Butun son bo`lishi kerak"

    try:
        skin = float(request.form["skinThickness"])
        if not (7 <= skin <= 99):
            errors["skinThickness"] = "7—99 oralig`ida bo`lishi kerak"
    except:
        errors["skinThickness"] = "Raqamli qiymat bo`lishi kerak"

    try:
        ins = int(request.form["insulin"])
        if not (15 <= ins <= 900):
            errors["insulin"] = "15—900 oralig`ida bo`lishi kerak"
    except:
        errors["insulin"] = "Butun son bo`lishi kerak"

    try:
        bmi = float(request.form["bmi"])
        if not (10 <= bmi <= 70):
            errors["bmi"] = "10—70 oralig`ida bo`lishi kerak"
    except:
        errors["bmi"] = "Raqamli qiymat bo`lishi kerak"

    try:
        dpf = float(request.form["diabetesPedigree"])
        if not (0 <= dpf <= 2):
            errors["diabetesPedigree"] = "0—2 oralig`ida bo`lishi kerak"
    except:
        errors["diabetesPedigree"] = "Raqamli qiymat bo`lishi kerak"

    try:
        age = int(request.form["age"])
        if not (10 <= age <= 120):
            errors["age"] = "10—120 oralig`ida bo`lishi kerak"
    except:
        errors["age"] = "Butun son bo`lishi kerak"

    if errors:
        return jsonify({"status": "error", "errors": errors}), 400
    
    data = [
        preg,
        glu,
        bp,
        skin,
        ins,
        bmi,
        dpf,
        age
    ]

    result = get_result(data)
    return render_template(
        'result.html',
        data = data,
        result = result['prediction'],
        probability = result['probability']
    )

if __name__ == '__main__':
    app.run(debug=True)