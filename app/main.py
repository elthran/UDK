from flask import jsonify, redirect
from flask_login import login_user, current_user

from .config.initialize import initialize
from .models.users import User
from .models.worlds import World
from .models.counties import County

app = initialize(__name__)


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


@app.route('/user/create/<string:username>', methods=['GET', 'POST'])
def user_creation(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        new_user = User(username=username)
        new_user.save()
        login_user(new_user)
        new_county = County(kingdom_id=1,
                            name="Test County",
                            leader="Test Leader",
                            user_id=new_user.id,
                            race="Human",
                            title="Lady",
                            background="Warlord")
        new_county.save()
        return jsonify(f"User {new_user.id} id created.")
    return jsonify(f"User already exists with that username and id {user.id}")


@app.route('/user/login/<string:username>', methods=['GET', 'POST'])
def user_login(username):
    user = User.query.filter_by(username=username).first()
    if user:
        login_user(user)
    return jsonify(f"Logged in as {current_user}")


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


def import_routes():
    import app.api.routes
    import app.routes.home
    import app.routes.county.home
    import app.routes.county.economy
    import app.routes.county.infrastructure


import_routes()
