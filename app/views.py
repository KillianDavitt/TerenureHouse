from app import app
from flask import render_template, request, redirect

from app import app, db, lm
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import PinForm
from .models import User, Job, Work

from datetime import datetime

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
@app.route('/index')
@login_required
def index():

    jobs = Job.query.filter_by(active=True).all()

    user = User.query.order_by(User.username).all()

    complete_list = []

    for job in jobs:
        work = list(reversed(Work.query.filter_by(job=job.name).order_by(Work.date_time.desc()).limit(5).all()))
        complete_list.append((job,work))


    return render_template('index.html', complete_list=complete_list, user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    pin_form = PinForm()

    user = User.query.filter_by().first()

    if pin_form.validate_on_submit():
        pin = pin_form.pin.data
        if pin==9112016:
            login_user(user, remember=True)
            return redirect('/')

    u = User.query.all()
    return render_template('login.html', users=u, pin_form=pin_form)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/add_job', methods=['POST'])
def add_job():
    job = request.form['job']

    if job != "":
        new_job = Job(name=job, description="", active=True)

        db.session.add(new_job)
        db.session.commit()

    return redirect('/')

@app.route('/add_work', methods=['POST'])
def add_work():
    job = request.form['job']
    user = request.form['user']
    if job != "" and not user is None:
        new_work = Work(user=user, job=job, date_time=datetime.now(), comment="")
    
        db.session.add(new_work)
        db.session.commit()
    
    return redirect('/')


