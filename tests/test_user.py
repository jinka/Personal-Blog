from app.models import User, Post, Comment
from app import db

def setUp(self):
        self.user_Daud = User(username = 'Daud',password = 'password', email = 'daudi@ms.com')
        self.new_review = User(user_id=12345,username='jinka'user = self.user_Daud )

def tearDown(self):
        Review.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_user_name,'ali')
        self.assertEquals(self.new_[password],'12345')
