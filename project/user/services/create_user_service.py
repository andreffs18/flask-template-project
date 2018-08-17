from project.user.models import User
from project.user.services.reset_user_password_service import ResetUserPasswordService
from project.user.services.generate_user_api_key_service import GenerateUserApiKeyService


class CreateUserService:

    def __init__(self, username, password, generate_api_key=True, *args, **kwargs):
        self.username = username
        self.password = password
        self.generate_api_key = generate_api_key
        self.args = args
        self.kwargs = kwargs

    def call(self):
        self.kwargs.update(dict(username=self.username, password=bytes(self.password, encoding='utf8')))
        user = User(**self.kwargs)
        user.save()
        ResetUserPasswordService(user, self.password).call()
        if self.generate_api_key:
            GenerateUserApiKeyService(user).call()

        return user
