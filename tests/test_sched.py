import os
import unittest

from clock import create_app
from clock import sched
from clock.sched import Alarm


class TestSched(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.app.config['DB_FILE'])
        os.remove(cls.app.config['LOG_FILE'])

    def test_add_alarm(self):
        alarm = Alarm(name='pi alarm', days='mon-fri', hour=3, minute=14,
                      action='play_songs', param=3)
        sched.add_alarm(alarm)

    def test_get_alarm(self):
        alarm = sched.get_alarm(Alarm(id='pi_alarm'))
        self.assertEqual(alarm.id, 'pi_alarm')
        self.assertEqual(alarm.name, 'pi alarm')

    def test_list_alarms(self):
        alarms = sched.list_alarms()
        self.assertEqual(len(alarms), 1)

        alarm = alarms[0]
        self.assertEqual(alarm.id, 'pi_alarm')
        self.assertEqual(alarm.name, 'pi alarm')
