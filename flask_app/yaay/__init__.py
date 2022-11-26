import os
import os.path
import re

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from yaay import api
from yaay.db import db
from yaay.cli import init_db, add_event, add_task, add_task_to_event, show


def create_app(test_config=None):
    global db

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
    app.register_blueprint(api.bp)

    # commandline interface
    app.cli.add_command(init_db)
    app.cli.add_command(add_event)
    app.cli.add_command(add_task)
    app.cli.add_command(add_task_to_event)
    app.cli.add_command(show)

    @app.after_request
    def handle_CORS(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'content-type'
        return response

    return app


app = create_app()
