from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

if __name__ == "__main__":
   app.run()