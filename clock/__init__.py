import logging
import sys

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

logger = logging.getLogger(__name__)

bootstrap = Bootstrap()
moment = Moment()


def _configure_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: [%(name)s] %(message)s')

    stdout = logging.StreamHandler(sys.stdout)
    stdout.setFormatter(formatter)
    root_logger.addHandler(stdout)

    file_handler = logging.FileHandler('pi-clock.log')
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

def create_app():
    _configure_logging()
    logger.info("Welcome to Pi Clock")

    app = Flask(__name__)

    bootstrap.init_app(app)
    moment.init_app(app)

    from views import views as views_bp
    app.register_blueprint(views_bp)

    return app
