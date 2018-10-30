# !/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Unicode
from project.database import Base


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False, server_default=u'', unique=True)
    label = Column(Unicode(255), server_default=u'')

    def __str__(self):
        return u'"{}"'.format(self.label)
