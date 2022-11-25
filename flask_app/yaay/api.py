from flask import Blueprint, current_app
from flask.json import jsonify

from yaay.db import db
from yaay.model import Event


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/start')
def start():
    ''' nic nie bierze, daje token '''
    return jsonify('ZajebistyToken2137')


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
