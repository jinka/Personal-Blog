from flask import render_template
from . import main
from flask import Flask
from urllib import request
import json
import threading


# basic route
@main.route("/")
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