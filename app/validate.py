import pydantic
import typing
from errors import HttpError
from hashlib import md5


class CreateOwner(pydantic.BaseModel):
    email: str
    password: str

    @pydantic.validator("password")
    def secure_password(self, value):
        if len(value) < 8:
            raise ValueError("Password is short")
        return value


class Create_Ads(pydantic.BaseModel):
    title: str
    description: str
    owner_id: int

    @pydantic.validator("title")
    def secure_password(self, value):
        if 20 > len(value) > 1:
            raise ValueError("Long title")
        return value

    @pydantic.validator("description")
    def secure_password(self, value):
        if 30 > len(value) > 1:
            raise ValueError("Long description")
        return value


def validate(val_schema, val_data):
    try:
        return val_schema(**val_data).dict()
    except pydantic.ValidationError as er:
        raise HttpError(400, er.errors())


def hash_password(password: str):
    password = password.encode()
    password = md5(password).hexdigest()
    return password
