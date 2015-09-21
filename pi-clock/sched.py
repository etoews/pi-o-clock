from collections import namedtuple

from apscheduler.schedulers.background import BackgroundScheduler

import action

bg = BackgroundScheduler()
bg.add_jobstore('sqlalchemy', url='sqlite:///pi-clock.sqlite')
bg.start()

bg.remove_all_jobs()
bg.add_job(action.play_song, id='play_song', trigger='cron',
           day_of_week='mon-fri', hour=6, minute=45)

Alarm = namedtuple('Alarm', 'id days hour minute next_run')

def get_alarms():
    alarms = []

    for job in bg.get_jobs():
        alarm = Alarm(
            id=job.id,
            days=str(job.trigger.fields[4]),
            hour=int(str(job.trigger.fields[5])),
            minute=int(str(job.trigger.fields[6])),
            next_run=job.next_run_time)
        alarms.append(alarm)

    return alarms
