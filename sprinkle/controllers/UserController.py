"""
  UserController.py
  Sprinkle

  Created by LeeKW on 2021/02/04.
"""

from sprinkle.models.User import User

class UserController():
    def __init__(self):
        self.user = User()

    def createUser(self, userInfo):
        """
        새로운 사용자 정보를 Database에 저장하는 메소드
        기존에 동일한 정보가 있는지 확인하고 없다면 새로 저장한다.

        :param deviceId: 기기 고유의 ID
        :param phoneNum: 사용자 핸드폰 번호
        :param phonebooks: 사용자 전화번호부 이름 목록
        :return: 성공 여부
        """
        deviceId = userInfo['deviceId']
        phoneNum = userInfo['phoneNum']
        phonebooks = userInfo['phonebooks']   

        print(deviceId)
        print(phoneNum)
        print(phonebooks)

        res = self.user.searchUserById(deviceId)
        if(res != None):
            # deviceId로 유저 정보가 존재하는 경우
            if(res["phoneNum"] != phoneNum):
                # 검색된 유저 정보의 전화번호와 입력받은 전화번호가 같지 않은 경우 (전화번호 변경)
                self.user.updatePhoneNum(deviceId, phoneNum)
                print("전화번호가 변경된 경우")
            self.updatePhonebooks(deviceId, phonebooks)
            print("기기번호와 전화번호가 모두 같은 경우")
        else:
            # deviceId로 유저 정보가 존재하지 않는 경우
            res = self.user.searchUserByPhoneNum(phoneNum)
            if(res != None):
                # phoneNum으로 유저 정보가 존재하는 경우 (기기 변경)
                self.user.updateDeviceId(phoneNum, deviceId)
                self.updatePhonebooks(deviceId, phonebooks)
                print("기기번호가 변경된 경우")
            else:
                # deviceId와 phoneNum의 정보가 모두 존재하지 않는 경우 (새로운 유저)
                res = self.user.createUser(deviceId, phoneNum, phonebooks)
                print("새로운 유저가 가입한 경우")
                if(res == True):
                    # 새로운 모델을 훈련하는 메소드 실행.
                    print("")
                else:
                    return "Fail"

        return "Success"

    def updatePhonebooks(self, deviceId, phonebooks):
       res = self.user.updatePhonebooks(deviceId, phonebooks) 

       #res 결과에 따라서
       #phonebooks의 update는 성공했지만 수정된 값이 없다면 그냥 진행
       #수정된 값이 있다면 모델을 다시 train

    def deleteUser(self):
        print("dd")





# blueprint
# 유저 명령 CRUD
# 유저 명령 처리 해서 반화하는거
# 일단 기본 모델을 가지고 수행하는 형태로

# Custom 모델은 다른작업하고 추후에