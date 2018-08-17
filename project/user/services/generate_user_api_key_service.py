import secrets


class GenerateUserApiKeyService:

    def __init__(self, user, size=32):
        self.user = user
        self.size = size

    def call(self):
        """
        For given size, generate random string with all ascii and digits
        """
        self.user.api_key = secrets.token_hex(self.size)
        self.user.save()
        return self.user.api_key
