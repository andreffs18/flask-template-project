from project.user.models import User


class UserFinder:

    @classmethod
    def by_id(cls, id):
        return User.objects.filter(id=id).first()

    @classmethod
    def by_username(cls, username):
        return User.objects.filter(username=username).first()
