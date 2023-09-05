from flask import jsonify, request
from flask.views import MethodView
from errors import HttpError
from validate import validate, hash_password, CreateOwner, UpdateOwner

# Create_Ads, Update_Ads
from models import Session, OwnerModel
from sqlalchemy.exc import IntegrityError


def get_owner(session, owner_id):
    user = session.get(OwnerModel, owner_id)
    if user is None:
        raise HttpError(404, "User not found")
    return user


class OwnerView(MethodView):
    def get(self, owner_id: int):
        with Session() as session:
            owner = get_owner(session, owner_id)
            return jsonify(
                {
                    "id": owner.id,
                    "email": owner.email,
                    "create_time": owner.creation_time,
                }
            )

    def post(self):
        owner_data = validate(request.json, CreateOwner)
        owner_data["password"] = hash_password(owner_data["password"])
        with Session() as session:
            owner = OwnerModel(**owner_data)
            session.add(owner)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(409, "There is already such a user")
            return jsonify(
                {
                    "id": owner.id,
                    "email": owner.email,
                    "create_time": owner.creation_time,
                }
            )

    def patch(self, owner_id: int):
        owner_data = validate(request.json, UpdateOwner)
        owner_data["password"] = hash_password(owner_data["password"])
        with Session() as session:
            new_owner = get_owner(session, owner_id)
            for field, value in owner_data.items():
                setattr(new_owner, field, value)
            session.add(new_owner)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(409, "Такой пользователь уже существует")
            return jsonify(
                {
                    "id": new_owner.id,
                    "email": new_owner.email,
                    "create_time": new_owner.creation_time,
                }
            )

    def delete(self, owner_id: int):
        with Session() as session:
            owner = get_owner(session, owner_id)
            session.delete(owner)
            session.commit()
            return jsonify({"status": "Successfully!"})


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
