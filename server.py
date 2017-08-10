from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')
@app.route('/')
# query = "SELECT * FROM users"
# users = mysql.query_db(query)
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email=request.form['email']
    print email
    query = "SELECT * FROM users WHERE email = :specific_id"
    data = {"specific_id":email}
    response = mysql.query_db(query,data)
    print response[0]['email']

    
    if response[0]['email'] == email:
        return redirect('/wall')
    else:
        return redirect('/')
@app.route('/register', methods =['POST'])
def register():
    print "HEY LISTEN!"
    
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    print query
    data = {"first_name": request.form['first_name'], "last_name": request.form['last_name'], "email": request.form['email']}
    print "im tryin to print:",data

    print mysql.query_db(query, data)
    
    # print "im about to redirect"
    return redirect('/')
@app.route('/wall')
def wall():
    return render_template("wall.html")
app.run(debug=True)
