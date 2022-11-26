from flask import Blueprint, current_app, request
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
    if not Event.query.filter_by(id=event_id).first():
        print('h..hi?')
        response = jsonify('wrong event')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
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
    if not user:
        response = jsonify('ERROR')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    task = Task.query.filter_by(filename=user.active_task_id).first()
    with open('yaay/static/tasks/' + task.filename) as f:
        question = f.readlines()
    
    num_of_tasks = Event.query.filter_by(id=user.event_id).first().stage_amount
    
    response = jsonify({
        'task': question,
        'title': task.title,
        'try_num': user.try_number,
        'max_tries': user.max_tries,
        'task_number': user.stage,
        'max_task_number': num_of_tasks
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@bp.route('/check/<string:token>', methods=['POST'])
def check(token):
    user = User.query.filter_by(token=token).first()
    task = Task.query.filter_by(filename=user.active_task_id).first()
    num_of_tasks = Event.query.filter_by(id=user.event_id).first().stage_amount
    answer = list(request.form.keys())[0]
    
    
    if answer == task.answer and user.stage == num_of_tasks:
        response = jsonify(2)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    if answer == task.answer:
        user.try_number = 1
        tasks_done = UserTask.query.filter_by(user_id=user.token).all()
        new_task = choice(Task.query.all())
        while new_task.filename in tasks_done:
            new_task = choice(Task.query.all())
        user.active_task_id = new_task.filename
        user_task = UserTask(user_id=token, task_id=new_task.filename)
        db.session.add(user_task)
        db.session.commit()
        response = jsonify(1)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    user.try_number += 1
    db.session.commit()
    if user.try_number > user.max_tries:
        response = jsonify(0)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    response = jsonify(1)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    


@bp.route('/end/<string:token>')
def end(token):
    ''' bierze token, daje content eventu i coś tam jeszcze nie wiem w sumie '''
    return jsonify('Przyjdź na targi pracy na PW żeby odebrać nagrodę!!!!!!!!!!')
