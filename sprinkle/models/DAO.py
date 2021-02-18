"""
  DAO.py
  Sprinkle

  Created by LeeKW on 2021/02/18.
"""

from pymongo import MongoClient


class DAO():
    def __init__(self):
        # Database Init
        self.conn = MongoClient("mongodb://sprinkle:bitbitr35@localhost:27017/sprinkle").sprinkle

    def getConn(self):
        return self.conn