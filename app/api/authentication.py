from flask import jsonify
from flask_login import login_user

from app.models.users import User
from app.models.counties import County


def create_user(username):
    new_user = User(username=username)
    new_user.save()
    new_county = County(kingdom_id=1,
                        name="Test County",
                        leader="Test Leader",
                        user_id=new_user.id,
                        race="Human",
                        title="Lady",
                        background="Warlord")
    new_county.save()
    return new_user


def login(username):
    user = User.query.filter_by(username=username).first()
    if user:
        if login_user(user):
            # FIXME: return current_user.api_token.token
            return jsonify(
                user=dict(id=user.id,
                          username=user.username,
                          countyId=user.county.id)
            )
        return jsonify(error="Failed to log in user")

    else:
        user = create_user(username)
        login_user(user)
        return jsonify(
            user=dict(id=user.id,
                      username=user.username,
                      countyId=user.county.id)
        )




    return jsonify(error=f"Could not find user for {username}")

