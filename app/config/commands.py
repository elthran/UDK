import click
from sqlalchemy.exc import DatabaseError
from flask import current_app
from flask.cli import with_appcontext


"""command group access follows the pattern `flask db drop`"""
@click.group('db')
def db_cli():
    """Some simple database commands."""


@db_cli.command('drop')
@with_appcontext
def drop_db():
    """Remove the database."""
    from sqlalchemy import create_engine
    from sqlalchemy_utils import drop_database

    engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    drop_database(engine.url)


def add_auto_commit(app, db):
    @app.after_request
    def session_commit(response):
        if response.status_code >= 400:
            # I'm not sure if this is correct?
            # Maybe should redirect to 404?
            return response
        try:
            db.session.commit()
        except DatabaseError:
            db.session.rollback()
            raise
        # db.session.remove() # is called for you by flask-sqlalchemy
        return response

