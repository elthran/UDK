from app.main import app
from app.models.counties import County


@app.route('/debug/advance_day', methods=['GET'])
def advance_day():
    print("Advance day API hit")
    county = County.query.get(1)
    county.economy.gold += 200
    return "happy"


@app.route('/debug/buy_footman', methods=['GET'])
def buy_footman():
    print("Buy soldier API hit")
    county = County.query.get(1)
    unit = county.military.soldier
    unit.total_owned += 1
    county.economy.gold -= unit.gold_cost
    county.economy.wood -= unit.wood_cost
    county.economy.iron -= unit.iron_cost
    return "happy"


@app.route('/debug/buy_archer', methods=['GET'])
def buy_archer():
    print("Buy archer API hit")
    county = County.query.get(1)
    unit = county.military.archer
    unit.total_owned += 1
    county.economy.gold -= unit.gold_cost
    county.economy.wood -= unit.wood_cost
    county.economy.iron -= unit.iron_cost
    return "happy"

