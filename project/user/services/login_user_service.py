from flask_login import login_user


class LoginUserService:

    def __init__(self, user):
        self.user = user

    def call(self):
        return login_user(self.user)
