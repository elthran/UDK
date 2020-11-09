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
        name=county.name,
        background=county.background,
        population=county.economy.population,
        happiness=75,
        happinessChange=2,
        healthiness=county.economy.healthiness,
        land=county.economy.land,
        gold=county.economy.gold,
        wood=county.economy.wood,
        iron=county.economy.iron,
        stone=county.economy.stone,
        mana=county.economy.mana,
        maxMana=10,
        manaChange=1,
        buildings=[
            dict(
                id=building.id,
                className=building.class_name,
                goldCost=building.gold_cost,
                woodCost=building.wood_cost,
                stoneCost=building.stone_cost,
                description=building.description,
            ) for building in county.infrastructure.buildings],
        employedWorkers=county.infrastructure.get_employed_workers(),
        grainStores=county.economy.grain_stores,
        taxRate=county.preference._tax_rate,
        rations=county.preference.rations,
        productionChoice=county.preference.production_choice,
    )
    if county.user_id == 1:
        # Replace with current_user.id == county.user_id
        return jsonify(
            county=full_county_view
        )

    return jsonify(
        county=basic_county_view
    )
