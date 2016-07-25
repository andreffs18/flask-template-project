# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from project.tests.base import MVCTestCase
from slugify import slugify
class BlogModelTestCase(MVCTestCase):

    def setUp(self):
        super(BlogModelTestCase, self).setUp()
        self.post = self.create_blog_post()

    def test_post_representation(self):
        """Ensure post object __repr__, __str__ and __unicode__ are
        returning correct values"""
        self.assertEqual(str(self.post), self.post.title)
        self.assertEqual(repr(self.post), u"<Post: {}>".format(str(self.post)))
        self.assertEqual(unicode(self.post), unicode(self.post.id))

    def test_get_absolute_url(self):
        """Ensure getting the absolute url from a blog post corresponds to
        the correct values"""
        self.assertEqual(slugify(self.post.title, to_lower=True),
                         self.post.slug)
        self.assertEqual(self.post.get_absolute_url(),
                         "/post/{}".format(self.post.slug))