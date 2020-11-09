from flask import jsonify

from app.models.counties import County


def get_infrastructure(county_id):
    county = County.query.get(county_id)
    infrastructure = county.infrastructure
    return jsonify(
        infrastructure=dict(
            employedWorkers=county.infrastructure.get_employed_workers(),
            buildings=[
                dict(
                    id=building.id,
                    className=building.class_name,
                    goldCost=building.gold_cost,
                    woodCost=building.wood_cost,
                    stoneCost=building.stone_cost,
                    description=building.description,
                ) for building in infrastructure.buildings],
        )
    )
