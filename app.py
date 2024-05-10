import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

# Connect to the phpMyAdmin database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Define a function to insert data into the database
def insert_data(name, email):
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql, val)
    mydb.commit()

# Define a route to display a form for adding new data
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to process form data and insert it into the database
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    insert_data(name, email)
    return 'Data added successfully!'

if __name__ == '__main__':
    app.run(debug=True)
