import logging

from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager

from apscheduler.schedulers.background import BackgroundScheduler

import alarm

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')

logger = logging.getLogger(__name__)
logger.debug("Welcome to Pi Clock")

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)

scheduler = BackgroundScheduler()
scheduler.add_jobstore('sqlalchemy', url='sqlite:///pi-clock.sqlite')
scheduler.add_job(alarm.play_song, id='play_song', trigger='cron',
                  day_of_week='mon-fri', hour=7)
scheduler.start()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass

    return render_template('index.html')

if __name__ == '__main__':
    manager.run()
