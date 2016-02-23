# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""

from flask import flash, redirect, render_template, request, url_for, Blueprint
from forms import LoginForm, RegisterForm
from flask.ext.login import login_user, login_required, logout_user
from models import User
user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/dashboard/', methods=['GET'])
@login_required
def dashboard():
    return render_template('user/dashboard.html')


@user_blueprint.route('/signin/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data).save()
        login_user(user)
        return redirect(url_for('user.dashboard'))

    return render_template('user/register.html', form=form)


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.objects.filter(username=request.form['username']).first()
            if user is not None:
                login_user(user)
                flash('You were logged in.')
                return redirect(url_for('user.dashboard'))
            else:
                error = 'Invalid Credentials. Please try again.'

    return render_template('user/login.html', form=form, error=error)


@user_blueprint.route('/logout/')
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('app.home'))
