from flask_login import logout_user


class LogoutUserService:

    def __init__(self):
        pass

    def call(self):
        logout_user()
        return None
