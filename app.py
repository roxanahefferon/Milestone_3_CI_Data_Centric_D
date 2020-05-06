import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/add_own")
def add_own():
    return render_template("add_own.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)