__author__ = 'dagilmore'

import os
import tempfile

import unittest
from runserver import app
from database import init_db
from py_noodle.blog import repository
from py_noodle.blog.models import Blog

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

    def test_save_blog(self):
        """
        Save a blog
        """
        blog = Blog(
            title='the title',
            slug='the-title',
            category='buzz',
            body='yo python is dope',
        )
        repository.save(blog)

    def test_list_all_blogs(self):
        """
        List blogs
        """
        blogs = repository.list_all_blogs()

    def test_list_all_blogs__limit(self):
        """
        List specified amount of blogs
        """
        repository.list_all_blogs(30)

    def test_get_blogs_by_category(self):
        """
        List blogs by category
        """
        repository.list_all_blogs()

    def test_get_blogs_by_category__(self):
        """
        List specified amount of blogs by category
        """
        repository.list_all_blogs()

    def test_get_blog_by_title(self):
        """
        Get blog by title
        """
        repository.get_blog_by_title('title')


if __name__ == '__main__':
    unittest.main()