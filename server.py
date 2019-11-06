import socket;
connection = None
from naoqi import ALProxy


class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
    def onLoad(self):
        self.ROBOT_IP = '192.168.43.191'
        self.ROBOT_PORT = 9559
        self.LISTEN_PORT = 8001
        self.tts = ALProxy("ALTextToSpeech")
        self.motion = ALProxy("ALMotion")
        self.posture = ALProxy("ALRobotPosture")
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ROBOT_IP, self.LISTEN_PORT))
        self.sock.listen(10)
        global connection
        CONNECT = True
        while CONNECT == True:
            connection, address = self.sock.accept()
            buffer = connection.recv(1024)
            if buffer =='REACHED':
                if self.motion.robotIsWakeUp() == False:
                    self.motion.wakeUp()
                connection.send("对方已收到请求")
                self.tts.say("收到","Chinese")
                connection.close()
                break;
            connection.close()  # 关闭当前socket连接，进入下一轮循环
        self.sock.close()
        self.onStopped()
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box