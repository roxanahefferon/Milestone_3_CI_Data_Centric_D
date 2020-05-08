import os
import json
from flask import Flask, render_template, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI') 

app.secret_key = "grubs_key"

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html", recipe=mongo.db.recipe.find())

@app.route("/add_recipe")
def add_recipe():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html", view_name="Register")


@app.route("/login")
def login():
    return render_template("login.html", view_name="Login")


@app.route("/courses")
def courses():
    data = []

    with open("data/categories.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("courses.html", view_name="Courses", categories=data)


@app.route('/courses/<option_name>')
def courses_option(option_name):
    option = {}
    with open("data/categories.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == option_name:
                option = obj

    return render_template("selected.html", option=option)


@app.route('/get_in_touch', methods=["GET", "POST"])
def get_in_touch():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("get_in_touch.html", page_title="Get_in_touch")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)