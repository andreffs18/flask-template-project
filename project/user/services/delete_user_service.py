from project.database import db


class DeleteUserService:

    def __init__(self, user):
        self.user = user

    def call(self):
        db.session.delete(self.user)
        db.session.commit()
        return None
