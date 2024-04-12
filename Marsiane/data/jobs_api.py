import flask
from flask import make_response, jsonify, request
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs/<job_id>', methods=["GET"])
def get_job(job_id):
    db_sess = db_session.create_session()
    try:
        i = db_sess.query(Jobs).get(job_id)
        if not i:
            return make_response(jsonify({'error': 'Not found'}), 404)
        data = {'jobs': [{'id': i.id, 'team_leader': i.team_leader, 'job': i.job, 'work_size': i.work_size,
                          'collaborators': i.collaborators, 'is_finished': i.is_finished, 'start_date': i.start_date,
                          'end_date': i.end_date}]}
        return flask.jsonify(data)
    except Exception:
        return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.route('/api/jobs/<jobs_id>', methods=['DELETE', 'GET'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    try:
        jobs = db_sess.query(Jobs).get(jobs_id)
        if not jobs:
            return make_response(jsonify({'error': 'Not found'}), 404)
        db_sess.delete(jobs)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    except Exception:
        return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.route('/api/jobs/<jobs_id>', methods=['GET', 'POST'])
def edit_jobs(jobs_id):
    db_sess = db_session.create_session()
    try:
        jobs = db_sess.query(Jobs).get(jobs_id)
        if not jobs:
            return make_response(jsonify({'error': 'Not found'}), 404)
        elif not request.json:
            return make_response(jsonify({'error': 'Empty request'}), 400)
        elif not all(key in request.json for key in
                     ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
            return make_response(jsonify({'error': 'Bad request'}), 400)
        jobs.team_leader = request.json['team_leader']
        jobs.job = request.json['job']
        jobs.work_size = request.json['work_size']
        jobs.collaborators = request.json['collaborators']
        jobs.is_finished = request.json['is_finished']
        db_sess.commit()
        return jsonify({'success': 'OK'})
    except Exception:
        return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.route('/api/jobs', methods=['GET', 'POST'])
def get_jobs():
    db_sess = db_session.create_session()
    if flask.request.method == 'GET':
        jobs = db_sess.query(Jobs).all()
        data = {'jobs': [{'id': i.id, 'team_leader': i.team_leader, 'job': i.job, 'work_size': i.work_size,
                          'collaborators': i.collaborators, 'is_finished': i.is_finished, 'start_date': i.start_date,
                          'end_date': i.end_date} for i in jobs]}
        return flask.jsonify(data)
    elif flask.request.method == 'POST':
        if not request.json:
            return make_response(jsonify({'error': 'Empty request'}), 400)
        elif not all(key in request.json for key in
                     ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
            return make_response(jsonify({'error': 'Bad request'}), 400)
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=request.json['team_leader'],
            job=request.json['job'],
            work_size=request.json['work_size'],
            collaborators=request.json['collaborators'],
            is_finished=request.json['is_finished']
        )
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'id': job.id})
