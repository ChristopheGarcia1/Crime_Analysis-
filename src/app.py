from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/about")
def about():
   data = {
      'paul': {
         'description': "",
         'gh': "",
         'linked': "",
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
   return render_template("about.html", authors=data)

@app.route("/food")
def food():
   return render_template("food.html") 

@app.route("/weather")
def weather():
   return render_template("weather.html")   

@app.route("/machine-learning")
def ml():
   return render_template("machine_learning.html")

if __name__ == "__main__":
   app.run()