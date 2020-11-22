from flask import jsonify, redirect, url_for
from flask_login import login_user, logout_user

from app.models.users import User
from app.models.counties import County
from app.serializers.users_serializer import UsersSerializer


def create(username):
    """
    This will create a new user if one does not exist with that username.

    Args:
        username (string): Unique identifier of that user

    Returns:
        A serialized version of the user or an error message.
    """
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify(error="User already exists. Failed to create account.")
    user = User(username=username)
    user.save()
    county = County(kingdom_id=1,
                    name=f"County-{user.id}",
                    leader=f"Leader-{user.id}",
                    user_id=user.id,
                    race="Human",
                    title="Lady",
                    background="Warlord")
    county.save()
    return user


def login(username):
    """
    This logs in as user as Flask-login current_user for the cookie session.
    Args:
        username (string): Unique identifier chosen by the user

    Returns:
        A serialized version of the user or an error message.
    """
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify(error="User does not exist. Failed to login.")
    if login_user(user):
        # FIXME: return current_user.api_token.token
        return jsonify(
            user=UsersSerializer.call(user)
        )
    return jsonify(error="User exists but failed to login.")


def logout():
    """
    Logs the current_user out and cleans up the 'remember me' cookie.
    Returns:
        A redirect or an error message.
    """
    if logout_user():
        return redirect(url_for('home'))
    return jsonify(error="User failed to logout.")
