# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask_restful import Resource
from project.user.handlers.user_api_handler import UserApiHandler


class User(Resource):
    """
    API interface to manipulate User Model
    """

    @staticmethod
    def get():
        """
        Get list of users
        """
        users = UserApiHandler.get_list_of_users()
        return {"users": users}, 200
