# !/usr/bin/python
# -*- coding: utf-8 -*-
from project.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from project.user.models.rbac_user_mixin import UserMixin as RBACUserMixin


class User(RBACUserMixin, UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    email = Column(String(128), unique=True)
    password = Column(String(128))
    api_key = Column(String(128))

    roles = relationship('Role', secondary='user_roles')

    def __repr__(self):
        return '<User %r>' % self.username
