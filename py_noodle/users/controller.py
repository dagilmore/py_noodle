__author__ = 'dagilmore'

import config
from flask import (
    render_template,
    request,
    Blueprint,
    redirect,
    session,
    url_for,
    flash,
    g,
)

users = Blueprint('user', __name__, template_folder='templates')

@users.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != config.USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != config.PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect('/')
    return render_template('login.html', error=error)


@users.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect('/')