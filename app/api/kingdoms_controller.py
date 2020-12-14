from flask import jsonify

from app.models.kingdoms import Kingdom
from app.serializers.kingdom_serializer import KingdomSerializer


def get_kingdoms():
    kingdoms = Kingdom.query.all()

    return jsonify(kingdoms=KingdomSerializer.call(kingdoms))


def get_kingdom(id_):

    kingdom = Kingdom.query.get(id_)

    return jsonify(kingdoms=KingdomSerializer.call(kingdom))
