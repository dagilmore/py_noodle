__author__ = 'dgilmore'

import config
from flask import render_template, flash, redirect
from flask import Blueprint, jsonify
from forms import LoginForm
from models import Post

base = Blueprint('base', __name__, template_folder='templates')

@base.route('/hello_world', methods=['GET'])
def hello_world():
    """
    Simple GET request that returns 'Hello world!' in a JSON message.
    """
    response = jsonify({'message': 'Hello world!'})
    return response

@base.route('/')
@base.route('/index')
def index():
    """
    GET request returns site index
    """
    user = {'nickname': 'YO YO MA'}
    return render_template("index.html",
        title = 'Home',
        user = user
    )

@base.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login:

    GET simply returns login form.

    POST...
    """
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')

    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = config.OPENID_PROVIDERS
    )

@base.route('/tech/<category>', methods=['GET'])
def get_tech_blog(category):
    """
    Get a tech blog by category

    GET simply returns login form.

    """
    posts = Post.query.filter(Post.category == category).limit(10)

    return render_template('tech_blog.html',
        title=category,
        posts=posts,
    )

@base.route('/tech/<category>', methods=['POST'])
def create_tech_blog(category):
    """

    :param category:
    :return:
    """
    pass