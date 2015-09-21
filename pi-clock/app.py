import logging
import sys

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.moment import Moment

import sched
from api import api

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')

logger = logging.getLogger(__name__)
logger.info("Welcome to Pi Clock")

app = Flask(__name__)
app.register_blueprint(api)

bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)


@app.route('/')
def index():
    alarms = sched.get_alarms()

    return render_template('index.html', alarms=alarms)

if __name__ == '__main__':
    manager.run()
