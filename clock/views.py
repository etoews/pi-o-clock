from flask import Blueprint, render_template, request, redirect, flash, url_for

from clock.sched import Alarm
from clock import sched
from forms import AlarmForm

views = Blueprint('views', __name__)


@views.route('/')
def list_alarms():
    alarms = sched.list_alarms()

    return render_template('alarm/list-alarms.html', alarms=alarms)


@views.route('/alarms/add', methods=['GET', 'POST'])
def add_alarm():

    if request.method == 'POST':
        alarm = Alarm(
            name=request.form['name'],
            days=request.form['days'],
            hour=request.form['hour'],
            minute=request.form['minute'],
            action=request.form['action'],
            param=request.form['param']
        )

        sched.add_alarm(alarm)

        flash('Added alarm {}'.format(alarm.name))

        return redirect(url_for('.list_alarms'))

    return render_template('alarm/add-alarm.html', form=AlarmForm())


@views.route('/alarms/<alarm_id>')
def get_alarm(alarm_id):
    alarm = sched.get_alarm(Alarm(id=alarm_id))

    return render_template('alarm/get-alarm.html', alarm=alarm)


@views.route('/alarms/<alarm_id>/play')
def play_alarm(alarm_id):
    alarm = sched.get_alarm(Alarm(id=alarm_id))
    sched.play_alarm(alarm)

    return render_template('alarm/get-alarm.html', alarm=alarm)


@views.route('/alarms/<alarm_id>/remove')
def remove_alarm(alarm_id):
    alarm = sched.get_alarm(Alarm(id=alarm_id))
    sched.remove_alarm(alarm)

    return redirect(url_for('.list_alarms'))


@views.route('/alarms/<alarm_id>/disable')
def disable_alarm(alarm_id):
    alarm = sched.get_alarm(Alarm(id=alarm_id))
    sched.play_alarm(alarm)

    return render_template('alarm/get-alarm.html', alarm=alarm)
