# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
import bcrypt
import mongoengine as me

from flask import current_app as app
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.local import LocalProxy

import project.permission.models as pmodels
import project.language.models as lmodels
