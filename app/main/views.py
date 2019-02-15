from flask import render_template
from . import main


# basic route
@main.route("/")
def index():

   head = "Welcome to my Blog"
   return render_template("index.html", head = head)