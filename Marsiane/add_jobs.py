from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("./db/mars_explorer.db")

job = Jobs()
job.team_leader = 1
job.job = 'Найти золото'
job.work_size = 5
job.collaborators = '2'
job.is_finished = True
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 2
job.job = 'Починить корабль'
job.work_size = 10
job.collaborators = '2'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 3
job.job = 'Убраться'
job.work_size = 2
job.collaborators = '1'
job.is_finished = True
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 4
job.job = 'Отдохнуть'
job.work_size = 1
job.collaborators = '1'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 5
job.job = 'Заработать деньги'
job.work_size = 20
job.collaborators = '2'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()