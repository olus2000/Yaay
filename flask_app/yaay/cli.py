import click
from flask import current_app
from flask.cli import with_appcontext

from yaay.db import db
from yaay.model import *

from .model import Event, Task

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
    event = Event(info=info, stage_amount=stage_amount)
    db.session.add(event)
    db.session.commit()

    print(f'Created event with ID {event.id}')


# Add a task
@click.command('add-task')
@click.option('--filename', required=True)
@click.option('--title', required=True)
@click.option('--answer', required=True)
@with_appcontext
def add_task(filename, title, answer):
    task = Task(filename=filename, title=title, answer=answer)
    db.session.add(task)
    db.session.commit()

    print(f'Created task with title {task.title}')


# Add task to event
@click.command('add-task-to-event')
@click.option('--filename', required=True)
@click.option('--event-id', required=True, type=int)
@with_appcontext
def add_task_to_event(filename, event_id):
    tasks = Task.query.all()
    events = Event.query.all()
    found = False
    for task in tasks:
        if task.filename == filename:
            found = True
    if not found:
        print("Task not found")
        return
    found = False
    for event in events:
        if event.id == event_id:
            found = True
    if not found:
        print("Event not found")
        return
    task_to_event = EventTask(event_id=event_id, task_id=filename)
    db.session.add(task_to_event)
    db.session.commit()

    print(f'Connected Event {task_to_event.event_id} with task {task_to_event.task_id}')
