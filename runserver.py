from flask import Flask
from py_noodle.views import base

app = Flask(__name__)
app.register_blueprint(base, url_prefix='')
app.config.from_object('config')

app.run(debug=True)