from flask import Flask, render_template, request
import pandas as pd
import predictor

app = Flask("My-app")

@app.route("/")
def page():
    return render_template("chacha.taya")


@app.route("/submit", methods=["post"])
def submit_form():
    quote = request.form["quote"]
    
    ans = predictor.predict(quote)

    return ans


