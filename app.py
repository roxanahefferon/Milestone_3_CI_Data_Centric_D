import os
import json
from flask import Flask, render_template, request, flash, url_for, redirect, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

""" App configuration
"""

app = Flask(__name__)

""" MongoDB configuration
"""

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

""" DB Collections
"""

users_coll = mongo.db.users
recipes_coll = mongo.db.recipe
categories_coll = mongo.db.categories

""" User Authentication - Login
"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html", recipe=mongo.db.recipe.find().sort("recipe_name"))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route("/add_recipe")
def add_recipe():
    return render_template("login.html")


@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for("recipes"))


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editRecipe.html', recipe=the_recipe, categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'category_name': request.form.get('category_name'),
        'recipe_description': request.form.get('recipe_description'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'servings': request.form.get('servings'),
        'cook_time': request.form.get('cook_time')
    })
    return redirect(url_for('recipes'))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("recipes"))



@app.route("/login")
def login():
    return render_template("login.html", view_name="Login",
        categories=mongo.db.categories.find(),
        difficulty=mongo.db.difficulty.find())


@app.route("/courses", methods=["POST"])
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
