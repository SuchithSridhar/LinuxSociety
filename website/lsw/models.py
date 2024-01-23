import flask_login as fl
from . import db, login_manager
from .utils import Utils


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.String, primary_key=True, default=Utils.create_uuid)
    name = db.Column(db.String, nullable=False)
    program = db.Column(db.String, nullable=True)
    student_id = db.Column(db.String, nullable=True)
    primary_email = db.Column(db.String, nullable=False)
    university_email = db.Column(db.String, nullable=True)
    registration_date = db.Column(db.DateTime, default=Utils.date_now)
    event_notification = db.Column(db.Boolean, default=True)
    year_of_study = db.Column(db.Integer)


class User(db.Model, fl.UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.String, primary_key=True, default=Utils.create_uuid)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    roles = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=Utils.date_now)

    created_by_id = db.Column(db.String, db.ForeignKey('user.id'))
    created_by = db.relationship('User', backref=db.backref('user', lazy=True, remote_side=[id]))

    member_id = db.Column(db.String, db.ForeignKey('member.id'))
    member = db.relationship('Member', backref='member')

    def __repr__(self):
        return f"<User '{self.id[-6:]}': '{self.email}'>"

    def set_roles(self, roles: list):
        self.roles = ','.join(roles)

    def get_roles(self) -> list:
        return self.roles.split(",")

    def has_role(self, role: str) -> bool:
        return role in self.get_roles()

    def add_role(self, role: str):
        self.set_roles(self.get_roles().append(role))

    def remove_role(self, role: str):
        self.set_roles(self.get_roles().remove(role))
