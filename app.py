from flask import Flask, render_template, request, url_for
app = Flask(__name__)

import joblib
import sklearn

#Import pre-trained model
model = joblib.load("./model/dbs.jl")


@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/dbs", methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

if __name__ == "__main__":
    app.run()