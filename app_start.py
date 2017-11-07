#!/usr/bin/env python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.html")

app.run(host='0.0.0.0', debug=True)
