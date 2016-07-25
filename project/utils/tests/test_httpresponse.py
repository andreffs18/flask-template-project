# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from project.tests.base import UtilsTestCase
from project.utils.httpresponse import NotOkResponse, OkResponse


class HTTPResponseUtilsTestCase(UtilsTestCase):

    def setUp(self):
        super(HTTPResponseUtilsTestCase, self).setUp()

    def test_not_ok_response(self):
        """Ensure NotOkResponse is working properly"""
        res = NotOkResponse({})

    def test_ok_response(self):
        """Ensure OkResponse is working properly"""
        res = OkResponse({})
