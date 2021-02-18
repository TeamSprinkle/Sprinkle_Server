"""
  User.py
  Sprinkle

  Created by LeeKW on 2021/02/09.
"""

from sprinkle.models.DAO import DAO

class User():
    def __init__(self):
        # self.userConn = DAO.getConn().users
        self.userConn = DAO().getConn().users
        # 이거 DAO에 Singleton 패턴 적용하면 수정할 것.

    def searchUserById(self, deviceId: str) -> dict:
        """
        deviceId로 유저의 정보를 찾는 메소드
        유저 정보가 있다면 유저의 정보를 
        없다면 None을 리턴한다

        :param deviceId: 기기 고유의 ID
        :return: 유저 정보 or None
        """
        userInfo = self.userConn.find({"deviceId":deviceId})

        if(userInfo.count() == 0):
            return None
        else:
            return userInfo.next()

    def searchUserByPhoneNum(self, phoneNum: str) -> bool:
        """
        phoneNum로 유저의 정보를 찾는 매소드
        유저 정보가 있다면 True, 없다면 False 를 반환한다.

        :param deviceId: 사용자 핸드폰 번호
        :return: 유저 정보 존재 여부
        """
        userInfo = self.userConn.find({"phoneNum":phoneNum})

        if(userInfo.count() == 0):
            return None
        else:
            return userInfo.next()

    def updatePhonebooks(self, deviceId, phonebooks):
        """
        deviceId에 해당하는 User의 phonebooks를 수정한다
        update 결과를 반환한다.

        :param deviceId: 사용자 기기호
        :return: Update 결과
        """
        query = {"deviceId" : deviceId}
        updateValue = { "$set" : {"phonebooks" : phonebooks}}

        res = self.userConn.update(query, updateValue)
        """
        res : mongodb update 결과
        key : value
        n
        nModified : 수정된 항목의 개수
        ok
        updateExisting : update의 성공여부? query의 성공여부?
        """     
        return res

        #phonebooks의 값이 같아서 업데이트가 수행이 되지 않았다? 그럼 모델 훈련이 필요 없지
        # 근데 수행 됐어? 그럼 훈ㄹ녀도 해야지..

    def updatePhoneNum(self, deviceId, phoneNum):
        """
        deviceId에 해당하는 User의 phoneNum을 수정한다
        update 성공여부를 반환한다.
        
        :param deviceId: 기기 고유의 ID
        :param phoneNum: 사용자 핸드폰 번호
        :return: 성공 여부
        """  
        query = {"deviceId" : deviceId}
        updateValue = { "$set" : {"phoneNum" : phoneNum}}

        res = self.userConn.update(query, updateValue)

        if(res["updatedExisting"] == True):
            return True
        else:
            return False

    def updateDeviceId(self, phoneNum, deviceId):
        query = {"phoneNum" : phoneNum}
        updateValue = { "$set" : {"deviceId" : deviceId}}

        res = self.userConn.update(query, updateValue)

        if(res["updatedExisting"] == True):
            return True
        else:
            return False

    def createUser(self, deviceId, phoneNum, phonebooks):
        """
        새로운 사용자 정보를 Database에 저장하는 매소드
        
        :param deviceId: 기기 고유의 ID
        :param phoneNum: 사용자 핸드폰 번호
        :param phonebooks: 사용자 전화번호부 이름 목록
        :return: 성공 여부
        """
        query = {"deviceId" : deviceId,
                 "phoneNum" : phoneNum,
                 "modelRoute" : "Training",
                 "modelUpdateDate" : None,
                 "phonebooks" : phonebooks
        }
        
        res = self.userConn.insert(query)
        
        print(res)

        return True
