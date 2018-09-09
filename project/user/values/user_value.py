from project.utils.value_composite import ValueComposite


class UserValue(ValueComposite):

    def __init__(self, user):
        super(UserValue, self).initialize({})
        self.serialize_with(username=user.username)
        self.serialize_with(id=user.id)
