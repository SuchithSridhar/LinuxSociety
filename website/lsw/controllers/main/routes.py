import flask as f

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
        'degree': ''
    }

    for key in data:
        data[key] = f.request.form[key]

    print(data)

    return f.redirect(f.url_for('main.welcome'))


@main_blueprint.route('/welcome')
def welcome():
    return f.render_template('pages/welcome.jinja')
