from project.user.finders.user_finder import UserFinder
from project.user.values.user_value import UserValue


class UserApiHandler:

    @classmethod
    def get_list_of_users(cls):
        """
        Return list of users
        """
        users = UserFinder.all()
        users = list(map(lambda user: UserValue(user).to_dict(), users))
        return users
