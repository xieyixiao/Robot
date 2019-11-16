#~ This script was generated automatically by drang&drop from Position Library
class MyClass(GeneratedClass):
    def __init__(self):
        try: # disable autoBind
          GeneratedClass.__init__(self, False)
        except TypeError: # if NAOqi < 1.14
          GeneratedClass.__init__( self )

    def onLoad(self):
        self.postureProxy = None
        try:
            self.postureProxy = ALProxy("ALRobotPosture")
            self.motionProxy = ALProxy("ALMotion")
        except:
            self.logger.error("Module 'ALRobotPosture' not found.")

    def onUnload(self):
        if(self.postureProxy != None):
            self.postureProxy.stopMove()

    def onInput_onStart(self):
        if(self.postureProxy != None):
            result = self.postureProxy.goToPosture("Stand", 0.8)
            self.motionProxy.wbEnableEffectorControl("Head", True)
            self.motionProxy.wbSetEffectorControl("Head", [0.0, 0.5, 0.0])
            self.motionProxy.wbEnableEffectorControl("Head",False)
            if(result):
                self.success()
            else:
                self.logger.error("Posture Stand is not a part of the standard posture library or robot cannot reach the posture")
                self.failure()
        else:
            self.failure()

    def onInput_onStop(self):
        self.onUnload() #~ it is recommanded to call onUnload of this box in a onStop method,               as the code written in onUnload is used to stop the box as well
        pass