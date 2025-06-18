from flask import Flask, request, render_template, jsonify
from brain import get_result
app = Flask(__name__)


@app.get('/')
def show_form():
    return render_template('form.html')
@app.post("/result")
def show_result():
    data = [
        int(request.form["pregnancies"]),
        int(request.form["glucose"]),
        int(request.form["bloodPressure"]),
        float(request.form["skinThickness"]),
        int(request.form["insulin"]),
        float(request.form["bmi"]),
        float(request.form["diabetesPedigree"]),
        int(request.form["age"])
    ]

    result = get_result(data)
    return render_template(
        'result.html',
        data = data,
        prediction = result['prediction']
    )

if __name__ == '__main__':
    app.run(debug=True)