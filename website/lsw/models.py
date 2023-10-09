import flask_login as fl
from . import db, login_manager
from .utils import Utils


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


class User(db.Model, fl.UserMixin):
    id = db.Column(db.String, primary_key=True, default=Utils.create_uuid)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    roles = db.Column(db.String)

    def __repr__(self):
        return f"<User '{self.id[-6:]}': '{self.email}'>"

    def set_roles(self, roles: list):
        self.roles = ','.join(roles)

    def get_roles(self):
        return self.roles.split(",")


class Member(db.Model):
    id = db.Column(db.String, primary_key=True, default=Utils.create_uuid)
    name = db.Column(db.String, unique=False, nullable=False)
    program = db.Column(db.String, unique=False, nullable=True)
    student_id = db.Column(db.String, unique=True, nullable=True)
    primary_email = db.Column(db.String, unique=True, nullable=False)
    university_email = db.Column(db.String, unique=True, nullable=True)
    registration_date = db.Column(db.DateTime, default=Utils.date_now)
    event_notification = db.Column(db.Boolean, default=True)
