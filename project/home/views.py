# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template, Blueprint

app_blueprint = Blueprint('app', __name__)


@app_blueprint.route('/')
def home():
    return render_template("home.html")
