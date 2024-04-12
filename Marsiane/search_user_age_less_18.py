from data import db_session
from data.users import User
from data.jobs import Jobs


def global_init(name):
    db_session.global_init("db/mars_explorer.db")


def create_session():
    db_sess = db_session.create_session()
    return db_sess


global_init(input())
db_sess = create_session()

for elem in db_sess.query(User).filter((User.position == 'chef') | (User.position == 'middle')).all():
    print(f'{elem} {elem.position} {elem.speciality}')
