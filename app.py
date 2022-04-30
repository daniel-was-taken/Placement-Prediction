import imp
from tkinter.font import names
from tkinter.tix import Tree
from tokenize import String
from unicodedata import name
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb
import numpy as np
import pickle

loaded_model = pickle.load(open("placement.pkl", "rb"))

app = Flask(__name__)

app.secret_key = "12345"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "admin"
app.config["MYSQL_DB"] = "login"

db = MySQL(app)

@app.route("/", methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'email' in request.form and 'password' in request.form:
            username = request.form['email']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM logininfo WHERE email=%s AND password=%s",(username,password))
            info = cursor.fetchone()
            print(info)
            
            if info is not None:
                if info['email'] == username and info['password'] == password:
                    pinfo = cursor.execute("SELECT name FROM logininfo WHERE email=%s AND password=%s",(username,password))          
                    pinfo = cursor.fetchone()
                    print(pinfo)
                    names = pinfo['name']     
                    session['loginsuccess'] = True
                    session['username'] = names
                    return redirect(url_for('profile', names=names))
                else:
                  flash('Check Credentials')
                  return redirect(url_for('index'))
    
    return render_template("login.html")
    
@app.route('/first')
def first():
    names  = session['username']
    return redirect(url_for('profile', names=names))


@app.route('/new/profile/')
def profile():
    if session['loginsuccess'] == True:  
        names = request.args['names']
        fname = names.upper()
        return render_template('profile.html',fname = fname)

@app.route('/index/')
def toPredict():
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


@app.route('/register')
def new_user1():
    return render_template("register.html")


@app.route('/new', methods=['GET','POST'])
def new_user():
    if request.method == 'POST':
      if "name" in request.form and "email" in request.form and "password" in request.form:
          name = request.form['name']  
          username = request.form['email'] #email
          password = request.form['password']  
          cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
          cur.execute("INSERT INTO login.logininfo (name,email,password) VALUES (%s,%s,%s)",(name,username,password))
          db.connection.commit()
          return redirect(url_for('index'))

    return render_template('register.html')
   

@app.route('/new/logout')
def logout():
    session.pop('loginsuccess', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run()