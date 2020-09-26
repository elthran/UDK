from flask import render_template


from app.main import app
from app.models.counties import County
from app.models.users import User


@app.route('/county/home', methods=['GET', 'POST'])
def county_home():
    # user = current_user
    user = User.query.get(1)
    county = County.query.get(1)
    return render_template('county/home.html', user=user, county=county)
