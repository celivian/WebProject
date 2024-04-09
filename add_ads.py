
from flask import Flask
from data import db_session

from data.ads_forming import Ads

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("./db/journal.db")

ad = Ads()
ad.owner_id = 2
ad.ad_name = 'Второй'
ad.discription = 'пкушопшупоукопшщзукошп'
db_sess = db_session.create_session()
db_sess.add(ad)
db_sess.commit()