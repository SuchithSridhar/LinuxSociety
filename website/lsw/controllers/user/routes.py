import flask as f
import flask_login as fl

from . import utils as user_utils
from ... import db

user_blueprint = f.Blueprint('user', __name__)


@user_blueprint.route("/login", methods=['get', 'post'])
def login():
    if fl.current_user.is_authenticated:
        return f.redirect(f.url_for('user.index'))

    if f.request.method == 'POST':
        email = f.request.form['email']
        password = f.request.form['password']

        user = utils.authenticate_user(email, password, db)
