import datetime
from flask import render_template,redirect,url_for, flash,request,abort
from . import main
from ..models import User
from flask_login import current_user,login_required
from .. import db,photos
from .forms import UpdateProfile


# from flask import Flask
# from .forms import LoginForm,RegistrationForm
# from flask_login import current_user,login_required


from urllib import request
import json
import threading


# basic route
@main.route('/about')
def about():
    title="Welcomr to about me"
    return render_template('about.html',title=title)

@main.route('/')

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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))