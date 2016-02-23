# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""

from project import app
from project.user.models import User
from flask.ext.testing import TestCase


class BaseTestCase(TestCase):
    """Default base test case"""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        user = User(email="admin@unbabel.com", username="admin", password="admin")
        user.save()

    def tearDown(self):
        pass