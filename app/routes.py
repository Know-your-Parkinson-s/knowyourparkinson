from app import app
from flask import render_template, request, redirect, url_for, session
import requests
import json
from device_detector import SoftwareDetector


@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = request.form.get('ageGroup')
        session['age'] = age
        return redirect(url_for('reaction'))
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
    val = []
    return render_template('reaction.html',
                           age=age,
                           val=val,
                           ua=device.os_name(),
                           title='Reaction')


@app.route("/tremor/", methods=['GET', 'POST'])
def tremor():
    if request.method == 'POST':
        val = request.get_json()
        session['val'] = val
        print(val)
    ua = request.headers.get('User-Agent')
    device = SoftwareDetector(ua).parse()
    age = session['age']
    val = session['val']
    return render_template('tremor.html',
                           age=age,
                           val=val,
                           ua=device.os_name(),
                           title='Tremor')


@app.route("/results/")
def results():
    return render_template('results.html', title='Results')


if __name__ == '__main__':
    app.run()
