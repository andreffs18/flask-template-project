# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 2/19/16"""
import os
import unittest
from coverage import Coverage
from flask.ext.script import Manager
from flask import url_for
from project import app


manager = Manager(app)


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(
            rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line


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
    for p in sorted (os.environ.keys()):
        pass
      #  print p
    manager.run()


__author__ = "andresilva"
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__email__ = "andre@unbabel.com"
