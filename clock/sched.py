from collections import namedtuple
import logging

from action import actions
from clock import bg

logger = logging.getLogger(__name__)


Alarm = namedtuple('Alarm', 'id name days hour minute next_run, action, param')
Alarm.__new__.__defaults__ = (None, None, None, None, None, None, None, None)


def add_alarm(alarm):
    logger.debug("Adding alarm %s", alarm)

    alarm_id = alarm.name.lower().replace(' ', '_')

    job = bg.add_job(
        actions[alarm.action]['function'],
        args=[alarm.param],
        id=alarm_id,
        name=alarm.name,
        trigger='cron',
        day_of_week=alarm.days,
        hour=alarm.hour,
        minute=alarm.minute)

    return job


def remove_alarm(alarm):
    logger.debug("Removing alarm %s", alarm)

    return bg.remove_job(alarm.id)


def list_alarms():
    return [_job_to_alarm(job) for job in bg.get_jobs()]


def get_alarm(alarm):
    return _job_to_alarm(bg.get_job(alarm.id))


def play_alarm(alarm):
    job = bg.get_job(alarm.id)
    job.func()


def disable_alarm(alarm):
    job = bg.get_job(alarm.id)
    job.pause()


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
