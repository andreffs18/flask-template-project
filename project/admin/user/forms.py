# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 7/25/16"""
from flask_wtf import Form
import wtforms as wtf
import wtforms.validators as v
import mongoengine as me
import project.user.models as umodels

class CreateForm(Form):
    username = wtf.StringField('Username', validators=[
        v.DataRequired(), v.Length(min=3)])
    password = wtf.PasswordField('Password', validators=[
        v.DataRequired(), v.Length(min=6, max=128)])
    email = wtf.StringField('Email', validators=[
        v.DataRequired(), v.Length(min=3)])
    is_admin = wtf.BooleanField("Is Admin")

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
