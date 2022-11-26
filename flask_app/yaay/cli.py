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

    #initializing database
    db.session.add(Event(info="Hackathon Goldman Sachs", stage_amount=5))
    db.session.add(Event(info="PW Work Trades", stage_amount=3))
    db.session.add(Event(info="Studen Debil Day", stage_amount=2))
    db.session.add(Task(filename="bit_sum.TXT", answer="2137", title="Bit Sum"))
    db.session.add(Task(filename="fib.TXT", answer="alot", title="Fibonacci"))
    db.session.add(Task(filename="median.TXT", answer="mediana", title="Mediana"))
    db.session.add(EventTask(event_id=3, task_id="bit_sum.TXT"))
    db.session.add(EventTask(event_id=3, task_id="fib.TXT"))
    db.session.add(EventTask(event_id=3, task_id="median.TXT"))
    db.session.commit()

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


@click.command('show')
@click.option('--task', default=False)
@click.option('--event', default=False)
@click.option('--event-task', default=False)
@with_appcontext
def show(task, event, event_task):
    if task:
        print(Task.query.all())
    if event:
        print(Event.query.all())
    if event_task:
        print(EventTask.query.all())
