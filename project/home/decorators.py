# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 7/8/16"""
from flask.ext.login import wraps, current_user, current_app as app


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            return app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view
