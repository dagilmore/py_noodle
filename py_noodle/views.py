import config

__author__ = 'dgilmore'

from flask import render_template, flash, redirect
from flask import Blueprint, jsonify
from forms import LoginForm

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

@base.route('/login', methods = ['GET', 'POST'])
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