import flask_login as fl
from . import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


class User(db.Model, fl.UserMixin):
    id = db.Column(db.String, primary_key=True, default=Util.create_uuid)
    email = db.Column(db.String, unique=True, nullable=False)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    roles = db.Column(db.String)

    def __repr__(self):
        return f"<User '{self.id[-6:]}': '{self.email}'>"

    def set_roles(self, roles: list):
        self.roles
