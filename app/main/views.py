from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user
from ..models import User
from .forms import LoginForm,RegistrationForm
from . import main
from flask import Flask
from flask_login import login_required
from urllib import request
import json
import threading


# basic route
@main.route("/")
@login_required
def index():
   # threading.Timer(5.0, printit).start()
   response = request.urlopen('http://quotes.stormconsultancy.co.uk/random.json')

   if response.code==200:
      read_Data=response.read()

      JSON_object = json.loads(read_Data.decode('UTF-8'))
      print(JSON_object)
      author = JSON_object['author']
      id = JSON_object['id']
      quote = JSON_object['quote']
      permalink = JSON_object['permalink']

      head = "Welcome to my Blog"
      # return render_template('index.html',head=head)
      return render_template("index.html", head = head, author = author, id = id, quote = quote, permalink = permalink)