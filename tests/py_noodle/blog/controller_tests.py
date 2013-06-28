__author__ = 'dagilmore'

import os
import tempfile
import json

import unittest
from nose.tools import eq_
from runserver import app
from database import init_db


class PyNoodleViewTests(unittest.TestCase):
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

    def test_hello_world(self):
        """
        Return JSON 'hello world'
        """
        res = self.app.get(
            '/hello_world',
            content_type='application/json'
        )

        res_dict = json.loads(res.data)
        eq_(res.status_code, 200)
        eq_(res_dict['message'], u'Hello world!')

    def test_index(self):
        """
        Render home page appropriately
        """
        res = self.app.get(
            '/',
            content_type='application/json'
        )

        eq_(res.status_code, 200)

    def test_music(self):
        """
        Render home page appropriately
        """
        res = self.app.get(
            '/music/',
            content_type='application/json'
        )

        eq_(res.status_code, 200)

    def test_contact(self):
        """
        Render contact page
        """
        res = self.app.get(
            '/contact/',
            content_type='application/json'
        )

        eq_(res.status_code, 200)

    # def test_contact_create(self):
    #     """
    #     Save a contact to the database
    #     """
    #     res = self.app.post(
    #         '/contact',
    #         content_type='application/json'
    #     )
    #
    #     eq_(res.status_code, 200)

    def test_tech_blog__get_posts(self):
        """
        Render posts appropriately
        """
        res = self.app.get(
            '/tech/test_category',
            content_type='application/json'
        )
        eq_(res.status_code, 200)

    def test_tech_blog__create_posts(self):
        pass


if __name__ == '__main__':
    unittest.main()