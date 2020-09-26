from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError as SqlalchemyOperationalError
from flask import Flask
from logging import basicConfig, DEBUG

from . import environment
from app.helpers.constants import Races, Titles, Backgrounds
from .database_extension import db
from .commands import db_cli, add_auto_commit
from app.models.users import User
from app.models.counties import County


def initialize(name):
    app = Flask(name)

    basicConfig(level=DEBUG)

    load_configs(app)
    load_extensions(app)
    load_commands(app)
    load_hooks(app)

    reset_database(app)

    return app


def load_configs(app):
    env = app.config["ENV"].title()
    config = getattr(environment, f"{env}Config")
    app.config.from_object(config)


def load_commands(app):
    app.cli.add_command(db_cli)


def load_extensions(app):
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

        county = County(name="Test County",
                        leader="Test Leader",
                        user_id=user.id,
                        race=Races.HUMAN,
                        title=Titles.SIR,
                        background=Backgrounds.PRIEST)
        county.save()

        db.session.commit()
