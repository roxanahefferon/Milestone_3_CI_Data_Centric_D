import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


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


@app.route("/recipes")
def recipes():
    return render_template("recipes.html", view_name="Recipes")


@app.route("/add_own")
def add_own():
    return render_template("add_own.html", view_name="Add your own recipe")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)