# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
app = Flask(__name__)

import os
config = os.environ.get('APP_ENV', 'config.LocalhostConfig')
app.config.from_object(config)

db = MongoEngine(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from project.user.views import user_blueprint
app.register_blueprint(user_blueprint)

from project.home.views import app_blueprint
app.register_blueprint(app_blueprint)


from project.user.models import User
login_manager.login_view = "user.login"
@login_manager.user_loader
def load_user(user_id):
    print user_id
    if user_id != u'None':
        user = User.objects.filter(id=user_id).first()
        print user
        return user
    return False

__author__ = "andresilva"
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__email__ = "andre@unbabel.com"
