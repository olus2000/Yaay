from flask import Blueprint, current_app, request
from flask.json import jsonify
from sqlalchemy.sql.expression import exists

from yaay.db import db
from yaay.model import Event, User, Task, UserTask, EventTask, Survey

from secrets import token_hex
from random import choice

bp = Blueprint('api', __name__, url_prefix='/api')

def create_response(text):
    response = jsonify(text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@bp.route('/start/<string:event_id>')
def start(event_id):
    ''' generates user token '''
    token = token_hex(16)
    tasks = Task.query.join(EventTask).join(Event).filter(Event.id == event_id).all()
    task_filename = choice(tasks).filename
    if Event.query.filter_by(id=event_id).one_or_none() is None:
        return create_response('wrong event')
    user = User(token=token, event_id=event_id, active_task_id=task_filename)
    user_task = UserTask(user_id=token, task_id=task_filename)
    
    db.session.add(user)
    db.session.add(user_task)
    db.session.commit()
    return create_response(token)


@bp.route('/task/<string:token>')
def task(token):
    user = User.query.filter_by(token=token).one_or_none()
    if user is None:
        return create_response('ERROR')
    task = Task.query.filter_by(filename=user.active_task_id).first()
    with open('yaay/static/tasks/' + task.filename) as f:
        question = f.readlines()
    
    event = Event.query.filter_by(id=user.event_id).one()
    
    return create_response({
        'task': question,
        'title': task.title,
        'try_num': user.try_number,
        'max_tries': event.max_tries,
        'task_number': user.stage,
        'max_task_number': event.stage_amount,
        'is_finished': user.is_finished
    })


@bp.route('/check/<string:token>', methods=('POST',))
def check(token):
    user = User.query.filter_by(token=token).first()
    task = Task.query.filter_by(filename=user.active_task_id).first()
    event = Event.query.filter_by(id=user.event_id).first()
    print(dict(request.form))
    answer = list(request.form.keys())[0]

    if user.try_number > event.max_tries:
        return create_response(0)
    
    # print(f'{user.stage=}, {event.stage_amount=}')
    if answer == task.answer and user.stage == event.stage_amount:
        user.is_finished = True
        db.session.commit()
        return create_response(2)

    if answer == task.answer:
        user.try_number = 1
        user.stage += 1

        viable_tasks = Task.query.join(EventTask).join(Event).filter(Event.id == event.id) \
                .filter(~exists().where(UserTask.task_id == Task.filename)).all()
        new_task = choice(viable_tasks)
        user.active_task_id = new_task.filename
        user_task = UserTask(user_id=token, task_id=new_task.filename)
        db.session.add(user_task)
        db.session.commit()
        return create_response(1)


    user.try_number += 1
    db.session.commit()
    if user.try_number > event.max_tries:
        return create_response(0)
    
    return create_response(1)
    

@bp.route('/end/<string:token>')
def end(token):
    ''' bierze token, daje content eventu '''
    user = User.query.filter_by(token=token).first()
    if not user.is_finished:
        return create_response('error')
    event = Event.query.filter_by(id=user.event_id).first()
    return create_response(event.info)


@bp.route('/survey/<string:token>', methods=('POST',))
def survey(token):
    survey = Survey.query.filter(Survey.user_token == token).one_or_none()
    if survey is None:
        survey = Survey(
                user_token=token,
                age=request.json['age'],
                gender=request.json['gender'],
                education=request.json['education'],
        )
        db.session.add(survey)
    else:
        survey.update(dict(request.json))

    db.session.commit()

    return create_response(1)

