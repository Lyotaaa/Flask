from flask import jsonify, request
from flask import MethodView
from errors import HttpError
from validate import validate, hash_password, CreateOwner

class AdsView(MethodView):

    def get(self, user_id: int):
        if ...:
            raise HttpError(404, "user not fount")
        pass

    def post(self):
        owner_data = validate(request.json, CreateOwner)
        owner_data["password"] = hash_password(owner_data["password"])
        pass

    def patch(self, user_id: int):
        pass

    def delete(self, user_id: int):
        pass

