__author__ = 'dagilmore'

from py_noodle.blog.models import Post
from py_noodle.blog import repository
from database import Base

def initialize_posts():
    for x in xrange(10):
        post = Post(
            title='the title {0}'.format(x),
            slug='the-title-{0}'.format(x),
            category='buzz',
            body='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
        )
        repository.save(post)