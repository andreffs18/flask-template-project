# !/usr/bin/python
# -*- coding: utf-8 -*-
# Codebase extracted from https://github.com/lingthio/Flask-User/blob/master/flask_user/decorators.py
from flask import current_app as app
from flask_login import current_user as user
from functools import wraps


def roles_required(*role_names):
    """
    This decorator ensures that the current user is logged in, and has *all* of the specified roles (AND operation).
    Example::
        @route('/escape')
        @roles_required('Special', 'Agent')
        def escape_capture():  # User must be 'Special' AND 'Agent'
            ...
    Calls unauthenticated_view() when the user is not logged in or when user has not confirmed their email address.
    Calls unauthorized_view() when the user does not have the required roles.
    Calls the decorated view otherwise.
    """
    def wrapper(view_function):

        @wraps(view_function)
        def decorator(*args, **kwargs):
            # User must have the required roles
            if not user.has_roles(*role_names):
                # Redirect to the unauthorized page
                return app.login_manager.unauthorized()

            # It's OK to call the view
            return view_function(*args, **kwargs)
        return decorator
    return wrapper
