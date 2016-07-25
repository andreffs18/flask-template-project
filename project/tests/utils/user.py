# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from flask import current_app as app
from flask.ext.bcrypt import generate_password_hash
import project.user.models as umodels


class UserTestUtils(object):

    def setUp(self):
        """"""
        super(UserTestUtils, self).setUp()

    @staticmethod
    def create_user(username=None, password=None, email=None, is_admin=False):
        """Aux test method that creates user from given arguments"""
        if username is None:
            username = "username"
        if password is None:
            password = "password"
        if email is None:
            email = username + "@test.com"

        kwargs = dict([
            ("username", username),
            ("password", generate_password_hash(password)),
            ("email", email),
            ("is_admin", is_admin)
        ])
        return umodels.User.create(**kwargs)