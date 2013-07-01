__author__ = 'dagilmore'

from flask import (
    render_template,
    Blueprint,
    jsonify,
    request,
    session,
    abort,
)
from py_noodle.blog import (
    repository,
    service,
)

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

@blog.route('/tech/<category>/', methods=['GET'])
def get_posts_by_category(category):
    """
    Get a tech blog by category

    GET simply returns login form.

    """
    posts = repository.get_posts_by_category(category)

    if posts:
        return render_template('blog.html',
            title=category,
            posts=posts,
        )
    else:
        return render_template('page_not_found.html',
            title='Oops',
        )

@blog.route('/create_posts/', methods=['GET', 'POST'])
def create_posts():
    """
    Create posts
    :return:
    """
    if not session.get('logged_in'):
        abort(401)
    if request.method == 'GET':
        return render_template('create_post.html')
    elif request.method == 'POST':
        service.save(request.form)
        return render_template('create_post.html')