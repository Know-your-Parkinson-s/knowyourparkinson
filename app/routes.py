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
        if 'percent' in data:
            session['percent'] = data['percent']
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
    percent = session['percent']

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

    if int(percent) > 85:
        pass
    elif int(percent) > 70:
        score += 1
    elif int(percent) < 65:
        score += 2
    elif int(percent) < 60:
        score += 3
    elif int(percent) < 50:
        score += 4
    else:
        score += 5

    score = 55 - score

    if age == '30':
        if score > 45:
            resultText = "You're doing as well as you can! Keep up the good work!"
        elif score < 40:
            resultText = "According to our data, your score is not as high as other people your age. You might want to focus on your health a bit more going forward :)"
        else:
            resultText = "Hey there! You scored well enough to be clear of all doubt, but you can be healthier and sharper yet!"

    elif age == '40':
        if score > 40:
            resultText = "You're doing as well as you can! Keep up the good work!"
        elif score < 35:
            resultText = "According to our data, your score is not as high as other people your age. You might want to focus on your health a bit more going forward :)"
        else:
            resultText = "Hey there! You scored well enough to be clear of all doubt, but you can be healthier and sharper yet!"

    else:
        if score > 40:
            resultText = "You're doing as well as you can! Keep up the good work!"
        elif score < 27:
            resultText = "According to our data, your score is not as high as other people your age. You might want to focus on your health a bit more going forward :)"
        else:
            resultText = "Hey there! You scored well enough to be clear of all doubt, but you can be healthier and sharper yet!"

    return render_template('results.html',
                           title='Results',
                           score=score,
                           resultText=resultText)


if __name__ == '__main__':
    app.run()
