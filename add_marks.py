from data.user_forming import User
from flask import Flask
from data import db_session
from data.marks_forming import Marks

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("./db/journal.db")

subject = Marks()
subject.owner_id = 1
subject.rus = '2'
subject.math = '3'
subject.bio = '4'
subject.geo = '5'
subject.hist = '1'
db_sess = db_session.create_session()
db_sess.add(subject)
db_sess.commit()