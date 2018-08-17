# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
from mongoengine.document import Document
from mongoengine.fields import StringField, BinaryField, BooleanField
from mongoengine.queryset import queryset_manager

from flask_login import UserMixin


class User(UserMixin, Document):
    """"""
    username = StringField(required=True, unique=True)
    password = BinaryField(required=True)
    api_key = StringField(required=False)
    is_admin = BooleanField(default=False)

    _is_deleted = BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.username)

    def __repr__(self):
        return "<User: {}>".format(str(self))

    meta = {
        # 'allow_inheritance': True,
        'indexes': [
            ('username',),
        ],
    }

    @queryset_manager
    def _objects(doc_cls, queryset):
        """Original queryset manager for this object that return every
        collection available in the database"""
        return queryset

    @queryset_manager
    def objects(doc_cls, queryset):
        """Hides all "deleted" users from every query"""
        return queryset.filter(_is_deleted=False)
