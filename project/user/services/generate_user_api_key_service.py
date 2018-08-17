import random
import string


class GenerateUserApiKeyService:

    def __init__(self, user, size=64):
        self.user = user
        self.size = size

    def call(self):
        """
        For given size, generate random string with all ascii and digits
        """
        return u''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(self.size))
