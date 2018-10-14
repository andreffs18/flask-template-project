# !/usr/bin/python
# -*- coding: utf-8 -*-
import base64
import binascii

from flask import current_app as app
from flask_bcrypt import check_password_hash
from project.user.finders.user_finder import UserFinder


def load_user(user_id):
    if user_id in ['None', None]:
        return False

    user = UserFinder.by_id(user_id)
    if not user:
        app.logger.error("User id \"{}\" does not exist".format(user_id))
        return False

    return user


def load_user_from_request(request):
    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = UserFinder.by_api_key(api_key)
        if user:
            return user

    # next, try to login using Basic Auth first, try apikey and then user:pass
    auth = request.headers.get('Authorization')
    if not auth:
        return None

    # get bytes string instead of str representation
    auth = auth.replace('Basic ', '', 1)
    try:
        auth = bytes(auth, 'utf8')
        auth = base64.b64decode(auth)
        auth = auth.decode()
    except (UnicodeDecodeError, TypeError, binascii.Error):
        # make byte string "Str" again
        auth = auth.decode()

    # try if auth is api_key
    user = UserFinder.by_api_key(auth)
    if user:
        return user

    # if not, try with username and password
    if ":" in auth:
        username, password = auth.split(":")
        user = UserFinder.by_username(username)
        if user and check_password_hash(user.password, password):
            return user

    return None
