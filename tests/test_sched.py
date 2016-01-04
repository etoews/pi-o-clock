import os
import unittest

from clock import create_app
from clock import sched
from clock.sched import Alarm


class TestSched(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('test')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.app.config['DB_FILE'])
        os.remove(cls.app.config['LOG_FILE'])

    def test_add_alarm_play_songs(self):
        alarm = Alarm(name='Pi Alarm', days='mon-fri', hour=3, minute=14,
                      action='play_songs', param=3)
        alarm_added = sched.add_alarm(alarm)
        self.assertEqual('pi-alarm', alarm_added.id)

    def test_get_alarm(self):
        alarm = sched.get_alarm(Alarm(id='pi-alarm'))
        self.assertEqual('pi-alarm', alarm.id)
        self.assertEqual('Pi Alarm', alarm.name)

    def test_list_alarms(self):
        alarms = sched.list_alarms()
        self.assertEqual(1, len(alarms))

    def test_remove_alarm(self):
        sched.remove_alarm(Alarm(id='pi-alarm'))

        self.assertIsNone(sched.get_alarm(Alarm(id='pi-alarm')))
