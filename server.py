from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
app.run(debug=True)
