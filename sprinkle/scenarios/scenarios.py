"""
  application.py
  Sprinkle

  Created by LeeKW on 2021/02/01.
"""

from kochat.app import Scenario

from sprinkle.scenarios.call import do_call
from sprinkle.scenarios.schedule import do_schedule


call = Scenario(
    intent='call',
    api=do_call,
    scenario={
        'Target': [],
    }
)

schedule = Scenario(
    intent='schedule',
    api=do_schedule,
    scenario={
        'Date':["오늘"],
        'Subject':["일정"],
        'Time':["지금"],
        'Action':["잡다"],
    }
)
