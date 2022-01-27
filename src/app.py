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
         'description': "Paul Westmore is a Senior Software Engineer at Mobile Tech RX (Repairify, Inc).Paul is currently enrolled in the Data Analysis and Visualization Boot Camp through UT's McCombs School of Business (partnered with Trilogy Education Services).",
         'gh': "https://github.com/pswestmore72",
         'linked': "https://www.linkedin.com/in/paul-westmore-a11040a9",
      },
      'chris': {
         'description': "Christopher Garcia is an aspiring data analyst and graduated with an undergraduate degree in mathematics from the University of Houston. Chris is also currently in the Data Analysis and Visualization Boot camp at University of Texas-Austin",
         'gh': "https://github.com/ChristopheGarcia1",
         'linked': "https://www.linkedin.com/in/christopher-garcia-979670213/",
      },
      'stuart': {
         'description': "Stuart Wilson Description Coming Soon",
         'gh': "https://github.com/PSWil",
         'linked': "https://www.linkedin.com/in/stuart-wilson-9a6234214/",
         'tableau': "https://public.tableau.com/app/profile/stuart.wilson2140",
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