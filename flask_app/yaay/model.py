from yaay.db import db


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column('id', db.BigInteger(), primary_key=True)

    # Fields
    info = db.Column('info', db.String(), nullable=False)
    stage_amount = db.Column('stage_amount', db.Integer(), nullable=False)

    # Relationships
    users = db.relationship('User')
    tasks = db.relationship('EventTask')


class User(db.Model):
    __tablename__ = 'user'

    token = db.Column('token', db.String(), primary_key=True)

    # Foreign keys
    event_id = db.Column('event_id', db.BigInteger(),
                         db.ForeignKey('event.id'), nullable=False)
    active_task_id = db.Column('active_task_id', db.String(
    ), db.ForeignKey('task.filename'), nullable=False)

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
    users = db.relationship('User')
    tasks_users = db.relationship('TaskUser')
    event_tasks = db.relationship('EventTask')


class EventUser(db.Model):
    __tablename__ = 'event_task'

    id = db.Column('id', db.BigInteger(), primary_key=True)

    # Foreign keys
    user_id = db.Column('user_id', db.BigInteger(),
                        db.ForeignKey('user.id'), nullable=False)
    active_task_id = db.Column('active_task_id', db.String(), db.ForeignKey('task.filename'), nullable=False)

    # Relationships
    users = db.relationship('User', back_populates='users')
    tasks = db.relationship('Task', back_populates='tasks')


class TaskUser(db.Model):
    __tablename__ = 'task_user'

    id = db.Column('id', db.BigInteger(), primary_key=True)

    # Foreign keys
    event_id = db.Column('event_id', db.BigInteger(), db.ForeignKey('event.id'), nullable=False)
    task_id = db.Column('task_id', db.String(), db.ForeignKey('task.filename'), nullable=False)

    # Relationships
    event = db.relationship('User', back_populates='users')
    tasks = db.relationship('Task', back_populates='tasks')
