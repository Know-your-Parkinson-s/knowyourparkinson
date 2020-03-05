from app import app
from flask import render_template, request, redirect, url_for, session
import requests
import json


@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['testNo'] = 1
        testNo = session.get('testNo', None)
        return redirect(url_for('tests', tNo=testNo))
    return render_template("index.html", title='Home')


@app.route("/tests/<tNo>", methods=['GET', 'POST'])
def tests(tNo):
    if request.method == 'POST':
        testNo = session.get('testNo', None)
        testNo += 1
        session['testNo'] = testNo
        if testNo < 5:
            return redirect(url_for('tests', tNo=testNo))
        else:
            return redirect(url_for('results'))
    age = request.form.get('ageGroup')
    print(age)
    return render_template('tests.html', age=age, tNo=tNo)


@app.route("/results/")
def results():
    return render_template('results.html')


@app.route('/debug-sentry/')
def trigger_error():
    division_by_zero = 1 / 0


if __name__ == '__main__':
    app.run()
