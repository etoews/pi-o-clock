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


def pause():
    bg.running


def _get_running_job():
    print(bg.get_jobs(pending=False))
