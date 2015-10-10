import unittest

from clock import create_app
from clock import sched


class TestSched(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get_alarms(self):
        alarms = sched.get_alarms()
        self.assertGreater(len(alarms), 0)
