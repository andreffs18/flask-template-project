# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""

from project import db, bcrypt
from flask.ext.login import UserMixin


class User(UserMixin, db.Document):
    username = db.StringField(max_length=255, required=True)
    password = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255, required=True)

    def __unicode__(self):
        return self.email

    meta = {
        'allow_inheritance': True,
        'indexes': ['username', ],
    }

    def save(self, *args, **kwargs):
        """"""
        if not self.username:
            self.username = self.email.split("@")[0]
            self.password = bcrypt.generate_password_hash(
                self.password)
        return super(User, self).save(*args, **kwargs)