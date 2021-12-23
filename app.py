#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


@app.route("/")
def index():
    # persons = persons.spis
    return render_template('index.html')
    #return "Hello World"


@app.route("/result",methods = ['POST', 'GET'])
def final():
    if request.method == 'POST':
        separator = request.form['separator']
        result = request.form['content']
        if separator:
            result = list(set(result.split(f"{separator}")))
        else:
            result = list(set(result.split()))
        #result = list(set(result.split(f"{separator}")))
        return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True) 
