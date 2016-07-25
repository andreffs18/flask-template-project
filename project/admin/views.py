# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
from flask import redirect, current_app as app, render_template, request, url_for, Blueprint
from flask.ext.login import login_user, login_required, logout_user, wraps, current_user
from project.home.decorators import admin_required

import project.user.models as umodels
import project.blog.models as bmodels

from flask import Blueprint
from flask.ext.mongoengine import Pagination

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.route('/admin/users/')
def home_users():
    return redirect("/admin/#users")


@admin_blueprint.route('/admin/posts/')
def home_posts():
    return redirect("/admin/#posts")


@admin_blueprint.route('/admin/')
@login_required
@admin_required
def home():
    params = request.args.to_dict()

    # user pagination
    upage = int(params.get('user-page', 1))
    users = Pagination(umodels.User.objects.all(), upage, 20)

    # post pagination
    ppage = int(params.get('post-page', 1))
    posts = Pagination(bmodels.Post.objects.all(), ppage, 20)

    return render_template('admin/home.html', **{
        'users': users, 'posts': posts
    })


# Load remaining endpoints
from .user.views import *  # load user admin routes  # noqa
from .blog.views import *  # load blog admin routes  # noqa
