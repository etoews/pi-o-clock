import logging
import sys

from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

from config import config


logger = logging.getLogger(__name__)

bootstrap = Bootstrap()
moment = Moment()
bg = BackgroundScheduler()


def _configure_scheduler(url):
    bg.add_jobstore('sqlalchemy', url=url)
    bg.start()


def _configure_logging(file):
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: [%(name)s] %(message)s')

    stdout = logging.StreamHandler(sys.stdout)
    stdout.setFormatter(formatter)
    root_logger.addHandler(stdout)

    file_handler = logging.FileHandler(file)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config[env])

    config[env].init_app(app)
    _configure_logging(app.config['LOG_FILE'])
    logger.info("Welcome to Pi Clock")
    _configure_scheduler(app.config['SQLALCHEMY_DATABASE_URI'])

    bootstrap.init_app(app)
    moment.init_app(app)

    from views import views as views_bp
    app.register_blueprint(views_bp)


    return app
