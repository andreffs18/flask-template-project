class DeleteUserService:

    def __init__(self, user, force=False):
        self.user = user
        self.force = force

    def call(self):
        """
        Only delete user from database if the flag "force" is True
        """
        if self.force:
            return self.user.delete()

        self.user._is_deleted = True
        self.user.save()
        return None
