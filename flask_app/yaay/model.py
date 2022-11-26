from yaay.db import db


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column('id', db.Integer(), primary_key=True)

    # Fields
    info = db.Column('info', db.String(), nullable=False)
    stage_amount = db.Column('stage_amount', db.Integer(), nullable=False)
    max_tries = db.Column('max_tries', db.Integer(), default=3, nullable=False)

    # Relationships
    users = db.relationship('User')
    tasks = db.relationship('EventTask')


class User(db.Model):
    __tablename__ = 'user'

    token = db.Column('token', db.String(), primary_key=True)

    # Foreign keys
    event_id = db.Column('event_id', db.Integer(),
                         db.ForeignKey('event.id'), nullable=False)
    active_task_id = db.Column('active_task_id', db.String(
    ), db.ForeignKey('task.filename'), nullable=False)

    # Fields
    stage = db.Column('stage', db.Integer(), default=1)
    is_finished = db.Column('is_finished', db.Boolean(), default=False)
    is_received = db.Column('is_received', db.Boolean(), default=False)
    
    try_number = db.Column('try_number', db.Integer(), default=1)

    # Relationships
    event = db.relationship('Event', back_populates='users')
    active_task = db.relationship('Task', back_populates='user')
    tasks = db.relationship('UserTask')


class Task(db.Model):
    __tablename__ = 'task'

    filename = db.Column('filename', db.String(), primary_key=True)

    # Fields
    answer = db.Column('answer', db.String(), nullable=False)
    title = db.Column('title', db.String(), nullable=False)

    # Relationships
    user = db.relationship("User")
    users = db.relationship('UserTask')
    events = db.relationship('EventTask')


class UserTask(db.Model):
    __tablename__ = 'user_task'
    
    user_task_id = db.Column('user_task_id', db.Integer(), primary_key=True)

    # Foreign + primary keys
    user_id = db.Column('user_id', db.String(), db.ForeignKey('user.token'))
    task_id = db.Column('task_id', db.String(), db.ForeignKey('task.filename'))

    # Relationships
    user = db.relationship('User', back_populates='tasks')
    task = db.relationship('Task', back_populates='users')


class EventTask(db.Model):
    __tablename__ = 'event_task'
    
    event_task_id = db.Column('event_task_id', db.Integer(), primary_key=True)

    # Foreign + primary keys
    event_id = db.Column('event_id', db.Integer(), db.ForeignKey('event.id'))
    task_id = db.Column('task_id', db.String(), db.ForeignKey('task.filename'))

    # Relationships
    event = db.relationship('Event', back_populates='tasks')
    task = db.relationship('Task', back_populates='events')


class Survey(db.Model):
    __tablename__ = 'survey'

    user_token = db.Column('user_token', db.String(), db.ForeignKey('user.token'), primary_key=True)
    gender = db.Column('gender', db.String(), nullable=False)
    age = db.Column('age', db.String(), nullable=False)
    education = db.Column('education', db.String(), nullable=False)
