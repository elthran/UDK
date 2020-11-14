from flask import jsonify, redirect
from flask_login import login_user, current_user

from app.main import app

# deprecated imports for deprecated routes
from app.models.users import User
from app.models.worlds import World
from app.models.counties import County

# actual routes
from app.api.authentication import login
from app.api.counties import get_county
from app.api.users import get_user
from app.api.system import get_current_user



app.add_url_rule('/api/counties/<int:id_>', 'get_county', get_county, methods=['GET'])
# TODO: make this a real login page that accepts a posted form data thing.
# api.add_url_rule('/api/session/login', 'login', login, methods=['POST'])
app.add_url_rule('/api/session/login/<string:username>', 'login', login, methods=['GET'])
app.add_url_rule('/api/system/current_user', 'get_current_user', get_current_user, methods=['GET'])
app.add_url_rule('/api/users/<int:id_>', 'get_user', get_user, methods=['GET'])


# Debug routes (to be deprecate)
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/debug/advance_day', methods=['GET'])
def advance_day():
    world = World.query.get(1)
    world.advance_day()
    return redirect('http://localhost:8080/county/home')


@app.route('/debug/buy_footman', methods=['GET'])
def buy_footman():
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
    county = County.query.get(1)
    # unit = county.military.archer
    unit = [unit for unit in county.military.units if unit.unit_type == 'Archer'][0]
    unit.total_owned += 1
    county.economy.gold -= unit.gold_cost
    county.economy.wood -= unit.wood_cost
    county.economy.iron -= unit.iron_cost
    return redirect('http://localhost:8080/county/home')


@app.route('/user/verify_login', methods=['GET', 'POST'])
def verify_login():
    return jsonify(f"Logged in as {current_user}. Authenticated: {current_user.is_authenticated}")


@app.route('/get_all', methods=['GET', 'POST'])
def get_all():
    counties = County.query.all()
    return jsonify(
        counties=[dict(id=county.id,
                       name=county.name,) for county in counties]
    )

