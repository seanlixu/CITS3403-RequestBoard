from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/userdashboard")
def userDashboard():
    return render_template("userDashboard.html")