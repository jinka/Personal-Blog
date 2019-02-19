from app.models import User, Post, Comment
from app import db

def setUp(self):
        self.user_Daud = User(username = 'Daud',password = 'password', email = 'daudi@ms.com')
        self.new_user = User(user_id=12345,username='jinka'user = self.user_Daud )

def tearDown(self):
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_id,12345)
        self.assertEquals(self.new_full_name,'Mike simon')
        self.assertEquals(self.new_user_name,'Mike')
        self.assertEquals(self.new_email,'daud@gmail.com')
        self.assertEquals(self.phone,'077777777')
        self.assertEquals(self.role_id,'111')
        self.assertEquals(self.bio,'aaaa')
        self.assertEquals(self.phone,'077777777')
        self.assertEquals(self.profile_picture,'/static/image/1.jpg')
        self.assertEquals(self.pass_secure,'ccccc')
        self.assertEquals(self.password_hash,'ccccc')
        


