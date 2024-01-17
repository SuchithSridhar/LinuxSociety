import flask as f
import flask_login as fl

from . import utils as user_utils
from ... import models

user_blueprint = f.Blueprint('user', __name__)


@user_blueprint.route("/login", methods=['get', 'post'])
def login():
    if fl.current_user.is_authenticated:
        return f.redirect(f.url_for('main.index'))

    if f.request.method == 'POST':
        email = f.request.form['email']
        password = f.request.form['password']

        user: models.User = user_utils.authenticate_user(email, password)
        if (user is None):
            return f.render_template(
                'pages/user/login.jinja', title='User Login'
            )

        fl.login_user(user)
        next_page = f.request.args.get('next')
        return f.redirect(next_page) if next_page else f.redirect(
            f.url_for('main.index'))

    return f.render_template('pages/user/login.jinja', title='User Login')


@user_blueprint.route("/user/view-members")
@fl.login_required
def view_members():

    email = fl.current_user.email
    user = models.User.query.filter_by(email=email).first()

    if user is None or not user.has_role('admin'):
        return f.abort(403)

    members = models.Member.query.order_by(
                models.Member.registration_date.desc()).paginate(per_page=20)

    return f.render_template(
        'pages/user/view-members.jinja',
        title="View Members",
        members=members
    )
