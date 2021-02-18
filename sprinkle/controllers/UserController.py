"""
  UserController.py
  Sprinkle

  Created by LeeKW on 2021/02/04.
"""

from pymongo import MongoClient

class UserController():
    def __init__(self):
        # Database Init
        self.client = MongoClient("mongodb://sprinkle:bitbitr35@localhost:27017/sprinkle")

    def searchUser(self):
        """
        # deviceId로 유저의 정보를 찾는 매소드
        # 유저 정보가 있다면 True, 없다면 False 를 반환한다.

        # :param deviceId: 기기 고유의 ID
        # :return: 유저 정보 존재 여부
        """
        userInfo = self.client.sprinkle.users.find()
        
        for i in userInfo:
            print(i)
        
        return "dd"

    def searchUserById(self, deviceId: str) -> bool:
        """
        deviceId로 유저의 정보를 찾는 매소드
        유저 정보가 있다면 True, 없다면 False 를 반환한다.

        :param deviceId: 기기 고유의 ID
        :return: 유저 정보 존재 여부
        """
        userInfo = self.client.sprinkle.users.find({"deviceId":deviceId})

        if(userInfo.count() == 0):
            return False
        else:
            return True

    def searchUserByPhoneNum(self, phoneNum: str) -> bool:
        """
        phoneNum로 유저의 정보를 찾는 매소드
        유저 정보가 있다면 True, 없다면 False 를 반환한다.

        :param deviceId: 사용자 핸드폰 번호
        :return: 유저 정보 존재 여부
        """
        userInfo = self.client.sprinkle.users.find({"phoneNum":phoneNum})

        if(userInfo.count() == 0):
            return False
        else:
            return True

    def createUser(self):
        """
        새로운 사용자 정보를 Database에 저장하는 매소드
        기존에 동일한 정보가 있는지 확인하고 없다면 새로 저장한다.

        :param deviceId: 기기 고유의 ID
        :param phoneNum: 사용자 핸드폰 번호
        :param phonebooks: 사용자 전화번호부 이름 목록
        :return: 성공 여부
        """
        deviceId = "123123123"
        phoneNum = "010-3806-7756"
        # 핸드폰 번호가 NULL일수도 있다~
        phonebooks = ["곽성순", "이석주", "이현지"]   
        # 전화번호부가 NULL일수도 있따~

        if(self.searchUserById(deviceId)==False and self.searchUserByPhoneNum(phoneNum)==False):
            self.client.sprinkle.users.insert({
                "deviceId":deviceId,
                "phoneNum":phoneNum,
                "modelRoute":"/usr/local/sprinkle",
                "modelUpdateDate":"2021-02-04",
                "phonebooks":phonebooks
            })


        return "ddddd"
