# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 2/19/16"""
import os
import unittest
from coverage import Coverage
from flask.ext.script import Manager
from project import app


manager = Manager(app)


@manager.command
def test():
    """runs tests without coverage"""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def coverage():
    """runs tests withcoverage"""
    cov = Coverage(branch=True, include='project/*')
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()


if __name__ == '__main__':
    manager.run()


__author__ = "andresilva"
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__email__ = "andre@unbabel.com"
