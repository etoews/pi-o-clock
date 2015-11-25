import unittest

import mock

from clock import action


class TestAction(unittest.TestCase):

    @mock.patch('os.walk')
    @mock.patch('subprocess.call')
    def test_play_songs(self, mock_call, mock_walk):
        mock_walk.return_value = [
                ('/audio/songs', (), ('1.mp3', '2.mp3', '3.mp3'))]
        mock_call.return_value = 0

        action.play_songs(num=2)
        self.assertEqual(2, mock_call.call_count)
