<h1>MILESTONE 3 - CODE INSTITUTE</h1>
<h2>Overview</h2>
A web application created in Python and Flask.
<h2>UX</h2>
This website was created with the intention to store and share recipes with other users. The home page shows the recipes categories, and allows the user to choose between Breakfast, Lunch, Dinner and Snacks. When clicking on any category, the user can view a list of recipes from that specific category. The user can choose a specific recipe from the list where it will be displayed more details about the recipe such as: Category, Serving, Time of preparation, difficulty level, ingredients and cooking method. This page also allows the user to delete or edit the recipe. On the navbar the user have access to all recipes, without categories. There's also a link that brings to a form to add a new recipe.
<h2>Features</h2>
•	Create new recipes - recipe name, category, level of difficulty, servings, preparation time, method, ingredients.
•	Read recipes
•	Edit recipes
•	Delete recipes
Technologies Used
•	Bootstrap
o	CSS framework to style and create responsive design
•	Python
•	Flask
o	Python microframework
•	MongoDB
o	NoSQL database
•	MLab
o	MongoDB cloud database service where the data is stored
•	Flask-Pymongo
o	Connects Flask to MongoDB
<h2>Testing</h2>
All the CRUD actions were tested and are working as it should. When updating a recipe the same is duplicated, this will be fixed later. I've added a delete button on the card so it can be deleted easily instead of the need to go to the recipe page to do so. The responsiveness was tested on every page. Every link was tested and works properly. All forms handle empty input fields.
<h2>Deployment</h2>
There are four things needed in order to push our code to Heroku.
1.	Firstly, we need to create a Heroku app.
2.	Secondly, we need to link our local Git repository to Heroku, 
3.	Thirdly, we need to create a requirements.txt file, which contains a list of our dependencies.
4.	And finally, we need to create a Procfile, which is a special kind of file that tells Heroku how to run our project.
Deployment and source control was carried out via GitHub and Heroku. Following steps were taken to deploy the website:
1.	Database were created in an Atlas MongoDB account
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
20.	Log in to Heroku to add config variables including IP, Port, Mongo_DB and Mongo_URI. Set Config Vars adding IP and PORT on Heroku app settings
IP 0.0.0.0 - PORT 5000
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
Create a new Git repository
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

#FFFEFE
#F2A535
#2A2A2A
#979797
#F8CD8E
Fonts: Norwester | Montserrat Classic

<h2>Credits</h2>
Logo created in <a href="https://www.canva.com/">Canva</a>
Favicon created in <a href="https://www.favicon-generator.org/">Favicon</a>
Images <a href="www.unsplash.com">Unsplash</a>
<ul>
<li>Courses|Breakfast <a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px" href="https://unsplash.com/@brookelark?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Brooke Lark"><span style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span style="display:inline-block;padding:2px 3px">Brooke Lark</span></a></li>
<li>Courses|Lunch <a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px" href="https://unsplash.com/@foodiesfeed?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Jakub Kapusnak"><span style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span style="display:inline-block;padding:2px 3px">Jakub Kapusnak</span></a> </li>
<li>Courses|Dinner <a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px" href="https://unsplash.com/@lvnatikk?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Lily Banse"><span style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span style="display:inline-block;padding:2px 3px">Lily Banse</span></a></li>
<li>Courses|Dessert <a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px" href="https://unsplash.com/@imaxpanama?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Max Panamá"><span style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span style="display:inline-block;padding:2px 3px">Max Panamá</span></a></li>
<h2>MongoDB</h2>
{"_id":
	{"$oid":"5eb53ab9f5a3f431259becc4"},
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

<h2></h2>
<h2></h2>

