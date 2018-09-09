import secrets
from project.database import db


class GenerateUserApiKeyService:

    def __init__(self, user, size=32):
        self.user = user
        self.size = size

    def call(self):
        """
        For given size, generate random string with all ascii and digits
        """
        self.user.api_key = secrets.token_hex(self.size)
        db.session.commit()
        return self.user.api_key
