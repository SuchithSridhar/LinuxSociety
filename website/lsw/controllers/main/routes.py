import flask as f

main_blueprint = f.Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return f.render_template('index.jinja')
