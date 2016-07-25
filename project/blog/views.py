# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""

from flask import render_template, Blueprint, abort
from project.blog.models import Post

blog_blueprint = Blueprint('blog', __name__)

@blog_blueprint.route('/')
def blog_home():
    posts = Post.objects.all()
    return render_template("home.html", posts=posts)


@blog_blueprint.route('/post/<post_id>')
@blog_blueprint.route('/post/<slug>')
def blog_post(post_id=None, slug=None):
    try:
        post = Post.objects.get(id=post_id)
    except:
        try:
            post = Post.objects.get(slug=slug)
        except:
            abort(404)
    return render_template("home.html", posts=post)
