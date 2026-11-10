#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


@app.route("/")
def index():
    # persons = persons.spis
    return render_template('index.html')
    #return "Hello World"

@app.route("/result", methods=["POST", "GET"])
def final():
    if request.method == "POST":
        separator = request.form.get("separator", "")
        content = request.form.get("content", "")
        if separator:
            result = list(set(content.split(separator)))
        else:
            result = list(set(content.split()))
        return render_template("result.html", result=result)
    return redirect(url_for("index"))

@app.route("/join", methods=["POST", "GET"])
def join_text():
    if request.method == "POST":
        content = request.form.get("content", "")
        glue = request.form.get("glue", " ")
        if glue == "":
            glue = " "

        # splitlines() ловить і \n, і \r\n
        lines = [line.strip() for line in content.splitlines()]
        result = glue.join(line for line in lines if line)

        return render_template("join_result.html", result=result)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True) 
