"""
  VoiceCommandComtroller.py
  Sprinkle

  Created by LeeKW on 2021/02/19.
"""


class VoiceCommand():
    def __init__(self):
        # self.userConn = DAO.getConn().users
        self.voiceCommandConn = DAO().getConn().users
        # 이거 DAO에 Singleton 패턴 적용하면 수정할 것.

    def 