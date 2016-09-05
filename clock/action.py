import fnmatch
import logging
import os
import random
import subprocess
from datetime import datetime

import requests

from clock import utils

logger = logging.getLogger(__name__)

__display = None


def clock_tick():
    time = datetime.now().strftime('%I%M')

    if time.startswith('0'):
        time = ' ' + time[1:]

    __display.clear()
    __display.set_colon(True)
    __display.print_number_str(time)
    __display.write_display()


def play_songs(num=3):
    num = int(num)
    songs = []

    for root, _, filenames in os.walk('audio/songs'):
        for filename in fnmatch.filter(filenames, '*.mp3'):
            songs.append(os.path.abspath(os.path.join(root, filename)))

    if not songs:
        logger.warn("No songs in %s", os.path.abspath('audio/songs'))
        return

    if num > len(songs):
        num = len(songs)

    for _ in xrange(num):
        song = random.choice(songs)
        songs.remove(song)

        logger.debug("Playing %s", song)
        subprocess.call(["mpg123", "-q", song])


def audio(filename):
    pass


def say(phrase):
    filename = utils.hyphenate(phrase) + '.mp3'
    filepath = os.path.abspath(
        os.path.join(os.getcwd(), 'audio', 'say', filename))

    if not os.path.exists(filepath):
        voicerss_api_key = os.environ.get('VOICERSS_API_KEY')
        params = {
            'key': voicerss_api_key,
            'src': phrase,
            'hl': 'en-gb',
            'f': '32khz_16bit_stereo'}
        response = requests.get('https://api.voicerss.org', params=params)

        # TODO: how about some error handling on the response

        with open(filepath, 'w') as f:
            f.write(response.content)

    logger.debug("Saying %s", filepath)

    subprocess.call(["mpg123", "-q", filepath])


def weather(postal_code):
    pass


def joke(phrase):
    pass


def configure_clock_display():
    try:
        from Adafruit_LED_Backpack import SevenSegment

        global __display
        __display = SevenSegment.SevenSegment()
        __display.begin()

        return True
    except IOError:
        logger.exception("Configuring the clock display failed."
                         "Continuing on anyway.")
        return True
    except ImportError:
        # The Adafruit_LED_Backpack package wasn't install so assume a clock
        # display isn't connected
        return False


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
