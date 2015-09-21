import logging

from flask import Blueprint, jsonify

import sched

logger = logging.getLogger(__name__)
api = Blueprint('api', __name__)


@api.route('/alarms')
def get_alarms():
    alarms = sched.get_alarms()
    alarm_dicts = []

    for alarm in alarms:
        alarm_dict = alarm._asdict()
        alarm_dicts.append(alarm_dict)

    return jsonify(alarms=alarm_dicts)
