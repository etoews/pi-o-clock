from flask import Blueprint, render_template

from clock.sched import Alarm
from clock import sched
from forms import AlarmForm

views = Blueprint('views', __name__)


@views.route('/')
def get_alarms():
    alarms = sched.get_alarms()

    return render_template('alarms.html', alarms=alarms)


@views.route('/alarms/add')
def add_alarm():
    return render_template('alarm.html', mode='add', form=AlarmForm())


@views.route('/alarms/<alarm_id>')
def get_alarm(alarm_id):
    alarm = sched.get_alarm(Alarm(id=alarm_id))

    return render_template('alarm.html', mode='get', alarm=alarm)


@views.route('/alarms/<alarm_id>/play')
def play_alarm(alarm_id):
    alarm = sched.get_alarm(Alarm(id=alarm_id))
    sched.play_alarm(alarm)

    return render_template('alarm.html', alarm=alarm)


@views.route('/alarms/<alarm_id>/disable')
def disable_alarm(alarm_id):
    alarm = sched.get_alarm(Alarm(id=alarm_id))
    sched.play_alarm(alarm)

    return render_template('alarm.html', alarm=alarm)
