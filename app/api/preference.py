from flask import jsonify

from app.models.counties import County


def get_preference(county_id):
    county = County.query.get(county_id)
    preference = county.preference
    return jsonify(
        preference=dict(
            taxRate=preference._tax_rate,
            rations=preference.rations,
            productionChoice=preference.production_choice,
        )
    )
