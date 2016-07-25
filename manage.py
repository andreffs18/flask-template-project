# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 2/19/16"""
from flask.ext.script import Manager
from flask import render_template
from project import create_app

# in case we run the test command choose the "TestConfig"
import sys
arg_dict = dict((i, v) for i, v in enumerate(sys.argv))
config = "config.TestConfig" if arg_dict.get(1, None) == "test" else None
app = create_app(config)
manager = Manager(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    import project.commands as cmd
    manager.add_command("worker", cmd.WorkerCommand())
    manager.add_command("test", cmd.TestCommand())
    manager.add_command("routes", cmd.ListRoutesCommand())
    manager.run()


__author__ = "andresilva"
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__email__ = "andreffs18@gmail.com"
