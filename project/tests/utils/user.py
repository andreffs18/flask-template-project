# !/usr/bin/python
# -*- coding: utf-8 -*-
from project.user.services.create_user_service import CreateUserService


class UserTestUtils(object):

    def setUp(self):
        super(UserTestUtils, self).setUp()

    @staticmethod
    def create_user(username=None, password=None, is_admin=False):
        """
        Aux test method that creates user from given arguments
        """
        if username is None:
            username = "username"
        if password is None:
            password = b"password"

        kwargs = dict([
            ("username", username),
            ("password", password),
            ("is_admin", is_admin)
        ])
        return CreateUserService(**kwargs).call()
