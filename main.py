from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)

account={'username':"Nishi","Password":"Hello","email":"nishi@gmail.com"}
@app.route("/")
@app.route("/filmsy")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("profile.html",account=account)

@app.route("/book")
def book():
    return render_template("book.html")

@app.route("/login",methods=['POST','GET'])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

