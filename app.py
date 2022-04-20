from tkinter.tix import Tree
from unicodedata import name
from flask import Flask, render_template, request
import numpy as np
import pickle

loaded_model = pickle.load(open("placement.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def result():
    data1 = request.form['age']
    data2 = request.form['gender']
    data3 = request.form['stream']
    data4 = request.form['internships']
    data5 = request.form['cgpa']
    data6 = request.form['hbacklog']
    arr = np.array([[data1,data2,data3,data4,data5,data6]])
    pred = loaded_model.predict(arr)
    return render_template('result.html',data = pred)

if __name__ == "__main__":
    app.debug = True
    app.run()