from flask import jsonify, request
from flask_login import login_user, logout_user

from app.models.users import User
from app.serializers.users_serializer import UsersSerializer


def login():
    """
    This logs in as user as Flask-login current_user for the cookie session.
    Args:
        username (string): Unique identifier chosen by the user

    Returns:
        A serialized version of the user or an error message.
    """

    username = request.json["username"]
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify(error="User does not exist. Failed to login."), 401

    if login_user(user):
        print("user", user)
        # FIXME: return current_user.api_token.token
        return jsonify(user=UsersSerializer.call(user))

    return jsonify(error="User exists but failed to login.")


def logout():
    """
    Logs the current_user out and cleans up the 'remember me' cookie.
    Returns:
        A redirect or an error message.
    """
    if logout_user():
        return jsonify(message="Logout successful."), 200

    return jsonify(error="User failed to logout."), 422
