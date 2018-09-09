# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask import redirect, render_template, request, Blueprint
from flask_login import login_required
from flask_mongoengine import Pagination

from project.home.decorators import admin_required
from project.api import Resources

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.route('/users/')
def home_users():
    return redirect("/#users")


@admin_blueprint.route('/')
@login_required
@admin_required
def home():
    params = request.args.to_dict()

    # user pagination
    from project.user.models import User
    upage = int(params.get('user-page', 1))
    users = Pagination(User.objects.all(), upage, 20)

    return render_template('admin/home.html', **{'users': users, 'resources': Resources})


# Load remaining endpoints
from .user.views import *  # noqa
