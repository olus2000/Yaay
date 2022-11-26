from flask import Blueprint, current_app
from flask.json import jsonify

from yaay.db import db
from yaay.model import Event, User, Task, UserTask

from secrets import token_bytes
from random import choice

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/start/<string:event_id>')
def start(event_id):
    ''' generates user token '''
    token = str(token_bytes(16))
    tasks = Task.query.all()
    task_filename = choice(tasks).filename
    user = User(token, event_id=event_id, active_task_id=task_filename)
    user_task = UserTask(token, task_filename)
    
    db.session.add(user)
    db.session.add(user_task)
    response = jsonify(token)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@bp.route('/task/<string:token>')
def task(token):
    ''' dostaje token, zwraca content taska, tytuł taska, liczbę prób, maksymalną liczbę prób, które zadanie, z ilu '''
    return jsonify({
        'task': 'Napisz co oznacza popularny młodzierzowy sktót "JD".',
        'title': 'Nienawidzę Greków',
        'tries': 6,
        'max_tries': 9,
        'task_number': 4,
        'max_task_number': 20,
    })


@bp.route('/check/<string:token>')
def check(token):
    ''' dostaje token i rozwiązanie zwraca 0,1,2, update'uje zadanko '''
    return jsonify(1)


@bp.route('/end/<string:token>')
def end(token):
    ''' bierze token, daje content eventu i coś tam jeszcze nie wiem w sumie '''
    return jsonify('Przyjdź na targi pracy na PW żeby odebrać nagrodę!!!!!!!!!!')
