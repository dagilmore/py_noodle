__author__ = 'dgilmore'

from flask import Flask
from nose.tools import eq_

import json
import unittest

from py_noodle.views import base


class PyNoodleTests(unittest.TestCase):
    """
    Test base package views
    """
    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(base, url_prefix='')
        app.config['TESTING'] = True
        self.app = app.test_client()

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

    def test_login(self):
        pass

if __name__ == '__main__':
    unittest.main()