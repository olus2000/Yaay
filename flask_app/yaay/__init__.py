import os
import os.path
import re

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# from yaay import names, of, blueprints
# from yaay.model import model, stuff
# from yaay.cli import cli, stuff


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)


    # ensure the instance folder exists
    if not os.path.exists(app.instance_path):
        os.mkdir(app.instance_path)

    # load config and overwrite if testing
    app.config.from_pyfile('config.py', silent=True)
    if test_config is not None:
        app.config.config_mapping(test_config)

    # database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'] \
            .format(instance=app.instance_path)
    db.init_app(app)

    # simple page
    @app.route('/hello')
    def hello():
        return 'Henlo ,warld!'

    # pages
    # app.register_blueprint(some.bp)

    # model
    # ap.register_blueprint(some.bp)

    # commandline interface
    # app.cli.add_command(command)

    return app


app = create_app()
