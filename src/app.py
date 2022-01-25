import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

local_path = 'http://127.0.0.1:5000'
local_host = '127.0.0.1'
local_port = 5000

if os.environ.get("ENV") and os.environ.get("ENV") == "PROD":
   local_path = 'https://crime-ut-data-class.herokuapp.com'
   local_host = '0.0.0.0'
   local_port = os.environ.get("PORT")

@app.route("/")
def home():
   data = {
      'path': local_path,
   }
   return render_template("home.html", data=data)

@app.route("/about")
def about():
   data = {
      'path': local_path,
      'paul': {
         'description': "Paul Westmore is a Senior Software Engineer at Mobile Tech RX (Repairify, Inc). He has been part of Mobile Tech RX's team since its earliest days and has been part of it growing from a small startup to it accepting a Series A funding round from Silverton Partners in 2019, and then its eventual acquisition by Repairify, Inc in 2021.",
         'gh': "https://github.com/pswestmore72",
         'linked': "www.linkedin.com/in/paul-westmore-a11040a9",
      },
      'chris': {
         'description': "",
         'gh': "",
         'linked': "",
      },
      'stuart': {
         'description': "",
         'gh': "",
         'linked': "",
      },
      'moez': {
         'description': "",
         'gh': "",
         'linked': "",
      },
   }
   return render_template("about.html", data=data)

@app.route("/food")
def food():
   data = {
      'path': local_path,
   }
   return render_template("food.html", data=data) 

@app.route("/weather")
def weather():
   data = {
      'path': local_path,
   }
   return render_template("weather.html", data=data)   

@app.route("/machine-learning")
def ml():
   data = {
      'path': local_path,
   }
   return render_template("machine_learning.html", data=data)

if __name__ == "__main__":
   app.run(debug=False, port=local_port, host=local_host)