global_init(input())
db_sess = create_session()

for elem in db_sess.query(User).filter(User.address == 'module_1', User.speciality.notlike('%engineer%'),
                                       User.position.notlike('%engineer%')).all():
    print(elem.id)
