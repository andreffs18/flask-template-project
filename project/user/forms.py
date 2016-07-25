# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/21/16"""
from flask_wtf import Form
import mongoengine as me
import wtforms as wtf
import wtforms.validators as v

import project.user.models as umodels


class LoginForm(Form):
    username = wtf.StringField('Username', validators=[v.DataRequired()])
    password = wtf.PasswordField('Password', validators=[v.DataRequired()])


class RegisterForm(Form):
    username = wtf.StringField('Username', validators=[
        v.DataRequired(), v.Length(min=3)])
    email = wtf.StringField('Email', validators=[
        v.DataRequired(), v.Length(min=3), v.Email()])
    password = wtf.PasswordField('Password', validators=[
        v.DataRequired(), v.Length(min=6, max=128)])
    confirm_password = wtf.PasswordField('Confirm Password', validators=[
        v.DataRequired(), v.EqualTo('password')])

    def validate_username(form, field):
        username = field.data
        try:
            umodels.User.objects.get(username=username)
            raise v.ValidationError("Username \"{}\" already exists. "
                                    "".format(username))
        except me.DoesNotExist:
            pass
        return username

    def validate_email(form, field):
        email = field.data
        try:
            umodels.User.objects.get(email=email)
            raise v.ValidationError("Email \"{}\" already exists. "
                                    "Did you forget your password?"
                                    "".format(email))
        except me.DoesNotExist:
            pass
        return email
