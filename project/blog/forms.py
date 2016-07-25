# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/21/16"""
from flask_wtf import Form
from slugify import slugify

import wtforms as wtf
import wtforms.validators as v

class CreateNewPost(Form):
    title = wtf.StringField('Username', validators=[
        v.DataRequired(), v.Length(min=3, max=255)])
    slug = wtf.StringField('slug')
    body = wtf.StringField('Body', validators=[
        v.DataRequired(), v.Length(min=3, max=255)])

    def validate(self):
        rv = super(CreateNewPost, self).validate()
        if not rv:
            return False

        self.slug.data = slugify(self.title.data, to_lower=True)
        return True