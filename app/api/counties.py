from flask import jsonify

from app.models.counties import County


def get_county(id):
    county = County.query.get(id)

    basic_county_view = dict(
        title=county.title,
        leader=county.leader,
        race=county.race,
    )

    full_county_view = dict(
        **basic_county_view,
        background=county.background,
        population=county.economy.population,
        healthiness=county.economy.healthiness,
        gold=county.economy.gold,
        wood=county.economy.wood,
        iron=county.economy.iron,
        stone=county.economy.stone,
        mana=county.economy.mana,
        maxMana=10,
        manaChange=1,
        grainStores=county.economy.grain_stores,
    )
    if county.user_id == 1:
        # Replace with current_user.id == county.user_id
        return jsonify(
            county=full_county_view
        )

    return jsonify(
        county=basic_county_view
    )
