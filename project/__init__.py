# !/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension
from flask_basicauth import BasicAuth
from flask_graphql import GraphQLView
from flask_login import LoginManager
from flask_dotenv import DotEnv
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_admin import Admin
from flask_rq import RQ

from project.database import db
from config import config as project_config


def read_env(app, config_class):
    """
    config environment variables and override with .env declared ones. use configuration given by environment
    variable APP_ENV if "config_class" is not given
    """
    env = DotEnv()
    env.init_app(app, env_file=".env")

    # get correct APP_ENV and right variable
    if not config_class:
        config_class = project_config.get(app.config.get('APP_ENV'))
    app.config.from_object(config_class)
    return app


def setup_logger(app):
    """
    config logger depending on APP_ENV
    """
    log_level = logging.DEBUG if app.config.get("TESTING") else logging.INFO
    log_format = "[%(asctime)s] {%(filename)s#%(funcName)s:%(lineno)d} %(levelname)s - %(message)s"
    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    handler.setFormatter(logging.Formatter(log_format))
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)
    # remove default Flask debug handler
    del app.logger.handlers[0]
    return app


def create_app(config=None):
    app = Flask(__name__)
    # read .envs and configuration class
    app = read_env(app, config)

    # define logging patterns
    app = setup_logger(app)

    # register view blueprints
    from project.home.views import app_blueprint
    from project.user.views import user_blueprint
    app.register_blueprint(app_blueprint)
    app.register_blueprint(user_blueprint)

    # setup apps
    DebugToolbarExtension(app)
    Bcrypt(app)
    RQ(app)
    basic_auth = BasicAuth(app)
    db.init_app(app)

    # register graphql view
    from project.graphql.schema import schema
    app.add_url_rule(
        "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
    )

    # register admin view
    from project.user.models.user import User
    from project.user.models.role import Role
    from project.user.models.user_roles import UserRoles

    from project.admin.views import ModelView, SuperSecretPage
    from project.user.admin.views import UserView
    admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
    admin.add_view(UserView(User, db.session, basic_auth, endpoint="users"))
    admin.add_view(ModelView(Role, db.session, basic_auth, endpoint="roles"))
    admin.add_view(SuperSecretPage(name="Secret"))

    # register api endpoints
    from project.api.v1.user import User
    api = Api(app, prefix='/api/v1/')
    api.add_resource(User, 'users/', endpoint='api.v1.users')

    # import custom login manager functions
    from project.user.login_manager import load_user_from_request, load_user
    login_manager = LoginManager(app)
    login_manager.login_view = "user.login"
    login_manager.user_loader(load_user)
    login_manager.request_loader(load_user_from_request)
    # default flashed messages category
    login_manager.login_message_category = 'info'
    login_manager.needs_refresh_message_category = 'info'

    # jinja extensions
    app.jinja_env.add_extension('jinja2.ext.do')

    return app
