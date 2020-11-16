from flask import render_template
from flask_login import current_user


from app.main import app
from app.models.counties import County
from app.models.users import User


@app.route('/county/economy', methods=['GET', 'POST'])
def county_economy():
    # user = current_user
    user = User.query.get(1)
    county = County.query.get(1)
    return render_template('county/economy.html', user=user, county=county)
