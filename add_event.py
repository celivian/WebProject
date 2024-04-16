
from flask import Flask
from data import db_session

from data.events_forming import  Events

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("./db/journal.db")

ad = Events()
ad.owner_id = 2
ad.name = 'Событие'
ad.discription = 'очень весело'
ad.month = 'Март'
ad.day = '18'
ad.year = '2024'
db_sess = db_session.create_session()
db_sess.add(ad)
db_sess.commit()