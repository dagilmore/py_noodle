__author__ = 'dagilmore'

import os
import tempfile

import unittest
from runserver import app
from database import init_db
from py_noodle.blog import repository
from py_noodle.blog.models import Post

class PyNoodleRepositoryTests(unittest.TestCase):
    """
    Base package unit tests
    """
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_save_post(self):
        """
        Save a post
        """
        post = Post(
            title='the title',
            slug='the-title',
            category='buzz',
            body='yo python is dope',
        )
        repository.save(post)

    def test_list_all_post(self):
        """
        List posts
        """
        posts = repository.list_all_posts()

    def test_list_all_posts__limit(self):
        """
        List specified amount of posts
        """
        repository.list_all_posts(30)

    def test_get_posts_by_category(self):
        """
        List posts by category
        """
        repository.list_all_posts()

    def test_get_posts_by_category__(self):
        """
        List specified amount of posts by category
        """
        repository.get_posts_by_category('buzz')

    def test_get_post_by_title(self):
        """
        Get post by title
        """
        repository.get_post_by_title('title')


if __name__ == '__main__':
    unittest.main()