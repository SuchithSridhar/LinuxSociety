from lsw import create_app
import logging

app = create_app()

if __name__ == '__main__':
    logger = logging.getLogger('gunicorn.error')
    app.logger.handler.extend(gunicorn_error_logger.handlers)
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=False)
