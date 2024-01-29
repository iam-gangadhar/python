from ast import Num
from nturl2path import url2pathname
from os import name
from flask import Flask, render_template
import random
import datetime
import requests
# from markupsafe import escape



year = datetime.datetime.now()
c_years = year.year

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('index.html', Num=random.randint(10,100), c_year=c_years, y_name="XYZ", p_age="20", y_gen="male/female")

@app.route("/guess/<name>")
def hello(name):
    name_1 = name
    response = requests.get(f"https://api.agify.io?name={name}")
    age = response.json()
    myage = age["age"]
    response2 = requests.get(f"https://api.genderize.io?name={name}")
    gender = response2.json()
    mygender = gender["gender"]
    return render_template('about.html', my_name=name_1, my_age=myage, my_gender=mygender)

@app.route("/blog")
def blog():
    sample_data = requests.get(url="https://api.npoint.io/4b2dbf19469a3eafee12")
    sample_d = sample_data.json()

    return render_template("blog.html", my_data=sample_d)




# @app.route("/<name>")
# def hello(name):
#     name_get = requests.get(url=f"https://api.agify.io?name={name}")
#     name_dict = name_get.json
#     your_age = name_dict["age"]
#     return render_template('index.html',Num=random.randint(10,100), c_year=c_years, p_age=your_age, y_name=name, y_gen="**")




if __name__ == "__main__":
    app.run(debug=True)