from app import app
from flask import render_template

from app import app, db, lm
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import PinForm
from .models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    pin_form = PinForm()

    if pin_form.validate_on_submit():
        user = pin_form.user.data
        pin = pin_form.pin.data
        user = User.query.filter_by(username=user).first()
        if user.pin == pin:
            login_user(user.username)
            return redirect('/')

    u = User.query.all()
    return render_template('login.html', users=u, pin_form=pin_form)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


def add_job():
    

def add_work():


