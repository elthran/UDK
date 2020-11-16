from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError as SqlalchemyOperationalError
from flask import Flask
from flask_cors import CORS
from logging import basicConfig, DEBUG
from time import sleep


from . import environment
from .database_extension import db
from .commands import db_cli
from app.config.hooks import add_auto_commit

from app.models.users import User
from app.models.worlds import World
from app.models.counties import County
from app.models.kingdoms import Kingdom
from app.helpers.constants import Races, Titles, Backgrounds


def initialize(name):
    app = Flask(name)

    basicConfig(level=DEBUG)

    load_configs(app)
    wait_for_db(app)
    load_extensions(app)
    load_commands(app)
    load_hooks(app)

    reset_database(app)

    return app


def load_configs(app):
    env = app.config["ENV"].title()
    print("ENV:", env)
    config = getattr(environment, f"{env}Config")
    app.config.from_object(config)


def wait_for_db(app):
    """Wait for the database."""
    wait_time_in_seconds = 10
    for i in range(12):  # give up after 2 minutes
        try:
            engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
            database_exists(engine.url)
        except SqlalchemyOperationalError as e:
            sleep(wait_time_in_seconds)
            app.logger.info(f"<custom> Database connection not complete. "
                            f"Retrying after {wait_time_in_seconds} seconds...")
        else:
            app.logger.info("<custom> Database connection successful.")
            break


def load_commands(app):
    app.cli.add_command(db_cli)


def load_extensions(app):
    # For development, allow separate front/back-ends.
    CORS(app, resources={r'/*': {'origins': '*'}})

    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    if not database_exists(engine.url):
        create_database(engine.url)
    db.init_app(app)


def load_hooks(app):
    add_auto_commit(app, db)


def reset_database(app):
    with app.app_context():
        try:
            app.logger.info("<custom> Attempting to drop database.")
            db.drop_all()
            app.logger.info("<custom> Database dropped successfully..")
        except SqlalchemyOperationalError as ex:
            app.logger.info("<custom> Failed to drop database.")

        db.create_all()

        user = User("test_user")
        user.save()

        world = World()
        world.save()

        kingdom = Kingdom(name="Eldarion")
        kingdom.save()

        county = County(kingdom_id=1,
                        name="Test County",
                        leader="Test Leader",
                        user_id=user.id,
                        race=Races.HUMAN,
                        title=Titles.SIR,
                        background=Backgrounds.PRIEST)
        county.save()

        db.session.commit()
