<h1>MILESTONE 3 - CODE INSTITUTE</h1>
<h2>Overview</h2>
A web application created in Python and Flask. 
View website on <a href="https://milestone3-data-centric.herokuapp.com/" target="_blank">Heroku</a>
A recipe database where viewers can search and view recipes. 
Users can also add, edit or delete their own recipes.
<h2>UX</h2>
This website was created with the intention to store and share recipes with other users. The home page shows the recipes categories, and allows the user to choose between Breakfast, Lunch, Dinner and Snacks. When clicking on any category, the user can view a list of recipes from that specific category. The user can choose a specific recipe from the list where it will be displayed more details about the recipe such as: Category, Serving, Time of preparation, difficulty level, ingredients and cooking method. This page also allows the user to delete or edit the recipe. On the navbar the user have access to all recipes, without categories. There's also a link that brings to a form to add a new recipe.
<h2>Features</h2>
<ul>
<li>Create new recipes - recipe name, category, level of difficulty, servings, preparation time, method, ingredients.</li>
<li>Read recipes</li>
<li>Edit recipes</li>
<li>Delete recipes</li>
</ul>
<h2>Technologies Used</h2>
<ul>
<li><a href ="https://getbootstrap.com/" target="_blank">Bootstrap</a></li>
Bootstrap is the most popular CSS Framework for developing responsive and mobile-first websites.
<li><a href="https://www.python.org/" target="_blank">Python</a></li>
<p> An interpreted, high-level, general-purpose programming language.
<li><a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">Flask</a></li>
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
<li><a href="https://www.mongodb.com/" target="_blank">MongoDB</a></li>
A general purpose, document-based, distributed database built for modern application developers and for the cloud era.
<li><a href="https://flask-pymongo.readthedocs.io/en/latest/>" target="_blank">Flask-Pymongo</a></li>
Flask-PyMongo bridges Flask and PyMongo and provides some convenience helpers.
<li><a href="https://materializecss.com/" target="_blank">Materialize</a></li>
A modern responsive front-end framework based on Material Design.
</ul>
<h2>Testing</h2>
All the CRUD actions were tested and are working as it should.   
The responsiveness was tested on every page. 
Every link was tested and works properly. 
All forms handle empty input fields.
<h2>Deployment</h2>

Deployment and source control was carried out via GitHub and Heroku. Following steps were taken to deploy the website:
1.	Database was created in MongoDB Atlas.
2.	Project workspace was created in GitPod. In this workspace: Flask was installed - pip3 install flask.
3.	Setup app.py file and imported flask and os - from flask import Flask. import os
4.	Created an instance of flask - app = flask(__name__)
5.	Inside the app run() function set the host, ip and debug=true
6.	Create a new Heroku App - unique name and EU Server
7.	In GitPod login to Heroku through CLI to confirm existance of app. CLI: heroku login. 
8.	gitpod /workspace/M3-CI-DCD $ heroku login -i
9.	heroku: Enter your login credentials
10.	Email: roxana.hefferon@gmail.com
11.	Password: **********
12.	CLI: heroku apps.
13.	Create a git repository in GitPod. CLI: git init. CLI: git add . CLI: git commit -m "Initial Commit"
14.	Connect GitPod to Heroku. Use code found on Heroku. CLI - $heroku git remote -a 
15.	Create requirements.txt file - CLI: pip3 freeze --local > requirements.txt
16.	Create Procfile - echo web:python app.py>Procfile
17.	Add and Commit to Git Repository
18.	Push to Heroku using code supplied by Heroku
19.	CLI - heroku ps:scale web=1 Command to tell Heroku to run the app
20.	Log in to Heroku to add config variables including IP, Port, Mongo_DB and Mongo_URI. 
<ul><li>Set Config Vars adding IP and PORT on Heroku app settings</li>
<li>IP 0.0.0.0 - PORT 5000</li></ul>
21.	Get Flask to talk to MongoDB - CLI: pip3 install flask-pymongo CLI: pip3 install dnspython
22.	Add extra libraries to app.py - from flask_pymongo import Pymongo from bson.objectid import ObjectID
23.	Add DB connection code to app.py
24.	Test connection to DB again to confirm it's working
25.	Connect GitHub repository to Heroku using code provided by heroku and github.
26.	Set Debug to False
Install the Heroku CLI
Download and install the Heroku CLI.
If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
$ heroku login
Create a new git repository
Initialize a git repository in a new or existing directory
$ cd my-project/
$ git init
$ heroku git:remote -a data-centric-m3-ci
Deploy your application
Commit your code to the repository and deploy it to Heroku using Git.
$ git add .
$ git commit -am "make it better"
$ git push heroku master
________________________________________
Existing Git repository
For existing repositories, simply add the heroku remote
$ heroku git:remote -a data-centric-m3-ci

<h2>Colour Scheme</h2>

<ul>
<li>#FFFEFE</li>
<li>#F2A535</li>
<li>#2A2A2A</li>
<li>#979797</li>
<li>#F8CD8E</li>
</ul>


<h2>Credits</h2>
<p>Logo created in <a href="https://www.canva.com/">Canva</a></p>
<p>Favicon created in <a href="https://www.favicon-generator.org/">Favicon</a></p>
<p>Images <a href="www.unsplash.com">Unsplash</a></p>
<ul>
<li> <a href="https://unsplash.com/@brookelark?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank">Brooke Lark</a></li>
<li> <a href="https://unsplash.com/@foodiesfeed?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank">Jakub Kapusnak</a> </li>
<li> <a href="https://unsplash.com/@lvnatikk?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank">Lily Banse</a></li>
<li> <a href="https://unsplash.com/@imaxpanama?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank">Max Panamá</a></li>
<h2>MongoDB</h2>
<p>recipe_manager.recipe</p>
{"_id":{"$oid":"5eb53ab9f5a3f431259becc4"},
"category_name":"",
"recipe_name":"",
"recipe_description":"",
"is_vegetarian":"",
"ingredientes":"",
"method":"",
"servings":"",
"difficulty":"",
"cook_time":""
}
<p>recipe_manager.categories</p>
{"_id":{"$oid":"5eb5d6014faee9a32d0ebe3e"},
"category_name":"
<p>recipe_manager.difficulty</p>
{"_id":{"$oid":"5eb5da874faee9a32d0ebe41"},
"difficulty_level":""}"}
<p>recipe_manager.users</p>
{"_id":{"$oid":"5eb5d7624fahe9a90d0ele7e"},
"username":"",
"password":""}"}



