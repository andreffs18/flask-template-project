from flask import make_response, jsonify


class ValueComposite(object):
    message = None

    def initialize(self, initial_message):
        self.message = initial_message

    def serialize_with(self, **entry):
        self.message.update(entry)

    def to_dict(self):
        return dict(self.message)

    def json(self, code=200):
        return make_response(jsonify(self.message), code)
