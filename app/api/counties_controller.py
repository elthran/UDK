from flask import jsonify

from app.models.counties import County
from app.serializers.unit_serializer import UnitSerializer
from app.serializers.building_serializer import BuildingSerializer


def get_county(id_):
    county = County.query.get(id_)

    basic_county_view = dict(
        title=county.title,
        leader=county.leader,
        race=county.race,
    )

    full_county_view = dict(
        **basic_county_view,
        name=county.name,
        day=county.day,
        background=county.background,
        population=county.economy.population,
        defensivePower=county.military.defensive_power(),
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
        offensivePower=county.military.offensive_power(),
        units=UnitSerializer.call(county.military.units),
        buildings=BuildingSerializer.call(county.infrastructure.buildings),
        employedWorkers=county.infrastructure.get_employed_workers(),
        grainStores=county.economy.grain_stores,
        taxRate=county.preference._tax_rate,
        rations=county.preference.rations,
        productionChoice=county.preference.production_choice,
    )

    return jsonify(county=full_county_view)
