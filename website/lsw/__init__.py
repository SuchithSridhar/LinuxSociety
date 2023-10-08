import flask as f
import flask_login as fl
import flask_sqlalchemy as sqla
import flask_migrate as fm
from .config import Config


db = sqla.SQLAlchemy()
login_manager = fl.LoginManager()
login_manager.login_view = 'user.login'
migrate = fm.Migrate()


def initialize_database(db, app):
    with app.app_context():
        db.create_all()


def create_app(config_class=Config):

    from .controllers.main.routes import main_blueprint

    app = f.Flask(__name__)
    app.config.from_object(config_class)

    # db.init_app(app)
    # login_manager.init_app(app)
    # migrate.init_app(app, db)

    app.register_blueprint(main_blueprint)

    return app
