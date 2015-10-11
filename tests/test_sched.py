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
        alarm = Alarm(days='mon-fri', hour='7', )
        sched.add_alarm(alarm)

    def test_get_alarms(self):
        alarms = sched.get_alarms()
        self.assertEqual(len(alarms), 1)
