from flask import Response, redirect
from flask_admin.contrib.sqla import ModelView as DefaultModelView
from werkzeug.exceptions import HTTPException


class BasicAuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class ModelView(DefaultModelView):

    def __init__(self, model, session, basic_auth, *args, **kwargs):
        super(ModelView, self).__init__(model, session, *args, **kwargs)
        self.basic_auth = basic_auth

    def is_accessible(self):
        if not self.basic_auth.authenticate():
            raise BasicAuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(self.basic_auth.challenge())
