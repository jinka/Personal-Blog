from flask_wtf import FlaskForm
from .forms import ReviewForm,UpdateProfile
from .. import db

from wtforms.validators import Required,Email
from ..models import User

from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
# from wtforms.validators import 
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about you.',validators = [Required()])
    submit = SubmitField('Submit')

