from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
@app.route("/filmsy")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/book")
def book():
    return render_template("book.html")


