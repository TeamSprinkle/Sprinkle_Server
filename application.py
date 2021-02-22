"""
  application.py
  Sprinkle

  Created by LeeKW on 2021/02/01.
"""

from flask import Flask, request

from sprinkle.controllers.UserController import UserController
from sprinkle.controllers.VoiceCommandController import VoiceCommandController


userController = UserController()
voiceCommandControler = VoiceCommandController()

@app.route('/')
def index():
    # userController.searchUserById("1234567890")
    return "adsf"

@app.route('/users/init', methods=['POST'])
def init():
    userInfo = request.json
    return userController.createUser(userInfo)

@app.route('/command/test', methods=['GET'])
def test():
    return voiceCommandControler.test("천우한테 전화 걸어줘")

if __name__ == '__main__':
    app = Flask(__name__)
    app.run(port=8080, host='0.0.0.0')

