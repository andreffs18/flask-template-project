from werkzeug.exceptions import HTTPException
from flask import Response, redirect
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView as DefaultModelView
from flask_login import login_required
from project.home.decorators import roles_required


class BasicAuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class ModelView(DefaultModelView):

    column_auto_select_related = True

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


class SuperSecretPage(BaseView):

    @expose(url="/", methods=("GET", ))
    @login_required
    @roles_required('admin')
    def secret(self):
        return self.render('admin/super-secret-page.html')
