import flask as f
from .config import Config


def create_app(config_class=Config):

    from .controllers.main.routes import main_bp

    app = f.Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main_bp)

    return app
