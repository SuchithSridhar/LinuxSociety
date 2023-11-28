import flask as f
from ... import models
from ... import db

main_blueprint = f.Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return f.render_template('index.jinja', page='index')


@main_blueprint.route('/register', methods=['get'])
def register():
    return f.render_template('pages/register.jinja')


@main_blueprint.route('/register', methods=['post'])
def register_post():
    data = {
        'name': '',
        'primary-email': '',
        'university-email': '',
        'student-id': '',
        'year-of-study': '',
        'program': '',
        'event-notification': 'yes',
    }

    for key in data:
        data[key] = f.request.form[key]

    # Convert string to boolean
    data['event-notification'] = data['event-notification'] == 'yes'

    # TODO: Perform checks before creating new item
    # - Check if member is already registered.
    # - Perform validation on all fields.
    item = models.Member(
        name=data['name'],
        program=data['program'],
        student_id=data['student-id'],
        primary_email=data['primary-email'],
        university_email=data['university-email'],
        event_notification=data['event-notification'],
        year_of_study=data['year-of-study']
    )

    db.session.add(item)
    db.session.commit()

    return f.redirect(f.url_for('main.welcome'))


@main_blueprint.route('/welcome')
def welcome():
    return f.render_template('pages/welcome.jinja')


@main_blueprint.route('/privacy')
def privacy():
    return f.render_template('pages/privacy.jinja')


@main_blueprint.route('/announcement/<date>')
def announcement(date):
    if date == "2023-Nov-28":
        return f.render_template('pages/announcement-2023-11-28.jinja')

    return f.redirect(f.url_for('main.index'))
