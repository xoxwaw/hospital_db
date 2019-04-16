import os
import sys

from flask import Flask, session, render_template, request,redirect, url_for, flash, make_response
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from jinja2 import Environment, PackageLoader, select_autoescape
import csv

env = Environment(
    loader=PackageLoader('server', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)

# #Set the DATABASE_URL
# DATABASE_URL = ""
# # Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
#
# # Set up database
# engine = create_engine(DATABASE_URL)
# # db = scoped_session(sessionmaker(bind=engine))
# conn = engine.connect()

@app.route('/', methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

@app.route("/profile", methods = ["GET"])
def profile():
    template = env.get_template('profile.html')
    return template.render()
@app.route("/search", methods = ["POST"])
def search():
    return

@app.route("/createProcedure", methods = ["POST"])
def createProcedure():
    return

@app.route("/createPatient", methods = ["POST, GET"])
def createPatient():
    return

@app.route("/createStaff", methods = ["POST", "GET"])
def createStaff():
    return

@app.route("/staff/<s_id>", methods = ["GET"])
def staff(s_id):
    return

@app.route("/patient/<p_id>", methods = ["GET"])
def patient(p_id):
    return
