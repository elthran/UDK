from flask import jsonify

from app.models.kingdoms import Kingdom
# from app.serializers.kingdoms_serializer import KingdomsSerializer


def get_kingdoms():
    kingdoms = Kingdom.query.all()

    kingdoms = [dict(
        counties=[
            dict(
                id=county.id,
                name=county.name,
                leader=county.leader,
            ) for county in kingdom.counties],
    ) for kingdom in kingdoms]

    return jsonify(
        kingdoms=kingdoms
    )


def get_kingdom(id_):

    kingdom = Kingdom.query.get(id_)

    kingdom_view = dict(
        counties=[
            dict(
                id=county.id,
                name=county.name,
                leader=county.leader,
            ) for county in kingdom.counties],
    )

    return jsonify(
        kingdom=kingdom_view
    )
