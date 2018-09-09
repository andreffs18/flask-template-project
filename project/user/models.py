# !/usr/bin/python
# -*- coding: utf-8 -*-
from project.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from flask_login import UserMixin


class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    email = Column(String(128), unique=True)
    password = Column(String(128))
    api_key = Column(String(128))
    is_admin = Column(Boolean)

    def __repr__(self):
        return '<User %r>' % self.username
