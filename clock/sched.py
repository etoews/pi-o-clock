from collections import namedtuple

from clock import bg
import action


Alarm = namedtuple('Alarm', 'id days hour minute next_run')
Alarm.__new__.__defaults__ = (None, None, None, None, None)


def add_alarm(alarm):
    bg.add_job(
        action.play_songs,
        id=alarm.id,
        trigger='cron',
        day_of_week=alarm.days,
        hour=alarm.hour,
        minute=alarm.minute)


def remove_alarm(alarm):
    return bg.remove_job(alarm.id)


def get_alarms():
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
    return Alarm(
        id=job.id,
        days=str(job.trigger.fields[4]),
        hour=int(str(job.trigger.fields[5])),
        minute=int(str(job.trigger.fields[6])),
        next_run=job.next_run_time)
