from flask_login import logout_user


class LogoutUserService:

    @staticmethod
    def call():
        logout_user()
        return None
