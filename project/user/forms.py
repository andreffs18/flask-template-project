# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/21/16"""

from flask_wtf import Form

import wtforms as wtf
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(Form):
    username = wtf.StringField('Username', validators=[DataRequired()])
    password = wtf.PasswordField('Password', validators=[DataRequired()])


class RegisterForm(Form):
    email = wtf.StringField('email', validators=[
        DataRequired(), Length(min=3, max=25), Email()])

    password = wtf.PasswordField('password', validators=[
        DataRequired(), Length(min=6, max=128)])

    confirm_password = wtf.PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password')])