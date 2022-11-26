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

    if reset:
        #populating database
        populate_database()

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
    task = Task.query.filetr(Task.filename == filename).one_or_none()
    event = Event.query.filter(Event.id == event_id).one_or_none()
    if task is None:
        print("Task not found")
        return
    if event is None:
        print("Event not found")
        return
    task_to_event = EventTask(event_id=event_id, task_id=filename)
    db.session.add(task_to_event)
    db.session.commit()

    print(f'Connected Event {task_to_event.event_id} with task {task_to_event.task_id}')


@click.command('show')
@click.option('--task', default=False, is_flag=True)
@click.option('--event', default=False, is_flag=True)
@click.option('--event-task', default=False, is_flag=True)
@with_appcontext
def show(task, event, event_task):
    if task:
        print(Task.query.all())
    if event:
        print(Event.query.all())
    if event_task:
        print(EventTask.query.all())

def populate_database():
    db.session.add(Event(info="Hackathon Goldman Sachs", stage_amount=3))
    db.session.add(Event(info="PW Job Fairs", stage_amount=3))
    db.session.add(Event(info="Women in Tech", stage_amount=3))

    db.session.add(Task(filename="bit_sum.TXT", answer="2137", title="Bit Sum"))
    db.session.add(Task(filename="fib.TXT", answer="68245678", title="Fibonacci"))
    db.session.add(Task(filename="median.TXT", answer="median", title="Median"))
    db.session.add(Task(filename="employees.TXT", answer="43900", title="Employees"))
    db.session.add(Task(filename="foundation.TXT", answer="1869", title="Foundation"))
    db.session.add(Task(filename="sector.TXT", answer="banking", title="Sector"))
    db.session.add(Task(filename="sum.TXT", answer="56", title="Sum"))
    db.session.add(Task(filename="headquarter.TXT", answer="New York", title="Headquarter"))

    db.session.add(EventTask(event_id=2, task_id="bit_sum.TXT"))
    db.session.add(EventTask(event_id=2, task_id="fib.TXT"))
    db.session.add(EventTask(event_id=2, task_id="median.TXT"))
    db.session.add(EventTask(event_id=2, task_id="sum.TXT"))
    db.session.add(EventTask(event_id=1, task_id="employees.TXT"))
    db.session.add(EventTask(event_id=1, task_id="sector.TXT"))
    db.session.add(EventTask(event_id=1, task_id="foundation.TXT"))
    db.session.add(EventTask(event_id=1, task_id="headquarter.TXT"))

    print('Database populated')

    db.session.commit()
