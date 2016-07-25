# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""

import project.blog.models as bmodels


class BlogTestUtils(object):

    def setUp(self):
        """"""
        super(BlogTestUtils, self).setUp()

    @staticmethod
    def create_blog_post(title=None, body=None):
        """Aux test method that creates user from given arguments"""
        if title is None:
            title = "BlogPost Title"
        if body is None:
            body = "This is a sample text. This should be the BlogPost body"

        return bmodels.Post.create(title=title, body=body)