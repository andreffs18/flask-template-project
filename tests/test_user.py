# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from base import BaseTestCase

class UsersViewsTests(BaseTestCase):
    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login', follow_redirects=True)
        self.assertIn(b'Please login', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        self.client.post(
            '/login/',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'You were logged out.', response.data)
