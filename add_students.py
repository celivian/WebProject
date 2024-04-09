from data.student import Student
from data.user_forming import User
from flask import Flask
from data import db_session
from data.marks_forming import Marks

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("./db/journal.db")

user = Student()
user.surname = "Илюкин"
user.name = "Сергей"
user.login = 'tests'
user.classs = '9Б'
user.age = 15
user.role = 'Ученик'
user.address = "module_1"
user.hashed_password = '12345'
user.setPassword(user.hashed_password)
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()