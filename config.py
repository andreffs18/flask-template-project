# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGODB_DB = os.environ.get("MONGODB_DB", "default")
    MONGODB_DB_TEST = os.environ.get("MONGODB_DB_TEST", "default_test")

    # app.config['RQ_DEFAULT_HOST'] = 'somewhere.com'
    # app.config['RQ_DEFAULT_PORT'] = 6479
    # app.config['RQ_DEFAULT_PASSWORD'] = 'password'
    # app.config['RQ_DEFAULT_DB'] = 1

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_PROFILER_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # TODO: run tests in local memory.
    MONGODB_DB = BaseConfig.MONGODB_DB_TEST


class LocalhostConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # TODO not working because current version of DebugToolbar doesn't allow this.
    DEBUG_TB_PANELS = (
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        'flask_mongoengine.panels.MongoDebugPanel',
    )


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


config = {
    '_baseconfig': BaseConfig,
    'localhost': LocalhostConfig,
    'test': TestConfig,
    'production': ProductionConfig,
}

__all__ = ['config']
