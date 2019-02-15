from flask_script import Manager,Server
from app import create_app
from flask import Flask

# app = Flask(__name__)
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app)


if __name__ == "__main__":
   app.run()