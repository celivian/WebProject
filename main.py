from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager
from flask_login.utils import login_user, current_user, login_required, logout_user

from data import db_session
from data.ads_form import AdsForm
from data.ads_forming import Ads
from data.events_form import EventsForm
from data.events_forming import Events
from data.login_form import LoginForm
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


@app.route('/')
def peresilka():
    return redirect("/login")

@app.route('/logout')
def logout():
    logout_user()
    return redirect("/login")


@app.route("/menu/ads", methods=['GET', 'POST'])
@login_required
def menu_ads():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        ads = db_sess.query(Ads).all()
        return render_template("menu_ads.html", current_user=current_user, ads=ads)
    return redirect("/login")


@app.route("/menu/profile", methods=['GET', 'POST'])
@login_required
def menu_profile():
    if current_user.is_authenticated:
        return render_template("menu_profile.html", current_user=current_user)
    return redirect("/login")


@app.route("/ads/add", methods=['GET', 'POST'])
@login_required
def add_ads():
    if current_user.is_authenticated and current_user.role == 'admin':
        form = AdsForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            ad = Ads()
            ad.owner_id = current_user.id
            ad.ad_name = form.ad_name.data
            ad.discription = form.discription.data
            db_sess.add(ad)
            db_sess.commit()
            return redirect('/menu/ads')
        return render_template("add_ads.html", current_user=current_user, form=form)
    return redirect('/login')


#     return redirect('/menu/ads')
# return render_template('add_jobs.html', title='Добавление работы',
#                        form=form)
# return redirect("/login")


@app.route("/menu/admin", methods=['GET', 'POST'])
@login_required
def menu_admin():
    if current_user.is_authenticated and current_user.role == 'admin':
        return render_template("menu_admin.html", current_user=current_user)
    return redirect("/login")


@app.route("/menu/timetable", methods=['GET', 'POST'])
@login_required
def menu_timetable():
    if current_user.is_authenticated:
        return render_template("menu_timetable.html", current_user=current_user)
    return redirect("/login")


@app.route("/menu/marks", methods=['GET', 'POST'])
@login_required
def menu_marks():
    if current_user.is_authenticated:
        return render_template("menu_marks.html", current_user=current_user)
    return redirect("/login")


@app.route("/menu/class", methods=['GET', 'POST'])
@login_required
def menu_class():
    if current_user.is_authenticated:
        return render_template("menu_class.html", current_user=current_user)
    return redirect("/login")

@app.route("/calendar/events/<month>/<day>", methods=['GET', 'POST'])
@login_required
def get_event(month, day):
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        events = db_sess.query(Events).filter(Events.month == month, Events.day == day).first()
        print(events)
        return render_template("check.html", current_user=current_user, events=events, month=month, day=day)
    return redirect("/login")

@app.route("/calendar/events/add/<month>/<day>", methods=['GET', 'POST'])
@login_required
def add_event(month, day):
    if current_user.is_authenticated and current_user.role == 'admin':
        db_sess = db_session.create_session()
        events = db_sess.query(Events).filter(Events.month == month, Events.day == day).first()
        form = EventsForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            ad = Events()
            ad.owner_id = current_user.id
            ad.name = form.name.data
            ad.discription = form.discription.data
            ad.day = day
            ad.month = month
            db_sess.add(ad)
            db_sess.commit()
            return redirect(f'/calendar/events/{month}/{day}')
        return render_template("add_event.html", current_user=current_user, events=events, form=form)
    return redirect('/login')

@app.route("/calendar/events/delete/<month>/<day>", methods=['GET', 'POST'])
@login_required
def del_event(month, day):
    if current_user.is_authenticated and current_user.role == 'admin':
        db_sess = db_session.create_session()
        events = db_sess.query(Events).filter(Events.month == month, Events.day == day).first()
        if events:
            db_sess.delete(events)
            db_sess.commit()
        else:
            abort(404)
        return redirect(f'/calendar/events/{month}/{day}')
    return redirect('/login')


@app.route("/menu/calendar", methods=['GET', 'POST'])
@login_required
def menu_calendar():
    if current_user.is_authenticated:
        return render_template("calendar.html", current_user=current_user, months=['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'])
    return redirect("/login")


@app.route("/menu/teacher", methods=['GET', 'POST'])
@login_required
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


@app.route('/ads/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def ads_delete(id):
    if current_user.is_authenticated and current_user.role == 'admin':
        db_sess = db_session.create_session()
        ads = db_sess.query(Ads).filter(Ads.id == id,
                                        (Ads.owner_id == current_user.id) | (current_user.role == 'admin')).first()
        if ads:
            db_sess.delete(ads)
            db_sess.commit()
        else:
            abort(404)
        return redirect('/menu/ads')
    return redirect('/login')


@app.route('/ads/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def ads_edit(id):
    if current_user.is_authenticated and current_user.role == 'admin':
        form = AdsForm()
        if request.method == "GET":
            db_sess = db_session.create_session()
            ads = db_sess.query(Ads).filter(Ads.id == id,
                                            (Ads.owner_id == current_user.id) | (current_user.role == 'admin')
                                            ).first()
            if ads:
                form.ad_name.data = ads.ad_name
                form.discription.data = ads.discription

            else:
                abort(404)
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            ads = db_sess.query(Ads).filter(Ads.id == id,
                                            (Ads.owner_id == current_user.id) | (current_user.role == 'admin')
                                            ).first()
            ads.owner_id = current_user.id
            ads.ad_name = form.ad_name.data
            ads.discription = form.discription.data
            db_sess.add(ads)
            db_sess.commit()
            return redirect('/menu/ads')
        return render_template("edit_ads.html", current_user=current_user, form=form)
    return redirect('/login')

@app.route("/calendar/events/edit/<month>/<day>", methods=['GET', 'POST'])
@login_required
def edit_event(month, day):
    if current_user.is_authenticated and current_user.role == 'admin':
        db_sess = db_session.create_session()
        events = db_sess.query(Events).filter(Events.month == month, Events.day == day).first()
        form = EventsForm()
        if form.validate_on_submit():
            events.owner_id = current_user.id
            events.name = form.name.data
            events.discription = form.discription.data
            events.day = day
            events.month = month
            db_sess.add(events)
            db_sess.commit()
            return redirect(f'/calendar/events/{month}/{day}')
        return render_template("add_event.html", current_user=current_user, events=events, form=form)
    return redirect('/login')

@app.route("/menu/admin/list/users", methods=['GET', 'POST'])
@login_required
def list_users():
    if current_user.is_authenticated and current_user.role == 'admin':
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return render_template()
    return redirect('/login')




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
