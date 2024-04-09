from flask import Flask, render_template, redirect, request, abort
from flask_login import login_user, LoginManager, current_user, login_required, logout_user

from data import db_session
from data.login_forming import LoginForm
from data.user_forming import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("./db/journal.db")
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route("/menu", methods=['GET', 'POST'])
def menu():
    if current_user.is_authenticated:
       return render_template("menu.html", current_user=current_user)
    return redirect("/login")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        logout_user()
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/menu")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
