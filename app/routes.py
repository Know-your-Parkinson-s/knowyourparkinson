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


@app.route("/reaction/", methods=['GET', 'POST'])
def reaction():
    if request.method == 'POST':
        val = request.get_json()
        session['val'] = val
        print(val)
    ua = request.headers.get('User-Agent')
    device = SoftwareDetector(ua).parse()
    age = session['age']
    return render_template('reaction.html',
                           age=age,
                           ua=device.os_name(),
                           title='Reaction')


@app.route("/test/", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        data = request.get_json()
        if 'values' in data:
            session['val'] = data['values']
            print(data)
        if 'score' in data:
            session['score'] = data['score']
            print(data)
    return render_template('test.html', title='Symptom Tracker')


@app.route("/tremor/", methods=['GET', 'POST'])
def tremor():
    ua = request.headers.get('User-Agent')
    device = SoftwareDetector(ua).parse()
    return render_template('tremor.html', title='Tremor')


@app.route("/results/")
def results():
    age = session['age']
    score = session['score']
    val = session['val']
    avg = statistics.mean(val)
    if avg < 200:
        pass
    elif avg < 350:
        score += 1
    elif avg < 450:
        score += 2
    elif avg < 550:
        score += 3
    elif avg < 650:
        score += 4
    else:
        score += 5

    return render_template(
        'results.html',
        title='Results',
        score=score,
    )


if __name__ == '__main__':
    app.run()
