# !/usr/bin/python
# -*- coding: utf-8 -*-
import logging

from flask import render_template, Blueprint

from project import get_customer_reporting_db

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
    log.info("Customer list requested for service %s" % service)

    db = get_customer_reporting_db()
    customers = db.customers.find()

    return render_template('admin/customer_list.html', customers=customers)


@admin_blueprint.route('/<service>/<customer>')
def customer_detail(service, customer):
    log.info("Customer detail requested for (%s, %s) pair" % (service, customer))
