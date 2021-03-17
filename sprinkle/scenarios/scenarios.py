"""
  application.py
  Sprinkle

  Created by LeeKW on 2021/02/01.
"""

from kochat.app import Scenario
from kocrawl.dust import DustCrawler
from kocrawl.map import MapCrawler
from kocrawl.retaurant import RestaurantCrawler
from kocrawl.weather import WeatherCrawler
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

weather = Scenario(
    intent='weather',
    api=WeatherCrawler().request,
    scenario={
        'LOCATION': [],
        'DATE': ['오늘']
    }
)

dust = Scenario(
    intent='dust',
    api=DustCrawler().request,
    scenario={
        'LOCATION': [],
        'DATE': ['오늘']
    }
)

restaurant = Scenario(
    intent='restaurant',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['맛집']
    }
)

travel = Scenario(
    intent='travel',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['관광지']
    }
)