from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("./db/mars_explorer.db")

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 11
user.position = "middle"
user.speciality = "research engineer"
user.address = "module_1"
user.hashed_password = '12345'
user.setPassword(user.hashed_password)
user.email = "scott_chief@mars.org1133"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

