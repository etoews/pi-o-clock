from flask import Blueprint, render_template

from sched import Alarm
import sched

views = Blueprint('views', __name__)


@views.route('/')
def get_alarms():
    alarms = sched.get_alarms()

    return render_template('alarms.html', alarms=alarms)

@views.route('/alarms/<alarm_id>')
def get_alarm(alarm_id):
    alarm = sched.get_alarm(Alarm(id=alarm_id))

    return render_template('alarm.html', alarm=alarm)
