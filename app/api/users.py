from flask import jsonify

from app.models.users import User
from app.serializers.users_serializer import UsersSerializer


def get_user(id_):
    user = User.query.get(id_)
    return jsonify(
        user=UsersSerializer.call(user)
    )
