import socket
import time
from naoqi import ALProxy


class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        self.LISTEN_PORT = 8001  # 服务器监听端口
        self.ROBOT_IP = '192.168.43.191'
        self.ROBOT_PORT = 9559
        self.tts = ALProxy("ALTextToSpeech")
        self.motion = ALProxy("ALMotion")
        self.posture = ALProxy("ALRobotPosture")
        # put initialization code here
        pass

    def onUnload(self):
        # put clean-up code here
        pass

    def onInput_onStart(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ROBOT_IP, self.LISTEN_PORT))
        time.sleep(2)
        CONNECT = True
        while CONNECT == True:
            self.sock.send('REACHED')
            buffer = self.sock.recv(1024)
            if (buffer == "对方已收到请求"):
                break;
        self.sock.close()  # 与服务器端断开socket连接
        self.tts.say(buffer, "Chinese")
        self.motion.stopMove()
        self.onStopped()  # activate the output of the box
            # self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload()  # it is recommended to reuse the clean-up as the box is stopped
        self.onStopped()  # activate the output of the box