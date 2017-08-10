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
    query = "SELECT * FROM users WHERE email = :email"
    email = mysql.query_db(query)
    if email is request.form['email']:
        return redirect('/wall', email)
    else:
        return redirect('/', message = "Invalid Login: Please register")
@app.route('/register', methods =['POST'])
def register():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/login')
@app.route('/wall')
def load(user_id):
    pass
app.run(debug=True)
