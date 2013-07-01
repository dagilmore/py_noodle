__author__ = 'dagilmore'

from flask import Flask
from flask.ext.assets import Environment
from database import init_db
from py_noodle.blog.controller import blog
from py_noodle.users.controller import users
from py_noodle.users import login_manager


app = Flask(__name__)

#Create assets
assets = Environment(app)

#register base view controller
app.register_blueprint(blog, url_prefix='')
app.register_blueprint(users, url_prefix='/users')

#use config file for configuration details
app.config.from_object('config')

#configure app for login
login_manager.init_app(app)

if __name__ == '__main__':
    init_db()
    app.run()
