__author__ = 'dgilmore'

from flask import Flask
from py_noodle.views import base

app = Flask(__name__)

#register base view controller
app.register_blueprint(base, url_prefix='')

#use config file for configuration details
app.config.from_object('config')

app.run()