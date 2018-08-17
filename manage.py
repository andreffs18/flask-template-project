# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask_script import Manager
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
    manager.add_command("create-user", cmd.CreateUserCommand())
    manager.add_command("delete-user", cmd.DeleteUserCommand())
    manager.run()


__version__ = '1.0.0'
__author__ = "Andre Silva"
__email__ = "andreffs18@gmail.com"
