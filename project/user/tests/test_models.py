# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from mongoengine import ValidationError
from flask_bcrypt import check_password_hash
from flask_login import current_user, login_user
from project.tests.base import MVCTestCase
import project.user.models as umodels
from project.user.services.create_user_service import CreateUserService
from project.user.services.reset_user_password_service import ResetUserPasswordService
from project.user.services.delete_user_service import DeleteUserService


class UserModelTestCase(MVCTestCase):

    def setUp(self):
        super(UserModelTestCase, self).setUp()
        self.user = self.create_user(username="username", password=b"password")

    def test_user_representation(self):
        """Ensure user object __repr__, __str__ are returning correct values"""
        self.assertEqual(str(self.user), self.user.username)
        self.assertEqual(repr(self.user), "<User: {}>".format(str(self.user)))

    def test_user_creation_method_and_model_fields(self):
        """Ensure when creating a User Object that the method used to create
        the user assigns all fields correctly"""
        user = CreateUserService(username="my_username", password=b"my_password").call()
        self.assertEqual(user.username, "my_username")
        self.assertTrue(check_password_hash(user.password, "my_password"))

    def test_reset_password(self):
        """Ensure the reset password method is actually updating the password
        to the given one"""
        self.assertTrue(check_password_hash(self.user.password, "password"))
        ResetUserPasswordService(self.user, "newpassword").call()
        self.user.save()
        self.user.reload()
        self.assertFalse(check_password_hash(self.user.password, "password"))
        self.assertTrue(check_password_hash(self.user.password, "newpassword"))

    def test_delete_user(self):
        """Ensure delete method is not actually deleting the editor, but only
        deletes it from the database if the flag "force" is given"""
        self.assertEqual(1, umodels.User.objects.count())
        DeleteUserService(self.user).call()
        self.assertEqual(0, umodels.User.objects.count())
        self.assertEqual(1, umodels.User._objects.count())
        DeleteUserService(self.user, force=True).call()
        self.assertEqual(0, umodels.User.objects.count())
        self.assertEqual(0, umodels.User._objects.count())
