import logging
import sys

from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.moment import Moment

import sched

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')

logger = logging.getLogger(__name__)
logger.info("Welcome to Pi Clock")

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass

    alarms = sched.alarms()

    return render_template('index.html', alarms=alarms)

if __name__ == '__main__':
    manager.run()
