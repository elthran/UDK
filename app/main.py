from flask import jsonify, redirect

from .config.initialize import initialize
from .models.worlds import World
from .models.counties import County

app = initialize(__name__)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/debug/advance_day', methods=['GET'])
def advance_day():
    print("Advance day API hit")
    world = World.query.get(1)
    world.advance_day()
    return redirect('http://localhost:8080/county/home')


@app.route('/debug/buy_footman', methods=['GET'])
def buy_footman():
    print("Buy soldier API hit")
    county = County.query.get(1)
    # unit = county.military.soldier
    unit = [unit for unit in county.military.units if unit.unit_type == 'Soldier'][0]
    unit.total_owned += 1
    county.economy.gold -= unit.gold_cost
    county.economy.wood -= unit.wood_cost
    county.economy.iron -= unit.iron_cost
    return redirect('http://localhost:8080/county/home')


@app.route('/debug/buy_archer', methods=['GET'])
def buy_archer():
    print("Buy archer API hit")
    county = County.query.get(1)
    # unit = county.military.archer
    unit = [unit for unit in county.military.units if unit.unit_type == 'Archer'][0]
    unit.total_owned += 1
    county.economy.gold -= unit.gold_cost
    county.economy.wood -= unit.wood_cost
    county.economy.iron -= unit.iron_cost
    return redirect('http://localhost:8080/county/home')


def import_routes():
    import app.api.routes
    import app.routes.home
    import app.routes.county.home
    import app.routes.county.economy
    import app.routes.county.infrastructure


import_routes()
