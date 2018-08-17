# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/21/16"""
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from project.user.finders.user_finder import UserFinder


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    def validate_username(form, field):
        username = field.data

        user = UserFinder.by_username(username)
        if not user:
            raise ValidationError("Username \"{}\" already exists. ".format(username))
        return username
