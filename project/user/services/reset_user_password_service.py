from flask_bcrypt import generate_password_hash


class ResetUserPasswordService:

    def __init__(self, user, new_password="password"):
        self.user = user
        self.new_password = new_password

    def call(self):
        self.user.password = generate_password_hash(self.new_password)
        self.user.save()
        return self.user.password
