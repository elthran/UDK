from flask import redirect, url_for


from app.main import app


@app.route('/', methods=['GET', 'POST'])
def home():
    print("hello?")
    return redirect(url_for('county_home'))
