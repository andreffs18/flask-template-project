# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
from flask import render_template, Blueprint
from project.blog.models import Post

app_blueprint = Blueprint('app', __name__)

@app_blueprint.route('/')
def home():
    posts = Post.objects.all()
    return render_template("home.html", posts=posts)
