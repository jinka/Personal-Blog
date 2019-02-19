import datetime
from flask import render_template,redirect,url_for, flash,request,abort
from . import main
from ..models import User,Blog,Comment
from flask_login import current_user,login_required
from flask_user import roles_required
from .. import db,photos
from .forms import UpdateProfile,PostForm,CommentForm


# from urllib import request
import urllib.request, json
# import json
import threading


# basic route
@main.route('/about')
def about():
    title="Welcome to about me"
    return render_template('about.html',title=title)

@main.route('/')

@main.route("/")
# @login_required
def index():
   # threading.Timer(5.0, printit).start()
   response = urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json')

   if response.code==200:
      read_Data=response.read()

      JSON_object = json.loads(read_Data.decode('UTF-8'))
      print(JSON_object)
      author = JSON_object['author']
      id = JSON_object['id']
      quote = JSON_object['quote']
      permalink = JSON_object['permalink']

      head = "Welcome to my Blog"
  
      blogs = Blog.query.all()
  

      return render_template("index.html", blogs=blogs, head = head, author = author, id = id, quote = quote, permalink = permalink)

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

@main.route('/user/<uname>/update/pic',methods= ['GET', 'POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/post/new',methods = ['GET','POST'])
@login_required
def new_post():

    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        post = post_form.text.data
        category = post_form.category.data
        new_post = Blog(blog_title=title,blog_content=post,category=category,user=current_user,likes=0,dislikes=0)

        new_post.save_blog()

        return redirect(url_for('.index'))
    title = 'New Blog'
    return render_template('new_post.html',title = title,post_form=post_form )


@main.route('/post/<int:id>', methods = ['GET','POST'])

def post(id):
    comment_form = CommentForm()
    blogs = Blog.query.filter_by(id=id).first

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment= Comment(comment=comment,user=current_user)
        db.session.add(comment)
        db.session.commit()

    comments=Comment.query.filter_by(id=id).all()
    return render_template("blog.html", blogs=blogs, comments=comments,comment_form=comment_form)

  
@main.route('/user/<uname>/posts')
def user_posts(uname):

    user = User.query.filter_by(username=uname).first()
    posts = Post.query.filter_by(user_id = user.id).all()
    posts_count = Post.count_posts(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')
    return render_template("new_post.html", user=user,posts=posts,posts_count=posts_count,date = user_joined)

