# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
from flask import redirect, current_app as app, render_template, request, url_for, Blueprint
from flask_login import login_user, login_required, logout_user, wraps, current_user
from project.home.decorators import admin_required

import project.user.models as umodels

from flask import Blueprint
from flask_mongoengine import Pagination

from project.api import Resources

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.route('/admin/users/')
def home_users():
    return redirect("/admin/#users")


@admin_blueprint.route('/admin/')
@login_required
@admin_required
def home():
    params = request.args.to_dict()

    # user pagination
    upage = int(params.get('user-page', 1))
    users = Pagination(umodels.User.objects.all(), upage, 20)

    return render_template('admin/home.html', **{
        'users': users, 'resources': Resources
    })


# Load remaining endpoints
from .user.views import *  # load user admin routes  # noqa
