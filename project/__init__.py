# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
import os

from flask import Flask
from pymongo import MongoClient


def get_cpw_db():
    host = os.environ.get("MONGO_CPW_URL")
    dbname = os.environ.get("MONGO_CPW_NAME")

    client = MongoClient(host, connect=False)
    db = client.get_database(dbname)

    return db


def get_unbabel_db():
    host = os.environ.get("MONGO_UNBABEL_URL")
    dbname = os.environ.get("MONGO_UNBABEL_NAME")

    client = MongoClient(host, connect=False)
    db = client.get_database(dbname)

    return db


def get_zendesk_db():
    host = os.environ.get("MONGO_ZENDESK_URL")
    dbname = os.environ.get("MONGO_ZENDESK_NAME")

    client = MongoClient(host, connect=False)
    db = client.get_database(dbname)

    return db


def get_customer_reporting_db():
    host = os.environ.get("MONGO_CUSTOMER_REPORTING_URL")
    dbname = os.environ.get("MONGO_CUSTOMER_REPORTING_NAME")

    client = MongoClient(host, connect=False)
    db = client.get_database(dbname)

    return db


def read_env(app, config_class):
    """config environment variables and override with .env declared ones.
    use configuration given by environment variable APP_ENV if "config_class"
    is not given"""
    from flask_dotenv import DotEnv
    env = DotEnv()
    env.init_app(app)
    # get all new .env variable and add them to os.environ dict
    os.environ.update(map(lambda x: (x[0], str(x[1])), app.config.iteritems()))
    # get correct APP_ENV and right variable
    if config_class is None:
        from config import config as c
        config_class = c.get(app.config.get('APP_ENV'))
    app.config.from_object(config_class)
    return app


def create_app(config=None):
    app = Flask(__name__)
    # read .envs and configuration class
    app = read_env(app, config)

    # define logging patterns
    import logging  # %(pathname)
    if app.config.get("TESTING"):
        log_format = ("[%(asctime)s] %(funcName)s:%(lineno)d "
                      "%(levelname)s - %(message)s")
        log_level = logging.DEBUG

    else:
        log_format = ("[%(asctime)s] {%(filename)s#%(funcName)s:%(lineno)d} "
                      "%(levelname)s - %(message)s")
        log_level = logging.INFO

    formatter = logging.Formatter(log_format)
    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)
    # remove default Flask debug handler
    del app.logger.handlers[0]

    # setup apps
    from flask_rq import RQ
    from flask_bcrypt import Bcrypt
    from flask_debugtoolbar import DebugToolbarExtension

    DebugToolbarExtension(app)
    Bcrypt(app)
    RQ(app)

    # register view blueprints
    from project.reporting.views import app_blueprint
    from project.admin.views import admin_blueprint

    app.register_blueprint(app_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # jinja extensions
    app.jinja_env.add_extension('jinja2.ext.do')

    return app

__version_info__ = ('1', '0', '0')
__author__ = "andresilva"
__email__ = "andre@unbabel.com"
