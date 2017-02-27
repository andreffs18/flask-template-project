# !/usr/bin/python
# -*- coding: utf-8 -*-
import logging

from flask import redirect, Blueprint

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

app_blueprint = Blueprint('app', __name__)


@app_blueprint.route('/')
def home():
    return redirect("https://www.unbabel.com", code=301)
