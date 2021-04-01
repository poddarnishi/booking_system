from flask import Flask,render_template,request,url_for,redirect,session
import re
import mysql.connector
import mini_project

app=Flask(__name__)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="nineten910",
  database="BOOKING"
)
cursor = mydb.cursor()
app.secret_key = 'hello123'
account={'username':"Nishi","Password":"Hello","email":"nishi@gmail.com"}
@app.route("/")
@app.route("/filmsy")
@app.route("/home")
def index():

    return render_template("index.html")
@app.route("/profile")
def profile():
    if 'loggedin' in session:
        cursor.execute("Select * from records where email_id= %s",(session['username'],))
        record=cursor.fetchall()
        return render_template("profile.html",account=session,record=record)
    else:
        return render_template("login.html")

@app.route("/book",methods=['GET','POST'])
def book():
    mini_project.genre_recommendations('1917')
    return render_template("book.html")
    
@app.route("/login",methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        username = request.form['email']
        password = request.form['password']
        cursor.execute('SELECT * FROM customer WHERE email_id = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['name'] = account[1]
            session['username'] = account[0]
            session['phone']=account[3]
            return render_template("index.html")
        else:
            msg = 'Incorrect username/password!'
    return render_template("login.html",msg=msg)
@app.route("/register",methods=['POST','GET'])
def register():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form and 'age' in request.form and 'phone' in request.form:
        # Create variables for easy access
        username = request.form['email']
        password = request.form['password']
        name = request.form['name']
        age=request.form['age']
        phone=request.form['phone']
        cursor.execute('SELECT * FROM customer WHERE email_id = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@$%]+', username):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg = 'Username must contain only characters and numbers!'
        elif len(phone)!=9:
            msg='Please enter 9 digit phone number'
        elif not username or not password or not name:
            msg = 'Please fill out the form!'
        else:
            age=int(age)
            phone=int(phone)
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO customer VALUES (%s, %s, %s,%s,%s)', (username,name, password,phone,age))
            mydb.commit()
            return render_template("index.html")
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('login.html', msg=msg)
@app.route('/pythonlogin/logout',methods=['POST','GET'])
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(debug=True)

