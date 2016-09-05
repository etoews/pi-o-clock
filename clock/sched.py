from collections import namedtuple
import logging

import action
from action import actions
from clock import bg
from clock import utils

logger = logging.getLogger(__name__)


Alarm = namedtuple('Alarm', 'id name days hour minute next_run, action, param')
Alarm.__new__.__defaults__ = (None, None, None, None, None, None, None, None)


def add_alarm(alarm):
    logger.debug("Adding %s", alarm)

    alarm_id = utils.hyphenate(alarm.name)

    job = bg.add_job(
        actions[alarm.action]['function'],
        args=[alarm.param],
        id=alarm_id,
        name=alarm.name,
        trigger='cron',
        misfire_grace_time=30,
        day_of_week=alarm.days,
        hour=alarm.hour,
        minute=alarm.minute)

    return _job_to_alarm(job)


def remove_alarm(alarm):
    logger.debug("Removing %s", alarm)

    bg.remove_job(alarm.id)


def list_alarms():
    return [_job_to_alarm(job) for job in bg.get_jobs() if job.id != 'clock-tick']


def get_alarm(alarm):
    alarm = bg.get_job(alarm.id)

    if alarm is not None:
        return _job_to_alarm(alarm)
    else:
        return None


def play_alarm(alarm):
    job = bg.get_job(alarm.id)
    job.func(job.args[0])


def disable_alarm(alarm):
    job = bg.get_job(alarm.id)
    job.pause()


def add_pi_oclock_alarm():
    alarm = get_alarm(Alarm('pi-oclock'))

    if alarm is None:
        alarm = Alarm(name=u"Pi O'Clock", days=u'mon-sun', hour=15, minute=14,
                      action='say', param=u"It's Pi O'Clock!")
        alarm = add_alarm(alarm)

    play_alarm(alarm)


def add_clock_tick():
    if bg.get_job('clock-tick') is None:
        logger.debug("Adding Clock Tick")

        bg.add_job(
            action.clock_tick,
            id='clock-tick',
            name='Clock Tick',
            trigger='cron',
            misfire_grace_time=30,
            second=0)

    action.clock_tick()


def _job_to_alarm(job):
    action_id = job.func_ref.split(':')[1]
    action_name = actions[action_id]['name']

    return Alarm(
        action=action_name,
        param=job.args[0],
        id=job.id,
        name=job.name,
        days=str(job.trigger.fields[4]),
        hour=int(str(job.trigger.fields[5])),
        minute=int(str(job.trigger.fields[6])),
        next_run=job.next_run_time)
