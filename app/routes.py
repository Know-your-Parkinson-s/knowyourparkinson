from app import app
from flask import render_template, request, redirect, url_for, session
import requests
import json
import statistics
from device_detector import SoftwareDetector


@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = request.form.get('ageGroup')
        session['age'] = age
        return redirect(url_for('test'))
    return render_template("index.html", title='Home')


@app.route("/test/", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        data = request.get_json()
        if 'values' in data:
            session['val'] = data['values']
        if 'motorScore' in data:
            session['motor'] = data['motorScore']
            session['mental'] = data['mentalScore']
            session['other'] = data['other']
        if 'percent' in data:
            session['percent'] = data['percent']
    return render_template('test.html', title='Symptom Tracker')


@app.route("/results/")
def results():
    age = session['age']
    motor = session['motor']
    mental = session['mental']
    other = session['other']

    resultText = "Thank you for taking the test!"

    return render_template('results.html',
                           title='Results',
                           motor=motor,
                           mental=mental,
                           other=other,
                           resultText=resultText)


if __name__ == '__main__':
    app.run()
