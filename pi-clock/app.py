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
app.register_blueprint(api, url_prefix='/api')

bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)


@app.route('/')
def get_alarms():
    alarms = sched.get_alarms()

    return render_template('alarms.html', alarms=alarms)

@app.route('/alarms/<alarm_id>')
def get_alarm(alarm_id):
    alarm = sched.get_alarm(alarm_id)

    return render_template('alarm.html', alarm=alarm)

if __name__ == '__main__':
    manager.run()
