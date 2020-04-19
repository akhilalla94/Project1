import os
import time
import sys

from sqlalchemy import create_engine,desc
from flask import Flask, session, render_template, request
from users import *

app = Flask(__name__,static_url_path='/static')


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return "<h1>Register</h1>"

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/userDetails",methods=["POST","GET"])
def userDetails():
    userName = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("pwd")  
    obj = user.query.filter_by(username = userName).first()
    if obj is None:
        usr = user(username = userName, email = email, password = password, time = time.ctime(time.time()))
        db.session.add(usr)
        db.session.commit()
    else:
        print()
        return render_template("registration.html", message = "email already exists.")

    return render_template("user.html", username = userName) 

@app.route("/admin")
def admin():
    adm = user.query.order_by(desc(user.time)).all()
    return render_template("admin.html", adm = adm)