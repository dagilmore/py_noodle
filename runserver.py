__author__ = 'dagilmore'

from flask import Flask
from flask.ext.assets import Environment
from database import init_db
from py_noodle.blog.controller import blog


app = Flask(__name__)

#Create assets
assets = Environment(app)

#register base view controller
app.register_blueprint(blog, url_prefix='')

#use config file for configuration details
app.config.from_object('config')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
