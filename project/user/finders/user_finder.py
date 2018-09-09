from project.user.models import User


class UserFinder:

    @classmethod
    def all(cls):
        return User.query.filter().all()

    @classmethod
    def by_id(cls, user_id):
        return User.query.filter(User.id == user_id).first()

    @classmethod
    def by_username(cls, username):
        return User.query.filter(User.username == username).first()

    @classmethod
    def by_api_key(cls, api_key):
        return User.query.filter(User.api_key == api_key).first()
