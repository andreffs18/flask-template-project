# !/usr/bin/python
# -*- coding: utf-8 -*-
# Example Admin ModelView: https://github.com/mrjoes/flask-admin/blob/master/examples/sqla/app.py
from project.admin.views import ModelView
from project.user.services.reset_user_password_service import ResetUserPasswordService
from project.user.services.generate_user_api_key_service import GenerateUserApiKeyService


class UserView(ModelView):

    form_excluded_columns = ['api_key']

    column_exclude_list = ['password']

    column_display_all_relations = True

    column_searchable_list = ('username', 'email', 'roles.label')

    def on_model_change(self, form, model, is_created):
        """
        Before committing to database, generate password and api key for this new user
        """
        ResetUserPasswordService(model, form.password.data).call()
        GenerateUserApiKeyService(model).call()
