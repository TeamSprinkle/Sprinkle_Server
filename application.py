"""
  application.py
  Sprinkle

  Created by LeeKW on 2021/02/01.
"""

from flask import request

from kochat.app import KochatApi
from kochat.data import Dataset
from kochat.loss import CRFLoss, CosFace, CenterLoss, COCOLoss, CrossEntropyLoss
from kochat.model import intent, embed, entity
from kochat.proc import DistanceClassifier, GensimEmbedder, EntityRecognizer, SoftmaxClassifier

from sprinkle.scenarios.scenarios import call, schedule
from sprinkle.controllers.UserController import UserController
from sprinkle.controllers.VoiceCommandController import VoiceCommandController


userController = UserController()
voiceCommandControler = VoiceCommandController()

@kochat.app.route('/')
def index():
    # userController.searchUserById("1234567890")
    return "adsf"

@kochat.app.route('/users/init', methods=['POST'])
def init():
    userInfo = request.json
    return userController.createUser(userInfo)

@kochat.app.route('/command/test', methods=['GET'])
def test():
    command = request.args["command"]
    return voiceCommandControler.test(command)

# @kochat.app.route('/getUsers')
# def getUsers():
#     return userController.searchUser()


if __name__ == '__main__':
    kochat.app.run(port=8080, host='192.168.1.63')
