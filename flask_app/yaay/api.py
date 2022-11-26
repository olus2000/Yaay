from flask import Blueprint, current_app
from flask.json import jsonify

from yaay.db import db
from yaay.model import Event, User, Task, UserTask

from secrets import token_hex
from random import choice

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/start/<string:event_id>')
def start(event_id):
    ''' generates user token '''
    token = token_hex(16)
    tasks = Task.query.all()
    task_filename = choice(tasks).filename
    user = User(token=token, event_id=event_id, active_task_id=task_filename)
    user_task = UserTask(user_id=token, task_id=task_filename)
    
    db.session.add(user)
    db.session.add(user_task)
    db.session.commit()
    response = jsonify(token)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@bp.route('/task/<string:token>')
def task(token):
    user = User.query.filter_by(token=token).first()
    task = Task.query.filter_by(filename=user.active_task_id).first()
    with open('yaay/static/tasks/' + task.filename) as f:
        question = f.readlines()
    
    num_of_tasks = Event.query.filter_by(id=user.event_id).first().stage_amount
    
    response = jsonify({
        'task': question,
        'title': task.title,
        'try_num': user.try_number,
        'max_tries': user.tries_max_triesleft,
        'task_number': user.task,
        'max_task_number': num_of_tasks
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@bp.route('/check/<string:token>')
def check(token):
    ''' dostaje token i rozwiązanie zwraca 0,1,2, update'uje zadanko '''
    return jsonify(1)


@bp.route('/end/<string:token>')
def end(token):
    ''' bierze token, daje content eventu i coś tam jeszcze nie wiem w sumie '''
    return jsonify('Przyjdź na targi pracy na PW żeby odebrać nagrodę!!!!!!!!!!')
