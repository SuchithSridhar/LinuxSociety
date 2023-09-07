import flask as f
from ...config import Config


main_bp = f.Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return f.render_template('index.jinja')
