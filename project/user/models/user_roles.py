# !/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, ForeignKey
from project.database import Base


class UserRoles(Base):
    __tablename__ = 'user_roles'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id', ondelete='CASCADE'))
    role_id = Column(Integer(), ForeignKey('roles.id', ondelete='CASCADE'))
