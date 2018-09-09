# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask import current_app as app
from flask_script import Command
from project.database import init_db, drop_db


class CreateDBCommand(Command):
    """
    Creates all tables from registered models
    """
    def run(self, **kwargs):
        app.logger.info("Running {} with arguments {}".format(self.__class__.__name__, kwargs))
        self.__dict__.update(**kwargs)  # update self's with kwargs
        drop_db(app)
        init_db(app)
