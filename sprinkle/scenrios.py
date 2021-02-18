"""
  application.py
  Sprinkle

  Created by LeeKW on 2021/02/01.
"""

from kochat.app import Scenario
from sprinkle.do import do_call, do_schedule


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
        'Date':[],
        'Subject':[],
        'Time':[],
        'Action':[],
    }
)