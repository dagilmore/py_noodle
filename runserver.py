__author__ = 'dagilmore'

from flask import Flask
from py_noodle.blog.views import blog
from database import init_db

app = Flask(__name__)

#register base view controller
app.register_blueprint(blog, url_prefix='')

#use config file for configuration details
app.config.from_object('config')

if __name__ == '__main__':
    init_db()
    app.run()
