# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
__author__ = "andresilva"
__email__ = "andre@unbabel.com"
from project import app
from flask.ext.dotenv import DotEnv
env = DotEnv()
env.init_app(app, verbose_mode=True)


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = app.config["SECRET_KEY"]
    MONGODB_SETTINGS = {
        "DB": app.config.get("MONGO_DB_NAME", "default")
    }

    # Custom db credentials
    MONGODB_ALIAS = None
    MONGODB_DB = None
    MONGODB_HOST = None
    MONGODB_PASSWORD = None
    MONGODB_PORT = None
    MONGODB_USERNAME = None

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLE = False
    MONGODB_SETTINGS = {
        "DB": app.config.get("MONGO_DB_NAME_TEST", "default-test")
    }


class LocalhostConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config = {
    '_baseconfig': BaseConfig,
    'localhost': LocalhostConfig,
    'test': TestConfig,
    'production': ProductionConfig,
}

__all__ = ['config']