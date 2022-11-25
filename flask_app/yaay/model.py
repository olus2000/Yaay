from yaay.db import db


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column('id', db.BigInteger(), primary_key=True)

    # Fields
    info = db.Column('info', db.String(), nullable=False)
    stage_amount = db.column('stage_amount', db.Integer(), nullable=False)

    # Relationships
    users = db.relationship('User')
    tasks = db.relationship('EventTask')


class User(db.Model):
    __tablename__ = 'user'

    token = db.Column('token', db.String(), primary_key=True)

    # Foreign keys
    event_id = db.Column('event_id', db.BigInteger(), db.ForeignKey('event.id'), nullable=False)
    active_task_id = db.Column('active_task', db.String(), db.ForeignKey('task.id'))

    # Fields
    stage = db.Column('stage', db.Integer(), default=1)
    is_finished = db.Column('is_finished', db.Boolean(), default=False)
    is_received = db.Column('is_received', db.Boolean(), default=False)

    # Relationships
    event = db.relationship('Event', back_populates='users')
    active_task = db.relationship('Task', back_populates='users')
    tasks = db.relationship('UserTask')


class Task(db.Model):
    __tablename__ = 'task'

    filename = db.Column('filename', db.String(), primary_key=True)

    # Fields 
    answer = db.Column('answer', db.String(), nullable=False)

    # Relationships


