# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

if os.path.isfile('.env'):
    load_dotenv('.env', override=True)


class BaseConfig(object):
    DEBUG = False
    TESTING = True
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Set flask admin layout to use container-fluid css
    FLASK_ADMIN_FLUID_LAYOUT = True

    # Database URI
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "True")

    # HTTP Basic Auth for Admin pages
    BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD')

    # Third party services - codacy.com
    # Coverage given by codacy.com. You need to register you project
    # there so they can give you the access token for this functionality
    CODACY_PROJECT_TOKEN = os.getenv("CODACY_PROJECT_TOKEN")


class TestConfig(BaseConfig):
    APP_ENV = "test"
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_PROFILER_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class LocalhostConfig(BaseConfig):
    APP_ENV = "localhost"
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class StagingConfig(BaseConfig):
    APP_ENV = "staging"
    DEBUG = True
    TESTING = False
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class ProductionConfig(BaseConfig):
    APP_ENV = "production"
    TESTING = False


config = {
    '_baseconfig': "config.BaseConfig",
    'localhost': "config.LocalhostConfig",
    'test': "config.TestConfig",
    'staging': "configStagingConfig",
    'production': "configProductionConfig",
}

__all__ = ['config']
