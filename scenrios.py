"""
  scenrios.py
  Sprinkle

  Created by LeeKW on 2021/02/01.
"""

from kochat.app import Scenario
from do import do_call, do_schedule

call = Scenario(
    intent='call',
    api=do_call,
    senario={
        'Target': [],
    }
)

schedule = Scenario(
    intent='schedule',
    api=do_schedule,
    senario={
        'Date':[],
        'Subject':[],
        'Time':[],
        'Action':[],
    }
)