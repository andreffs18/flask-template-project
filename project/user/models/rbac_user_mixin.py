# !/usr/bin/python
# -*- coding: utf-8 -*-
# Codebase extracted from https://github.com/lingthio/Flask-User/blob/master/flask_user/user_mixin.py
from flask_login import current_user as user


class UserMixin(object):
    """ This class adds required methods to the User data-model.
    Example:
        class User(db.Model, UserMixin):
            ...
    """

    def has_roles(self, *requirements):
        """
        Return True if the user has all of the specified roles. Return False otherwise.
        has_roles() accepts a list of requirements:

            has_role(requirement1, requirement2, requirement3).

        Each requirement is either a role_name, or a tuple_of_role_names.
            role_name example:   'manager'
            tuple_of_role_names: ('funny', 'witty', 'hilarious')

        A role_name-requirement is accepted when the user has this role.
        A tuple_of_role_names-requirement is accepted when the user has ONE of these roles.
        has_roles() returns true if ALL of the requirements have been accepted.
        For example:
            has_roles('a', ('b', 'c'), d)
        Translates to:
            User has role 'a' AND (role 'b' OR role 'c') AND role 'd'"""
        # Translates a list of role objects to a list of role_names
        role_names = [role.name for role in user.roles]

        # has_role() accepts a list of requirements
        for requirement in requirements:
            if isinstance(requirement, (list, tuple)):
                # this is a tuple_of_role_names requirement
                tuple_of_role_names = requirement
                authorized = False
                for role_name in tuple_of_role_names:
                    if role_name in role_names:
                        # tuple_of_role_names requirement was met: break out of loop
                        authorized = True
                        break
                if not authorized:
                    return False  # tuple_of_role_names requirement failed: return False
            else:
                # this is a role_name requirement
                role_name = requirement
                # the user must have this role
                if role_name not in role_names:
                    return False  # role_name requirement failed: return False

        # All requirements have been met: return True
        return True
