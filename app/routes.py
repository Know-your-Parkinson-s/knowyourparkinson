import json

import requests
from device_detector import SoftwareDetector
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from app import app


@app.route("/", methods=["GET", "POST"])
@app.route("/index/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["testNo"] = 1
        testNo = session.get("testNo", None)
        return redirect(url_for("tests", tNo=testNo))
    return render_template("index.html", title="Home")


@app.route("/tests/<tNo>", methods=["GET", "POST"])
def tests(tNo):
    if request.method == "POST":
        testNo = session.get("testNo", None)
        testNo += 1
        session["testNo"] = testNo
        if testNo < 5:
            return redirect(url_for("tests", tNo=testNo))
        else:
            return redirect(url_for("results"))
    age = request.form.get("ageGroup")
    print(age)
    return render_template("tests.html", age=age, tNo=tNo)


@app.route("/results/")
def results():
    return render_template("results.html")


@app.route("/reaction/")
def reaction():
    ua = request.headers.get("User-Agent")
    device = SoftwareDetector(ua).parse()
    return render_template("reaction.html", ua=device.os_name())


if __name__ == "__main__":
    app.run()
