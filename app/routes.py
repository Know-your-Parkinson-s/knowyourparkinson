from app import app
from flask import render_template, request, redirect, url_for, session
import requests
import json


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html", title='Home')


@app.route("/tests/", methods=['GET', 'POST'])
def tests():
    age = request.form.get('ageGroup')
    print(age)
    return render_template('tests.html', age=age)


@app.route('/debug-sentry/')
def trigger_error():
    division_by_zero = 1 / 0


if __name__ == '__main__':
    app.run()
