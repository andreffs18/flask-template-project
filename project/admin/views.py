# !/usr/bin/python
# -*- coding: utf-8 -*-
import logging

from flask import render_template, Blueprint


log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.route('/')
def home():
    log.info("home")
    return render_template("admin/home.html")


@admin_blueprint.route('/select_service')
def select_service():
    log.info("Select service page")
    return render_template('admin/select_service.html')


@admin_blueprint.route('/<service>/customer_list')
def customer_list(service):
    log.info("Selected service: %s" % service)
