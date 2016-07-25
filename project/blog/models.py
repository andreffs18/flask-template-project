# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/20/16"""

import datetime
import mongoengine as me
from slugify import slugify
from flask import url_for

class Comment(me.EmbeddedDocument):
    created_at = me.DateTimeField(default=datetime.datetime.now, required=True)
    body = me.StringField(verbose_name="Comment", required=True)
    author = me.StringField(verbose_name="Name", max_length=255, required=True)


class Post(me.Document):
    created_at = me.DateTimeField(default=datetime.datetime.now, required=True)
    title = me.StringField(max_length=255, required=True)
    slug = me.StringField(max_length=255, required=True)
    body = me.StringField(required=True)
    comments = me.ListField(me.EmbeddedDocumentField('Comment'))

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

    def get_absolute_url(self):
        return url_for('blog.blog_post', slug=self.slug)

    def __str__(self):
        return "{}".format(self.title)

    def __repr__(self):
        return u"<Post: {}>".format(str(self))

    def __unicode__(self):
        return unicode(self.id)

    @classmethod
    def create(cls, title, body, slug=None):
        """Create Blog Post object"""
        slug = slugify(title, to_lower=True)
        post = Post(title=title, body=body, slug=slug)
        post.save()
        return post


