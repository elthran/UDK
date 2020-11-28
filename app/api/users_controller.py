from flask import jsonify, request

from app.models.counties import County
from app.models.users import User
from app.serializers.users_serializer import UsersSerializer


def create_user():
    """
    data:
        username (string): Unique identifier for new user

    Returns:
        A serialized version of the user or an error message.
    """

    username = request.json["username"]

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify(error="User already exists. Failed to create account.")

    user = User(username=username)
    user.save()
    county = County(
        kingdom_id=1,
        name=f"County-{user.id}",
        leader=f"Leader-{user.id}",
        user_id=user.id,
        race="Human",
        title="Lady",
        background="Warlord",
    )
    county.save()
    return jsonify(user=UsersSerializer.call(user))


def get_user(id_):
    user = User.query.get(id_)
    return jsonify(user=UsersSerializer.call(user))


def get_users():
    users = User.query.all()
    return jsonify(users=[UsersSerializer.call(user) for user in users])
