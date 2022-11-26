import click
from flask import current_app
from flask.cli import with_appcontext

from yaay.db import db
from yaay.model import *


# Setup the database after installation or changing the model
@click.command('init-db')
@click.option('--reset/--no-reset', default=False)
@with_appcontext
def init_db(reset):
    print(current_app.config['SQLALCHEMY_DATABASE_URI'])
    if reset:
        print('Clearing the database.')
        db.drop_all()

    db.create_all()
    print('Database initialised.')


# Add an event
@click.command('add-event')
@click.option('--info', required=True)
@click.option('--stage-amount', required=True, type=int)
@with_appcontext
def add_event(info, stage_amount):
    db.session.add(Event(info=info, stage_amount=stage_amount))
    db.session.commit()

    print(f'Created event with ID {Event.id}')


# Add a task
@click.command('add-task')
@click.option('--filename')
@click.option('--title')
@click.option('--answer')
@with_appcontext
def add_task(filename, title, answer):
    task = Task(filename=filename, title=title, answer=answer)
    db.session.add(task)
    db.session.commit()

    print(f'Created task with title {task.title}')


# Add task to event
@click.command('add-task-to-event')
# @click.option('--')
def add_task_to_event(stuff):
    ...

