from flask import Flask, render_template, redirect, request, abort
from flask_login import login_user, LoginManager, current_user, login_required, logout_user

from data import db_session
from data.ads_forming import Ads
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
    return db_sess.get(User, user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route("/menu/ads", methods=['GET', 'POST'])
def menu_ads():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        ads = db_sess.query(Ads).all()
        return render_template("menu_ads.html", current_user=current_user, ads=ads)
    return redirect("/login")


@app.route("/menu/profile", methods=['GET', 'POST'])
def menu_profile():
    if current_user.is_authenticated:
        return render_template("menu_profile.html", current_user=current_user)
    return redirect("/login")


@app.route("/menu/admin", methods=['GET', 'POST'])
def menu_admin():
    if current_user.is_authenticated and current_user.role == 'admin':
        return render_template("menu_admin.html", current_user=current_user)
    return redirect("/login")


@app.route("/menu/timetable", methods=['GET', 'POST'])
def menu_timetable():
    if current_user.is_authenticated:
        return render_template("menu_timetable.html", current_user=current_user)
    return redirect("/login")


@app.route("/menu/marks", methods=['GET', 'POST'])
def menu_marks():
    if current_user.is_authenticated:
        return render_template("menu_marks.html", current_user=current_user)
    return redirect("/login")


@app.route("/menu/class", methods=['GET', 'POST'])
def menu_class():
    if current_user.is_authenticated:
        return render_template("menu_class.html", current_user=current_user)
    return redirect("/login")


@app.route("/menu/calendar", methods=['GET', 'POST'])
def menu_calendar():
    if current_user.is_authenticated:
        return render_template("menu_calendar.html", current_user=current_user)
    return redirect("/login")


@app.route("/menu/teacher", methods=['GET', 'POST'])
def menu_teacher():
    if current_user.is_authenticated and current_user.role == 'teacher':
        return render_template("menu_teacher.html", current_user=current_user)
    return redirect("/login")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/menu/ads")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
