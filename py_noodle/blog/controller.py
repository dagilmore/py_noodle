__author__ = 'dagilmore'

import config
from flask import render_template, flash, redirect
from flask import Blueprint, jsonify
from flask import request
from py_noodle.blog import repository

blog = Blueprint('blog', __name__, template_folder='templates')

@blog.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@blog.route('/hello_world', methods=['GET'])
def hello_world():
    """
    Simple GET request that returns 'Hello world!' in a JSON message.
    """
    response = jsonify({'message': 'Hello world!'})
    return response

@blog.route('/')
@blog.route('/index')
def index():
    """
    GET request returns site index
    """
    return render_template("index.html",
        title='Home',
    )


@blog.route('/music/')
def music():
    """
    Render the music static page
    """

    return render_template('music.html',
        title='Music',
    )

@blog.route('/contact/')
def contact():
    """
    Render the music static page
    """

    return render_template('contact.html',
        title='Contact',
    )

@blog.route('/contact/', methods='POST')
def contact_post():
    """
    Render the music static page
    """
    return render_template('contact.html',
        title='Contact',
    )

@blog.route('/tech/about', methods=['GET'])
def about():
    """
    The about page
    """
    return render_template('about.html',
        title='About',
    )

@blog.route('/tech/<category>', methods=['GET'])
def get_tech_blog(category):
    """
    Get a tech blog by category

    GET simply returns login form.

    """
    posts = repository.get_blogs_by_category(category)

    return render_template('blog.html',
        title=category,
        posts=posts,
    )

@blog.route('/tech/<category>', methods=['POST'])
def create_tech_blog(category):
    """
    :param title:
    :param slug:
    :param category:
    :param body:
    :return:
    """
    # try:
    #     repository.save(request.form)
    # except KeyError:
    #     redirect(
    #         'tech/{0}'.format(category),
    #         message='An error occurred'
    #     )
    return True
