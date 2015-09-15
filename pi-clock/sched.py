from apscheduler.schedulers.background import BackgroundScheduler

import alarm

bg = BackgroundScheduler()
bg.add_jobstore('sqlalchemy', url='sqlite:///pi-clock.sqlite')
bg.start()


def alarms():
    return bg.get_jobs()
