from flask import render_template
from flask_login import current_user


from app.main import app
from app.models.counties import County
from app.models.users import User


@app.route('/county/infrastructure', methods=['GET', 'POST'])
def county_infrastructure():
    # user = current_user
    user = User.query.get(1)
    county = County.query.get(1)
    return render_template('county/infrastructure.html', user=user, county=county)
