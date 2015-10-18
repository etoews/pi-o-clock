import fnmatch
import logging
import os
import random
from subprocess import call

from clock import bg

logger = logging.getLogger(__name__)


def play_songs(num=3):
    songs = []
    for root, _, filenames in os.walk('audio'):
        for filename in fnmatch.filter(filenames, '*.mp3'):
            songs.append(os.path.abspath(os.path.join(root, filename)))

    if not songs:
        logger.warn("No songs in %s", os.path.abspath('audio'))
        return

    n = num if num < len(songs) else len(songs)
    for _ in xrange(n):
        song = random.choice(songs)
        songs.remove(song)

        logger.debug("Playing %s", song)

        call(["mpg123", "-q", song])


def audio(filename):
    pass


def say(phrase):
    pass


def weather(postal_code):
    pass


def joke(phrase):
    pass


def pause():
    bg.running


def _get_running_job():
    print(bg.get_jobs(pending=False))

actions = {
    "play_songs": {
        "name": "Play Songs",
        "function": play_songs,
        "param": "number_of_songs",
        "param_description": "Number of Songs"
    },
    "say": {
        "name": "Say",
        "function": say,
        "param": "phrase",
        "param_description": "Phrase"
    },
    "weather": {
        "name": "Weather",
        "function": weather,
        "param": "postal_code",
        "param_description": "Postal Code"
    },
    "joke": {
        "name": "Joke",
        "function": joke,
        "param": "phrase",
        "param_description": "The joke"
    },
    "audio": {
        "name": "Audio",
        "function": audio,
        "param": "filename",
        "param_description": "The audio filename"
    }
}
