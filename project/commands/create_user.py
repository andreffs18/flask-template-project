# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask import current_app as app
from flask_script import Command, Option
from project.user.services.create_user_service import CreateUserService


class CreateUserCommand(Command):
    """
    Creates user by giving username and password
    """

    def __init__(self):
        super(CreateUserCommand, self).__init__()
        self.username = None
        self.password = None

    def get_options(self):
        return [
            Option('-u', '--username', dest='username', default=self.username),
            Option('-p', '--password', dest='password', default=self.password),
        ]

    def run(self, **kwargs):
        app.logger.info("Running {} with arguments {}".format(self.__class__.__name__, kwargs))
        self.__dict__.update(**kwargs)  # update self's with kwargs
        try:
            CreateUserService(self.username, self.password).call()
            app.logger.info("User \"{}\" was successfully created!".format(self.username))
        except Exception as e:
            app.logger.error("Something went wrong :s. {}".format(e))
