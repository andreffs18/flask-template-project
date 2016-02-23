# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
__author__ = "andresilva"
__email__ = "andre@unbabel.com"

# TODO create .env file that is loaded automatically

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "KeepThisS3cr3t"
    MONGODB_SETTINGS = {'DB': "curationtool"}


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLE = False
    MONGODB_SETTINGS = {'DB': "curationtool-test"}


class LocalhostConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
