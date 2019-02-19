from flask_wtf import FlaskForm

from wtforms.validators import Required,Email
from ..models import User

from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
# from wtforms.validators import 
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):

    title = StringField('New Blog',validators=[Required()])
    text = TextAreaField('Text',validators=[Required()])
    category = SelectField('Type',choices=[('ISP','Isp Blog'),('IPTV','IPTV Blog'),('Python','Python Blog')],validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')

