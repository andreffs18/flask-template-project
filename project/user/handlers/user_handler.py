from flask_bcrypt import check_password_hash

from project.user.services.create_user_service import CreateUserService
from project.user.services.login_user_service import LoginUserService
from project.user.services.logout_user_service import LogoutUserService

from project.user.finders.user_finder import UserFinder
from project.utils import flash


class UserHandler:

    @classmethod
    def login(cls, form):
        """
        Login user by giving "LoginForm" form and validate if username+password pair is valid
        """
        if not form.validate_on_submit():
            flash.danger(u'Form is not valid.')
            return False

        user = UserFinder.by_username(form.username.data)
        if not user:
            flash.danger(u'User {} does not exists.'.format(form.username.data))
            return False

        if not check_password_hash(user.password, form.password.data):
            flash.warning(u'Invalid Credentials. Please try again.')
            return False

        LoginUserService(user).call()
        return user

    @classmethod
    def logout(cls):
        """
        Delete user session
        """
        return LogoutUserService().call()

    @classmethod
    def register(cls, form):
        """
        Create new user by given "RegisterForm"
        """
        if not form.validate_on_submit():
            flash.danger(u'Form is not valid.')
            return False

        user = CreateUserService(form.username.data, form.password.data).call()
        return LoginUserService(user).call()
