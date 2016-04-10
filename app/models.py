from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    pin = db.Column(db.Integer)

    @property
    def is_authenticated(self):
        return True
  
    @property
    def is_active(self):
        return True
  
    @property
    def is_anonymous(self):
        return False

class Job(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    description = db.Column(db.String(120))


class Work(db.Model):
    work_id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), db.ForeignKey('user.username'))
    job = db.Column(db.String(64), db.ForeignKey('job.name'))
    date_time = db.Column(db.DateTime())
    comment = db.Column(db.String(120))
